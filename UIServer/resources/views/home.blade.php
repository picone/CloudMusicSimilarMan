@extends('layouts.app')

@section('title', '网易云音乐相似搜索')

@section('content')
    <div class="col-12 col-sm-10 col-md-8 col-lg-6 offset-0 offset-sm-1 offset-md-2 offset-lg-3">
        <form action="{{ url('/search/user') }}" method="get">
            <div class="input-group input-group-lg">
                <input type="text" name="kw" class="form-control" placeholder="请输入你的网易云音乐的名字">
                <div class="input-group-append">
                    <button type="submit" class="btn btn-primary">搜索</button>
                </div>
            </div>
        </form>
    </div>
@endsection
