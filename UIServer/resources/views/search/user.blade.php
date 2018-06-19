@extends('layouts.app')

@section('title', '网易云音乐相似搜索')

@section('nav_right')
    <form action="{{ url('/search/user') }}" method="get" class="form-inline">
        <div class="input-group">
            <input class="form-control" type="search" name="kw" value="{{ $kw }}" placeholder="请输入你的名字">
            <button class="btn btn-outline-primary input-group-append" type="submit">搜索</button>
        </div>
    </form>
@endsection

@section('content')
    @if($users->count() > 0)
        <div class="alert alert-primary" role="alert">先生的名字太大众化啦，来选择正确的您</div>
    @else
        <div class="alert alert-danger" role="alert">您的名字太个性化了，暂未被收录哦</div>
    @endif
    <div class="row">
        @foreach($users as $user)
            <div class="col-12 col-sm-6 col-md-4 col-lg-3">
                <div class="card user-profile-card d-flex flex-row justify-content-center p-1">
                    <a href="https://music.163.com/#/user?id={{ $user->id }}" target="_blank">
                        <img class="card-img" src="{{ $user->avatar_image_url }}" alt="{{ $user->nick_name }}">
                    </a>
                    <div class="card-body">
                        <a href="{{ url('/intersection/user', $user->id) }}" class="single-line-text">{{ $user->nick_name }}</a>
                    </div>
                </div>
            </div>
        @endforeach
    </div>
    {{ $users->appends('kw', $kw)->links() }}
@endsection
