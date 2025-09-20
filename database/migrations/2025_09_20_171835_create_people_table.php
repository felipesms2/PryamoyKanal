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
        Schema::create('people', function (Blueprint $table) {
            $table->id();
            $table->string('name');
            $table->unsignedBigInteger('user_id')->nullable();
            $table->string('preffered_alias')->nullable();
            $table->dateTime('dt_request_as_publisher')->nullable();
            $table->dateTime('dt_authorized_as_publisher')->nullable();
            $table->string('invite_code')->nullable();
            $table->string('invited_code')->nullable();
            $table->unsignedBigInteger('user_id_invited');
            $table->unsignedBigInteger('people_id_invited');
            $table->timestamps();
        });
    }

    /**
     * Reverse the migrations.
     */
    public function down(): void
    {
        Schema::dropIfExists('people');
    }
};
