import scrapy


class PlayListItem(scrapy.Item):
    id = scrapy.Field()
    creator_id = scrapy.Field()
    name = scrapy.Field()
    cover_image_url = scrapy.Field()
    tags = scrapy.Field()
    play_count = scrapy.Field()
    track_count = scrapy.Field()
    comment_thread_id = scrapy.Field()
    create_time = scrapy.Field()
    update_time = scrapy.Field()
    song_ids = scrapy.Field()
