# 网易云音乐爬虫

## 反爬虫要点

- POST参数加密算法参考[darknessomi/musicbox](https://github.com/darknessomi/musicbox/blob/master/NEMbox/api.py)
- 使用IP代理
- 动态的User-Agent，不能只改版本号，需要带上一段随机长度的字符
- 要带上Referer

## 使用到的第三方库

- [Redis](https://redis.io)
- [MongoDB](https://www.mongodb.com)
- [haipproxy](https://github.com/SpiderClub/haipproxy)
