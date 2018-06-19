#网易云音乐相似搜索

## 使用

```shell
# 编译前端资源，若不开发可以忽略
npm install
npm run dev
# 安装PHP的资源
composer install
php artisan serve
```

## 环境要求

- PHP ^7.1.3
- MongoDB ^3.4

### PHP扩展

- [mongodb](http://pecl.php.net/package/mongodb)
- [protobuf](http://pecl.php.net/package/protobuf)
- [grpc](http://pecl.php.net/package/grpc)

## 特性

- 使用[Laravel](laravel.com)框架搭建
- 使用[MongoDB](mongodb.org)存储数据，使用[jenssegers/mongodb](https://github.com/jenssegers/laravel-mongodb)库辅助读写
- 使用[gRpc](grpc.io)与后端进行通讯

## 许可

你可以在[GPL 3.0](https://github.com/picone/CloudMusicSimilarMan/blob/master/LICENSE)许可下自由使用本项目。
