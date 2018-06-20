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
 * @property $song_ids int[]
 */
class PlayList extends Eloquent
{
    protected $table = 'play_list';

    public function songs() {
        return Song::rawWhere(['id' => ['$in' => $this->song_ids]]);
    }
}
