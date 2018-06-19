<?php
/**
 * Created by PhpStorm.
 * User: chien
 * Date: 18/6/18
 * Time: 12:45
 */

namespace App\Models;

use Jenssegers\Mongodb\Eloquent\Model as Eloquent;


class UserProfileInfo extends Eloquent
{
    protected $table = 'user_profile_info';

    public function starPlayList() {
        return $this->hasOne(PlayList::class, 'id', 'star_play_list_id');
    }

    public function playList() {
        return $this->hasMany(PlayList::class, 'creator_id', 'id');
    }
}
