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
        Schema::create('scrapes', function (Blueprint $table) {
            $table->id();
            $table->ubsignedBigInteger('publisher_id');
            $table->dateTime('schedule_to');
            $table->dateTime('dt_started')->nullable();
            $table->dateTime('dt_completed')->nullable();
            $table->string('status')->default('completed');
            $table->unsignedInteger('platforms_to_scrape')->nullable();
            $table->unsignedInteger('platforms_scraped')->nullable();
            $table->text('error')->nullable();
            $table->timestamps();
        });
    }

    /**
     * Reverse the migrations.
     */
    public function down(): void
    {
        Schema::dropIfExists('scrapes');
    }
};
