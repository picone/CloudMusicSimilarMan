# -*- coding: utf-8 -*-
import json
import random

import scrapy
from scrapy import Request

from NeteaseCloudMusic.items.PlayListItem import PlayListItem
from NeteaseCloudMusic.items.UserProfileInfoItem import UserProfileInfoItem
from NeteaseCloudMusic.requests.WeapiRequest import WeapiRequest

user_profile_url = 'https://music.163.com/weapi/share/userprofile/info'


class MusicSpider(scrapy.Spider):
    name = 'music'
    allowed_domains = ['music.163.com']

    def start_requests(self):
        user_agent = []
        with open('user_agent.txt', 'r') as f:
            for line in f:
                user_agent.append(line.strip('\n'))
        for i in range(16356819, 1000000000):
            yield WeapiRequest(
                url=user_profile_url,
                formdata={
                    'userId': i,
                },
                referer='https://music.163.com/m/user/%d' % i,
                meta=dict(user_id=i),
                ua=random.choice(user_agent),
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
