# -*- coding: utf-8 -*-
from cloud_music import CloudMusicApi

if __name__ == '__main__':
    api = CloudMusicApi()
    print(api.user_play_list(10001))
