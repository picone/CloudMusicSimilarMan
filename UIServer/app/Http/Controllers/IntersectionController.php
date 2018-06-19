<?php
/**
 * Created by PhpStorm.
 * User: chien
 * Date: 18/6/18
 * Time: 14:57
 */

namespace App\Http\Controllers;


use App\Models\UserProfileInfo;
use Message\GetIntersectionRequest;
use Message\GetIntersectionResponse;
use Message\NeteaseMusicClient;

class IntersectionController extends Controller
{
    public function user($id) {
        $user = UserProfileInfo::where(['id' => intval($id)])->first();
        if (is_null($user)) {
            return view('error', ['message' => '用户不存在']);
        }
        $playList = $user->starPlayList;
        if (is_null($playList)) {
            return view('error', ['message' => '喜欢的歌单不存在']);
        }
        if (!is_array($playList->song_ids) || !isset($playList->song_ids[0])) {
            return view('error', ['message' => '未收藏喜欢的歌']);
        }
        $request = new GetIntersectionRequest();
        $request->setLimit(100);
        $request->setSongIds($playList->song_ids);
        /** @var $response GetIntersectionResponse */
        list($response, $status) = $this->getIntersection($request);
        var_dump($response->getIntersection());
        var_dump($response->getLimit());
        return view('intersection.user', compact('user', 'playList'));
    }

    protected function getIntersection($request) {
        return resolve(NeteaseMusicClient::class)->GetIntersection($request)->wait();
    }
}
