import base64
import binascii
import json
import os
from urllib.parse import urlencode

from Crypto.Cipher import AES
from scrapy import Request

MODULUS = ('00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7'
           'b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280'
           '104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932'
           '575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b'
           '3ece0462db0a22b8e7')
PUBKEY = '010001'
NONCE = b'0CoJUm6Qyw8W8jud'


class WeapiRequest(Request):

    def __init__(self, *args, **kwargs):
        formdata = kwargs.pop('formdata', None)
        referer = kwargs.pop('referer', None)
        ua = kwargs.pop('ua', None)
        kwargs['method'] = 'POST'
        self.user_id = kwargs.pop('user_id', None)
        if formdata:
            # csrf_token
            # formdata['csrf_token'] = ''
            # 对formdata进行加密
            formdata = _encrypt_formdata(formdata)

        super(WeapiRequest, self).__init__(*args, **kwargs)

        if referer:
            self.headers.setdefault(b'Referer', referer)
        if ua:
            self.headers['User-Agent'] = ua
        self.headers.setdefault(b'Content-Type', b'application/x-www-form-urlencoded')
        if formdata:
            self._set_body(urlencode(formdata))


def _encrypt_formdata(formdata):
    data = json.dumps(formdata).encode('utf-8')
    secret = _generate_key(16)
    params = _aes(_aes(data, NONCE), secret)
    encseckey = _rsa(secret, PUBKEY, MODULUS)
    return {'params': params, 'encSecKey': encseckey}


def _generate_key(size):
    return binascii.hexlify(os.urandom(size))[:16]


def _aes(text, key):
    pad = 16 - len(text) % 16
    text = text + bytearray([pad] * pad)
    encryptor = AES.new(key, 2, b'0102030405060708')
    ciphertext = encryptor.encrypt(text)
    return base64.b64encode(ciphertext)


def _rsa(text, pubkey, modulus):
    text = text[::-1]
    rs = pow(int(binascii.hexlify(text), 16), int(pubkey, 16), int(modulus, 16))
    return format(rs, 'x').zfill(256)
