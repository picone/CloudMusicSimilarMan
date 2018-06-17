import scrapy


class SongItem(scrapy.Item):
    id = scrapy.Field()
    name = scrapy.Field()
    album_id = scrapy.Field()
    artist_ids = scrapy.Field()
    # MV
    mv = scrapy.Field()
    # 发布时间
    publish_time = scrapy.Field()
    # 版权
    copyright = scrapy.Field()
    # 歌曲长度
    length = scrapy.Field()


class AlbumItem(scrapy.Item):
    id = scrapy.Field()
    name = scrapy.Field()
    pic_url = scrapy.Field()


class ArtistItem(scrapy.Item):
    id = scrapy.Field()
    name = scrapy.Field()
