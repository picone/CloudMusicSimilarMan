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
    <div>
        
    </div>
@endsection
