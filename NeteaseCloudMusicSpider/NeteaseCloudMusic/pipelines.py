# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
from pymongo.errors import BulkWriteError

from NeteaseCloudMusic.items.PlayListItem import PlayListItem
from NeteaseCloudMusic.items.UserProfileInfoItem import UserProfileInfoItem
from NeteaseCloudMusic.items.song import SongItem, AlbumItem, ArtistItem

BATCH_SIZE = 2000


class NeteaseCloudMusicPipeline(object):

    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db
        self.client = None
        self.db = None
        self.song_item = []
        self.artist_item = []
        self.album_item = []

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
            self.song_item.append(dict(item))
            if len(self.song_item) > BATCH_SIZE:
                try:
                    self.db['song'].insert_many(self.song_item, False)
                except BulkWriteError:
                    pass
                finally:
                    self.song_item = []
        elif isinstance(item, AlbumItem):
            self.album_item.append(dict(item))
            if len(self.album_item) > BATCH_SIZE:
                try:
                    self.db['album'].insert_many(self.album_item, False)
                except BulkWriteError:
                    pass
                finally:
                    self.album_item = []
        elif isinstance(item, ArtistItem):
            self.artist_item.append(dict(item))
            if len(self.artist_item) > BATCH_SIZE:
                try:
                    self.db['artist'].insert_many(self.artist_item, False)
                except BulkWriteError:
                    pass
                finally:
                    self.artist_item = []
        return item
