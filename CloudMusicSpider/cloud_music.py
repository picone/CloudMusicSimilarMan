# -*- coding: utf-8 -*-
import random

import urllib3
from Crypto.Cipher import AES
from binascii import b2a_hex
import hashlib
import json


class CloudMusicApi:

    __AES_KEY = b'e82ckenh8dichen8'
    """
    网易云音乐eapi调用
    
    :param num_pools: 线程池数量
    :param proxy: 若使用代理则传代理地址
    """
    def __init__(self, num_pools=10, proxy=None):
        headers = {
            'Accept': '*/*',
            'Origin': 'orpheus://orpheus',
            'Cookie': 'osver=%E7%89%88%E6%9C%AC%2010.13.6%EF%BC%88%E7%89%88%E5%8F%B7%2017G65%EF%BC%89;appver=1.5.9;'
                      'os=osx;channel=netease;',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/605.1.15 (KHTML, like Gecko)',
            'Accept-language': 'zh-cn',
            'Accept-encoding': 'gzip, deflate',
        }
        if proxy is None:
            self.__http_pool = urllib3.PoolManager(num_pools, headers)
        else:
            self.__http_pool = urllib3.ProxyManager(proxy, num_pools, headers)

    """
    获取用户播放列表
    
    :param uid: 用户ID
    :param offset: 偏移量
    :param limit: 每次获取的数量
    """
    def user_play_list(self, uid, offset=0, limit=1000):
        params = {
            'all': 'true',
            'uid': str(uid),
            'offset': str(offset),
            'limit': str(limit),
        }
        return self._request_eapi('/eapi/user/playlist', b'/api/user/playlist/', params)

    """
    获取歌单详情
    
    :param play_list_id: 播放列表ID
    :track_id_len: 获取歌曲id的数量
    :track_name_len: 获取具体歌曲名字的数量
    """
    def play_list_detail(self, play_list_id, track_id_len=-1, track_name_len=200):
        params = {
            'id': str(play_list_id),
            'c': '[]',
            't': str(track_id_len),
            'n': str(track_name_len),
            's': '0',
        }
        data = self._request_eapi('/eapi/v3/playlist/detail', b'/api/v3/playlist/detail', params)
        if data['code'] == 200:
            return data['playlist']
        else:
            return None

    """
    获取歌曲详情
    :param song_ids: 歌曲的id，需要传list({'id': xxx, 'v': 0})
    """
    def song_detail(self, song_ids):
        params = {
            'c': json.dumps(song_ids, separators=(',', ':')),
        }
        return self._request_eapi('/eapi/v3/song/detail/', b'/api/v3/song/detail/', params)

    def _request_eapi(self, gateway_path, request_path, params):
        params['verifyId'] = 1
        params['os'] = 'OSX'
        params['header'] = json.dumps({
            'os': 'osx',
            'appver': '1.5.9',
            'requestId': str(random.randint(10000000, 99999999)),
            'clientSign': '',
        }, separators=(',', ':'))
        params = self._encrypt(request_path, params)
        data = self._request(gateway_path, {'params': params}).data.decode('utf-8')
        return json.loads(data)

    def _request(self, path, data):
        url = 'http://music.163.com' + path
        return self.__http_pool.request('POST', url, data, encode_multipart=False)

    def _encrypt(self, path, params):
        params = json.dumps(params, separators=(',', ':')).encode('utf-8')
        sign_src = b'nobody' + path + b'use' + params + b'md5forencrypt'
        m = hashlib.md5()
        m.update(sign_src)
        sign = m.hexdigest()
        aes_src = path + b'-36cd479b6b5-' + params + b'-36cd479b6b5-' + sign.encode('utf-8')
        pad = 16 - len(aes_src) % 16
        aes_src = aes_src + bytearray([pad] * pad)
        encryptor = AES.new(self.__AES_KEY, AES.MODE_ECB)
        ret = encryptor.encrypt(aes_src)
        return b2a_hex(ret).upper()
