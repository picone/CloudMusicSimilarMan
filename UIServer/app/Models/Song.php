<?php
/**
 * Created by PhpStorm.
 * User: chien
 * Date: 18/6/18
 * Time: 16:39
 */

namespace App\Models;

use Jenssegers\Mongodb\Eloquent\Model as Eloquent;

class Song extends Eloquent
{
    protected $table = 'song';

    public function album() {
        return $this->hasOne(Album::class, 'id', 'album_id');
    }
}
