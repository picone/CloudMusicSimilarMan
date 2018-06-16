# -*- coding: utf-8 -*-
import json
import os
import random

import scrapy

from NeteaseCloudMusic.items.PlayListItem import PlayListItem
from NeteaseCloudMusic.items.UserProfileInfoItem import UserProfileInfoItem
from NeteaseCloudMusic.requests.WeapiRequest import WeapiRequest

PLAY_LIST_LIMIT = 100

user_profile_url = 'http://music.163.com/weapi/share/userprofile/info'


class MusicSpider(scrapy.Spider):
    name = 'music'
    allowed_domains = ['music.163.com']

    def start_requests(self):
        for i in range(3458918, 1000000000):
            yield WeapiRequest(
                url=user_profile_url,
                formdata={
                    'userId': i,
                },
                referer='http://music.163.com/m/user/%d' % i,
                meta=dict(user_id=i),
                ua='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) %s' % os.urandom(random.randint(20, 50)),
            )

    def parse(self, response):
        resp = json.loads(response.body)
        if resp['code'] == 200 and 'nickname' in resp:
            user_profile_info_item = UserProfileInfoItem(
                id=response.meta['user_id'],
                nick_name=resp['nickname'],
                avatar_image_url=resp['avatarImg'],
                background_image_url=resp['backgroundUrl'],
                play_count=resp['playCount'],
                create_play_list_count=resp['createdplCnt'],
                star_play_list_id=resp['starPlaylist']['id'],
            )
            yield user_profile_info_item
            play_list_item = PlayListItem(
                id=resp['starPlaylist']['id'],
                creator_id=response.meta['user_id'],
                name=resp['starPlaylist']['name'],
                cover_image_url=resp['starPlaylist']['coverImgUrl'],
                tags=resp['starPlaylist']['tags'],
                play_count=resp['starPlaylist']['playCount'],
                track_count=resp['starPlaylist']['trackCount'],
                comment_thread_id=resp['starPlaylist']['commentThreadId'],
                create_time=resp['starPlaylist']['createTime'],
                update_time=resp['starPlaylist']['updateTime'],
            )
            yield play_list_item
