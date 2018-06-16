# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo

from NeteaseCloudMusic.items.PlayListItem import PlayListItem
from NeteaseCloudMusic.items.UserProfileInfoItem import UserProfileInfoItem


class NeteaseCloudMusicPipeline(object):

    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db
        self.client = None
        self.db = None

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=crawler.settings.get('MONGO_URI'),
            mongo_db=crawler.settings.get('MONGO_DATABASE')
        )

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        if isinstance(item, UserProfileInfoItem):
            self.db['user_profile_info'].replace_one({'id': item['id']}, dict(item), True)
        elif isinstance(item, PlayListItem):
            self.db['play_list'].replace_one({'id': item['id']}, dict(item), True)
        return item
