<!DOCTYPE html>
<html lang="{{ app()->getLocale() }}">
<head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="keywords" Content="网易云音乐,相似度对比">
    <meta name="description" content="网易云音乐">
    <meta name="author" content="467360687@qq.com">
    <meta name="csrf-token" content="{{ csrf_token() }}">
    <title>@yield('title')</title>
    <link href="{{ asset('css/app.css') }}" rel="stylesheet">
    @yield('css')
</head>
<body>
@include('layouts._nav')
<div class="container">
    @yield('content')
</div>
<script src="{{ asset('js/app.js') }}"></script>
@yield('script')
</body>
</html>
