<?php
/**
 * Created by PhpStorm.
 * User: chien
 * Date: 18/6/18
 * Time: 15:44
 */

namespace App\Models;

use Jenssegers\Mongodb\Eloquent\Model as Eloquent;

/**
 * Class PlayList
 * @package App\Models
 * @property $song_ids array
 */
class PlayList extends Eloquent
{
    protected $table = 'play_list';

    public function songs() {
        return Song::where('id', 'in', $this->song_ids);
    }
}
