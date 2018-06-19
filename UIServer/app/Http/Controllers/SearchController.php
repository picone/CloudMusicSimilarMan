<?php
/**
 * Created by PhpStorm.
 * User: chien
 * Date: 18/6/17
 * Time: 22:50
 */

namespace App\Http\Controllers;


use App\Models\UserProfileInfo;
use Illuminate\Http\Request;

class SearchController extends Controller
{
    public function user(Request $request) {
        $kw = $request->post('kw', '');
        if (!empty($kw)) {
            $users = UserProfileInfo::whereRaw(['$text' => ['$search' => $kw]])
                ->paginate(96, ['id', 'avatar_image_url', 'nick_name']);
        } else {
            $users = [];
        }
        return view('search.user', compact('users', 'kw'));
    }
}
