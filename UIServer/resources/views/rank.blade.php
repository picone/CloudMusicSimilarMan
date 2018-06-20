@extends('layouts.app')

@section('title', '排行榜')

@section('content')
    <div id="accordion">
        <div class="card">
            <div class="card-body">
                <div class="alert alert-info" role="alert" style="text-indent: 2em">
                    <div>这里是奇奇怪怪的排行榜，为了满足各位看官的好奇心而设立的，爬了的数据不用白不用嘛(*´∀`)~♥</div>
                    <div>我知道您还有很多神奇的需求没实现，可以通过<a href="{{ url('/donate') }}">这里</a>跟我说话哦_(:3 」∠ )_</div>
                </div>
            </div>
        </div>
        <div class="card">
            <div class="card-header">
                <h5 class="mb-0">
                    <button class="btn btn-link" data-toggle="collapse" data-target="#longestSong">
                        时间最长的歌曲
                    </button>
                </h5>
            </div>
            <div id="longestSong" class="collapse show" data-parent="#accordion">
                <div class="card-body">
                    是他是他就是他，名字叫《{{ $longestSong->name }}》，长度为{{ round($longestSong->length/1000/60) }}分钟，<a href="https://music.163.com/#/song?id={{ $longestSong->id }}" target="_blank">点击这里收听</a>。
                </div>
            </div>
        </div>
        <div class="card">
            <div class="card-header">
                <h5 class="mb-0">
                    <button class="btn btn-link collapsed" data-toggle="collapse" data-target="#shortestSong" aria-expanded="false" aria-controls="collapseTwo">
                        时间最短的歌曲
                    </button>
                </h5>
            </div>
            <div id="shortestSong" class="collapse" data-parent="#accordion">
                <div class="card-body">
                    没错，最快的歌就是他，名字叫《{{ $shortestSong->name }}》，只有{{ $shortestSong->length }}毫秒，<a href="https://music.163.com/#/song?id={{ $shortestSong->id }}" target="_blank">点击这里收听</a>。
                </div>
            </div>
        </div>
        <div class="card">
            <div class="card-header">
                <h5 class="mb-0">
                    <button class="btn btn-link collapsed" data-toggle="collapse" data-target="#maximumListenMan">
                        听歌数量最多的人
                    </button>
                </h5>
            </div>
            <div id="maximumListenMan" class="collapse" data-parent="#accordion">
                <div class="card-body">
                    你猜你猜你猜不到吧，就是<a href="https://music.163.com/m/user?id={{ $maximumListenMan->id }}" target="_blank">{{ $maximumListenMan->nick_name }}</a>，TA竟然听了{{ $maximumListenMan->play_count }}首歌，创建了{{ $maximumListenMan->create_play_list_count }}张歌单，收藏了{{ count($maximumListenMan->starPlayList->song_ids) }}首歌。
                </div>
            </div>
        </div>
    </div>
@endsection
