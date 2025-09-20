<?php

namespace App\Console\Commands;

use Illuminate\Console\Command;
use App\Models\Youtube;
use App\Models\YoutubeThumbnail;

class ImportYoutube extends Command
{
    protected $signature = 'youtube:import {file=storage/app/youtube/videos.json}';
    protected $description = 'Importa vídeos do arquivo JSON gerado pelo yt-dlp';

    public function handle()
    {
        $file = base_path($this->argument('file'));

        if (!file_exists($file)) {
            $this->error("Arquivo não encontrado: $file");
            return Command::FAILURE;
        }

        $this->info("Lendo arquivo: $file");

        $handle = fopen($file, "r");
        $count = 0;

        while (($line = fgets($handle)) !== false) {
            $line = trim($line);
            if (!$line) continue;

            $data = json_decode($line, true);
            if (!$data) continue;

            // pega a primeira thumb como principal
            $mainThumb = $data['thumbnails'][0]['url'] ?? null;

            // cria ou atualiza vídeo
            $youtube = Youtube::updateOrCreate(
                ['youtube_id' => $data['id']],
                [
                    'title' => $data['title'] ?? '',
                    'description' => $data['description'] ?? null,
                    'url' => $data['url'] ?? null,
                    'duration' => isset($data['duration']) ? intval($data['duration']) : null,
                    'duration_string' => $data['duration_string'] ?? null,
                    'view_count' => $data['view_count'] ?? null,

                    'channel' => $data['channel'] ?? null,
                    'channel_id' => $data['channel_id'] ?? null,
                    'channel_url' => $data['channel_url'] ?? null,
                    'uploader' => $data['uploader'] ?? null,
                    'uploader_id' => $data['uploader_id'] ?? null,
                    'uploader_url' => $data['uploader_url'] ?? null,

                    'playlist' => $data['playlist'] ?? null,
                    'playlist_id' => $data['playlist_id'] ?? null,
                    'playlist_title' => $data['playlist_title'] ?? null,
                    'playlist_uploader' => $data['playlist_uploader'] ?? null,
                    'playlist_uploader_id' => $data['playlist_uploader_id'] ?? null,
                    'playlist_channel' => $data['playlist_channel'] ?? null,
                    'playlist_channel_id' => $data['playlist_channel_id'] ?? null,
                    'playlist_webpage_url' => $data['playlist_webpage_url'] ?? null,
                    'playlist_index' => $data['playlist_index'] ?? null,
                    'playlist_count' => $data['playlist_count'] ?? null,

                    'timestamp' => isset($data['timestamp']) ? date('Y-m-d H:i:s', $data['timestamp']) : null,
                    'release_timestamp' => isset($data['release_timestamp']) ? date('Y-m-d H:i:s', $data['release_timestamp']) : null,
                    'availability' => $data['availability'] ?? null,
                    'live_status' => $data['live_status'] ?? null,
                    'channel_is_verified' => $data['channel_is_verified'] ?? null,

                    'webpage_url' => $data['webpage_url'] ?? null,
                    'original_url' => $data['original_url'] ?? null,
                    'webpage_url_basename' => $data['webpage_url_basename'] ?? null,
                    'webpage_url_domain' => $data['webpage_url_domain'] ?? null,
                    'extractor' => $data['extractor'] ?? null,
                    'extractor_key' => $data['extractor_key'] ?? null,

                    'thumbnail_url' => $mainThumb,
                ]
            );

            // thumbnails (remove e recria para não duplicar)
            $youtube->thumbnails()->delete();
            if (isset($data['thumbnails'])) {
                foreach ($data['thumbnails'] as $thumb) {
                    YoutubeThumbnail::create([
                        'youtube_id' => $youtube->id,
                        'url' => $thumb['url'],
                        'height' => $thumb['height'] ?? null,
                        'width' => $thumb['width'] ?? null,
                    ]);
                }
            }

            $count++;
        }

        fclose($handle);

        $this->info("Importação concluída: $count vídeos processados.");

        return Command::SUCCESS;
    }
}
