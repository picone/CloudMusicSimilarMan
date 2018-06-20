<?php
/**
 * Created by PhpStorm.
 * User: chien
 * Date: 18/6/18
 * Time: 16:39
 */

namespace App\Models;

use Jenssegers\Mongodb\Eloquent\Model as Eloquent;

/**
 * Class Song
 * @package App\Models
 * @property $artist_ids int[]
 */
class Song extends Eloquent
{
    protected $table = 'song';

    public function album() {
        return $this->hasOne(Album::class, 'id', 'album_id');
    }

    public function artist() {
        return Artist::rawWhere(['id' => ['$in' => $this->artist_ids]]);
    }
}
