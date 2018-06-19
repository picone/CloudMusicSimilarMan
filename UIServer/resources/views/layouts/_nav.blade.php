<nav class="navbar navbar-expand-lg navbar-light bg-light">
    <a class="navbar-brand" href="{{ url('/') }}">网易云音乐相似搜索</a>
    <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#nvarbarContent">
        <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="nvarbarContent">
        <ul class="navbar-nav mr-auto">
            <li class="nav-item {{ request()->path() == '/' ? 'active' : '' }}">
                <a class="nav-link" href="{{ url('/') }}">搜相似</a>
            </li>
            <li class="nav-item {{ request()->path() == '/rank' ? 'active' : '' }}">
                <a class="nav-link" href="{{ url('/rank') }}">排行榜</a>
            </li>
            <li class="nav-item {{ request()->path() == '/donate' ? 'active' : '' }}">
                <a class="nav-link" href="{{ url('/donate') }}">捐赠</a>
            </li>
        </ul>
    </div>
    @yield('nav_right')
</nav>
