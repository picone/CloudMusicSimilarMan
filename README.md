# *CloudMusicSimilarMan*

> 通过爬取网易云音乐所有用户“喜欢的音乐”歌单的歌曲，并与某一账号喜欢的歌曲求交集，把交集数量Tok-K的用户列举出来，深度挖掘与你有同样兴趣的用♂户。

## 项目构成

### 爬虫器

爬虫器使用[Scrapy](https://github.com/scrapy/scrapy)框架，爬取到的内容都存放到MongoDB中。[详细内容](https://github.com/picone/CloudMusicSimilarMan/tree/master/NeteaseCloudMusicSpider)。

### 后台服务

处理用户交集结果请求，求出交集最多的用户。项目试用Golang开发，应用[grpc](https://github.com/grpc/grpc-go)进行RPC通讯。

#### 特性

- 求交集使用RCF算法，参考《Faster upper bounding of intersection sizes》

### 前台渲染

用户页面渲染，结果缓存等。[详细内容](https://github.com/picone/CloudMusicSimilarMan/tree/master/UIServer)

## 捐赠

如果你觉得我的项目对你有帮助，欢迎捐赠。

<table>
  <tr>
    <th width="50%">微信</th>
    <th width="50%">支付宝</th>
  </tr>
  <tr></tr>
  <tr align="center">
    <td><img width="70%" src="https://github.com/picone/CloudMusicSimilarMan/tree/master/UIServer/public/img/wechat.png"></td>
    <td><img width="70%" src="https://github.com/picone/CloudMusicSimilarMan/tree/master/UIServer/public/img/alipay.png"></td>
  </tr>
</table>

## LICENSE

你可以在[GPL 3.0](https://github.com/picone/CloudMusicSimilarMan/blob/master/LICENSE)许可下自由使用本项目。

