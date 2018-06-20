@extends('layouts.app')

@section('title', $user->nick_name . '的相似搜索')

@section('nav_right')
    <form action="{{ url('/search/user') }}" method="get" class="form-inline">
        <div class="input-group">
            <input class="form-control" type="search" name="kw" value="{{ $user->nick_name }}" placeholder="请输入你的名字">
            <button class="btn btn-outline-primary input-group-append" type="submit">搜索</button>
        </div>
    </form>
@endsection

@section('content')
    <div class="card">
        <div class="card-header">
            共有{{ $intersection['size'] }}条相近的记录
        </div>
        <div class="card-body">
            <div class="table-responsive ">
                <table class="table table-striped vertical-middle-table">
                    <thead>
                    <tr>
                        <th></th>
                        <th scope="col">昵称</th>
                        <th scope="col">听歌数</th>
                        <th scope="col">创建歌单数</th>
                        <th scope="col">交集数量</th>
                        <th></th>
                    </tr>
                    </thead>
                    <tbody>
                    @foreach($intersection['intersection'] as $item)
                        <?php $userItem = $userInfo[$item['user_id']];?>
                        <tr>
                            <td><img src="{{ $userItem->avatar_image_url }}" width="68" height="68"></td>
                            <td>
                                <a href="https://music.163.com/#/user?id={{ $userItem->id }}" target="_blank">{{ $userItem->nick_name }}</a>
                            </td>
                            <td>{{ $userItem->play_count }}</td>
                            <td>{{ $userItem->create_play_list_count }}</td>
                            <td>{{ $item['intersection_size'] }}</td>
                            <td>
                                <a href="https://music.163.com/#/playlist?id={{ $userItem->star_play_list_id }}" target="_blank">查看TA喜欢的歌单</a>
                            </td>
                        </tr>
                    @endforeach
                    </tbody>
                </table>
            </div>
        </div>
    </div>
@endsection
