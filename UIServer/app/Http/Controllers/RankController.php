<?php
/**
 * Created by PhpStorm.
 * User: chien
 * Date: 18/6/20
 * Time: 15:06
 */

namespace App\Http\Controllers;


use App\Models\Song;
use App\Models\UserProfileInfo;
use Illuminate\Support\Facades\Cache;

class RankController extends Controller
{
    const RANK_CACHE_TIME = 86400;

    public function show() {
        // 时间最长的歌曲
        $longestSong = Cache::remember('RANK:longest_song', self::RANK_CACHE_TIME, function() {
            return Song::orderBy('length', 'desc')->first();
        });
        // 时间最短的歌曲
        $shortestSong = Cache::remember('RANK:shortest_song', self::RANK_CACHE_TIME, function (){
            return Song::whereRaw(['length' => ['$gt' => 470]])->orderBy('length', 'asc')->first();
        });
        // 听歌数最多的人
        $maximumListenMan = Cache::remember('RANK:maximum_listen_man', self::RANK_CACHE_TIME, function (){
            return UserProfileInfo::orderBy('play_count', 'desc')->first();
        });
        return view('rank', compact('longestSong', 'shortestSong', 'maximumListenMan'));
    }
}
