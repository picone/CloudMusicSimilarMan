@extends('layouts.app')

@section('title', '网易云音乐相似搜索')

@section('content')
    <div class="alert alert-{{ $type ?? 'danger' }}" role="alert">
        <div>{{ $message or '系统遇到错误了QAQ' }}</div>
        @if(isset($backUrl))
            <a href="{{ $backUrl }}">返回</a>
        @endif
    </div>
@endsection
