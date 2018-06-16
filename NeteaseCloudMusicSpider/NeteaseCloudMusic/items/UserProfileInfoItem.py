import scrapy


class UserProfileInfoItem(scrapy.Item):
    id = scrapy.Field()
    nick_name = scrapy.Field()
    avatar_image_url = scrapy.Field()
    background_image_url = scrapy.Field()
    # 听歌数
    play_count = scrapy.Field()
    # 创建歌单数
    create_play_list_count = scrapy.Field()
    # 喜欢的音乐
    star_play_list_id = scrapy.Field()
