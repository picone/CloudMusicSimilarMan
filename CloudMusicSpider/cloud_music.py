# -*- coding: utf-8 -*-
import random

import urllib3
from Crypto.Cipher import AES
from binascii import b2a_hex
import hashlib
import json


class CloudMusicApi:

    __AES_KEY = b'e82ckenh8dichen8'

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

    def user_play_list(self, uid, offset=0, limit=1000):
        params = {
            'uid': str(uid),
            'offset': str(offset),
            'limit': str(limit),
        }
        return self._request_eapi('/eapi/user/playlist', b'/api/user/playlist/', params)

    def _request_eapi(self, gateway_path, request_path, params):
        params['all'] = 'true'
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
