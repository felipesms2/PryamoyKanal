<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class Youtube extends Model
{
    use HasFactory;

    protected $fillable = [
        'youtube_id',          // 👈 este campo PRECISA estar aqui!
        'title',
        'description',
        'url',
        'duration',
        'duration_string',
        'view_count',
        'channel',
        'channel_id',
        'channel_url',
        'uploader',
        'uploader_id',
        'uploader_url',
        'playlist',
        'playlist_id',
        'playlist_title',
        'playlist_uploader',
        'playlist_uploader_id',
        'playlist_channel',
        'playlist_channel_id',
        'playlist_webpage_url',
        'playlist_index',
        'playlist_count',
        'timestamp',
        'release_timestamp',
        'availability',
        'live_status',
        'channel_is_verified',
        'webpage_url',
        'original_url',
        'webpage_url_basename',
        'webpage_url_domain',
        'extractor',
        'extractor_key',
        'thumbnail_url',       // 👈 não esquecer da thumb principal
    ];

    public function thumbnails()
    {
        return $this->hasMany(YoutubeThumbnail::class);
    }
}
