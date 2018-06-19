<?php
/**
 * Created by PhpStorm.
 * User: chien
 * Date: 18/6/18
 * Time: 17:40
 */

namespace App\Providers;


use Grpc\ChannelCredentials;
use Illuminate\Support\ServiceProvider;
use Message\NeteaseMusicClient;

class NeteaseMusicServiceProvider extends ServiceProvider
{
    protected $defer = true;

    public function register()
    {
        $this->app->singleton(NeteaseMusicClient::class, function ($app) {
            return new NeteaseMusicClient(env('NETEASE_MUSIC_SERVICE'), [
                'credentials' => ChannelCredentials::createInsecure(),
            ]);
        });
    }
}
