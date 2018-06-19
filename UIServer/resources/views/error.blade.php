@extends('layouts.app')

@section('title', '网易云音乐相似搜索')

@section('content')
    <div class="alert alert-{{ $type ?? 'danger' }}" role="alert">
        {{ $message ?? '系统遇到错误了QAQ' }}
    </div>
@endsection
