# -*- coding: utf-8 -*-
from cloud_music import CloudMusicApi

if __name__ == '__main__':
    api = CloudMusicApi()
    print(api.user_play_list(10001))
    play_list = api.play_list_detail(409947357, -1, 200)
    print(play_list['tracks'])
    song_ids = []
    for item in play_list['trackIds']:
        song_ids.append({'id': item['id'], 'v': 0})
    print(api.song_detail(song_ids[200:700]))
