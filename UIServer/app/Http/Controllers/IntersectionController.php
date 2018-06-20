<?php
/**
 * Created by PhpStorm.
 * User: chien
 * Date: 18/6/18
 * Time: 14:57
 */

namespace App\Http\Controllers;


use App\Models\UserProfileInfo;
use Illuminate\Support\Facades\Cache;
use Illuminate\Support\Facades\Log;
use Message\GetIntersectionRequest;
use Message\GetIntersectionResponse;
use Message\NeteaseMusicClient;
use Message\UserSongInfo;

class IntersectionController extends Controller
{
    public function user($id) {
        $user = UserProfileInfo::where(['id' => intval($id)])->first();
        if (is_null($user)) {
            return view('error', ['message' => '用户不存在']);
        }
        // 检查Cache
        $cacheKey = 'INTERSECTION:USER:' . $id;
        $intersection = Cache::get($cacheKey);
        if (is_null($intersection)) {
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
            if (is_null($response)) {
                Log::warning('Get intersection failed, code:' . $status->code . ',detail:' . $status->details);
                return view('error', [
                    'message' => '服务器暂时无法提供服务',
                    'backUrl' => url('/')
                ]);
            }
            // 转成array，不然序列化不了=，=
            $intersection['size'] = $response->getSize();
            foreach ($response->getIntersection() as $userSongInfo) {
                /** @var $userSongInfo UserSongInfo */
                $intersection['intersection'][] = [
                    'user_id' => $userSongInfo->getUserId(),
                    'intersection_size' => $userSongInfo->getIntersectionSize(),
                ];
            }
            Cache::put($cacheKey, $intersection, 86400);
        }
        $userIds = array_pluck($intersection['intersection'], 'user_id');
        $userInfoResult = UserProfileInfo::whereRaw(['id' => ['$in' => $userIds]])->get([
            'id', 'nick_name', 'avatar_image_url', 'play_count', 'create_play_list_count', 'star_play_list_id',
        ]);
        $userInfo = [];
        foreach ($userInfoResult as $item) {
            $userInfo[$item->id] = $item;
        }
        return view('intersection.user', compact('user', 'intersection', 'userInfo'));
    }

    protected function getIntersection($request) {
        return resolve(NeteaseMusicClient::class)->GetIntersection($request)->wait();
    }
}
