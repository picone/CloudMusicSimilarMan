@extends('layouts.app')

@section('title', '捐赠')

@section('content')
    <div class="card">
        <div class="card-body">
            <div class="alert alert-info" role="alert">
                <p style="text-indent: 2em">这个项目是作者呕心烈血，爬取网易云数据多天完成的，你懂我的意思了吧(ﾟ∀ﾟ)。同时，这个项目是开源的，你可以在<a href="https://github.com/picone/CloudMusicSimilarMan">这里</a>获取全部源码，并可以提出建设性建议。</p>
            </div>
            <div class="row">
                <div class="col-12 col-md-6">
                    <div class="card-header">微信支付</div>
                    <div class="card text-center">
                        <div class="card-body">
                            <img src="{{ asset('img/wechat.png') }}">
                        </div>
                    </div>
                </div>
                <div class="col-12 col-md-6">
                    <div class="card-header">支付宝</div>
                    <div class="card text-center">
                        <div class="card-body">
                            <img src="{{ asset('img/alipay.png') }}">
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
@endsection
