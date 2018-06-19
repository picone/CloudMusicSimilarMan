# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
from pymongo.errors import DuplicateKeyError

from NeteaseCloudMusic.items.PlayListItem import PlayListItem
from NeteaseCloudMusic.items.UserProfileInfoItem import UserProfileInfoItem
from NeteaseCloudMusic.items.song import SongItem, AlbumItem, ArtistItem


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
            if 'song_ids' in item:
                self.db['play_list'].update_one({'id': item['id']}, {'$addToSet': {'song_ids': {'$each': item['song_ids']}}})
            else:
                self.db['play_list'].replace_one({'id': item['id']}, dict(item), True)
        elif isinstance(item, SongItem):
            self.db['song'].update_one({'id': item['id']}, {'$setOnInsert': dict(item)}, True)
        elif isinstance(item, AlbumItem):
            self.db['album'].update_one({'id': item['id']}, {'$setOnInsert': dict(item)}, True)
        elif isinstance(item, ArtistItem):
            self.db['artist'].update_one({'id': item['id']}, {'$setOnInsert': dict(item)}, True)
        return item
