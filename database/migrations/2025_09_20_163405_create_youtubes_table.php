<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

return new class extends Migration
{
    /**
     * Run the migrations.
     */
public function up(): void
{
    Schema::create('youtubes', function (Blueprint $table) {
        $table->id();
        $table->string('youtube_id')->unique(); // ex: -yGHG3pnHLg
        $table->string('title');
        $table->text('description')->nullable();
        $table->string('url'); // link do vídeo
        $table->integer('duration')->nullable(); // em segundos
        $table->string('duration_string')->nullable(); // ex: 1:35:44
        $table->unsignedBigInteger('view_count')->nullable();

        // Info de canal/uploader
        $table->string('channel')->nullable();
        $table->string('channel_id')->nullable();
        $table->string('channel_url')->nullable();
        $table->string('uploader')->nullable();
        $table->string('uploader_id')->nullable();
        $table->string('uploader_url')->nullable();

        // Playlist
        $table->string('playlist')->nullable();
        $table->string('playlist_id')->nullable();
        $table->string('playlist_title')->nullable();
        $table->string('playlist_uploader')->nullable();
        $table->string('playlist_uploader_id')->nullable();
        $table->string('playlist_channel')->nullable();
        $table->string('playlist_channel_id')->nullable();
        $table->string('playlist_webpage_url')->nullable();
        $table->integer('playlist_index')->nullable();
        $table->integer('playlist_count')->nullable();

        // Datas e status
        $table->timestamp('timestamp')->nullable();
        $table->timestamp('release_timestamp')->nullable();
        $table->string('availability')->nullable();
        $table->boolean('live_status')->nullable();
        $table->boolean('channel_is_verified')->nullable();

        // URLs extras
        $table->string('webpage_url')->nullable();
        $table->string('original_url')->nullable();
        $table->string('webpage_url_basename')->nullable();
        $table->string('webpage_url_domain')->nullable();
        $table->string('extractor')->nullable();
        $table->string('extractor_key')->nullable();

        // Thumb principal
        $table->string('thumbnail_url')->nullable();

        $table->timestamps();
    });
}


    /**
     * Reverse the migrations.
     */
    public function down(): void
    {
        Schema::dropIfExists('youtubes');
    }
};
