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
    Schema::create('youtube_thumbnails', function (Blueprint $table) {
        $table->id();
        $table->foreignId('youtube_id')->constrained('youtubes')->onDelete('cascade');
        $table->string('url');
        $table->integer('height')->nullable();
        $table->integer('width')->nullable();
        $table->timestamps();
    });
}

    /**
     * Reverse the migrations.
     */
    public function down(): void
    {
        Schema::dropIfExists('youtube_thumbnails');
    }
};
