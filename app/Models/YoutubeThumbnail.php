<?php

namespace App\Models;

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class YoutubeThumbnail extends Model
{
    use HasFactory;

    protected $fillable = [
        'youtube_id',
        'url',
        'height',
        'width',
    ];

    public function youtube()
    {
        return $this->belongsTo(Youtube::class);
    }
}
