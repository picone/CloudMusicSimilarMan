import time

from scrapy.http import Response

from haipproxy.client import ProxyFetcher

from twisted.internet.error import TimeoutError, ConnectionDone, ConnectError, ConnectionLost, TCPTimedOutError


class ProxyMiddleware(object):
    def __init__(self, redis_host, redis_port, redis_password, redis_db):
        args = dict(host=redis_host, port=redis_port, password=redis_password, db=redis_db)
        self.__fetcher = ProxyFetcher('https', redis_args=args)
        self.__start_time = 0

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            redis_host=crawler.settings.get('REDIS_HOST'),
            redis_port=crawler.settings.get('REDIS_PORT'),
            redis_password=crawler.settings.get('REDIS_PASSWORD'),
            redis_db=crawler.settings.get('REDIS_DB'),
        )

    def process_request(self, request, spider):
        self.__start_time = time.time()
        # 首次
        if 'proxy' not in request.meta:
            request.meta['proxy'] = self._get_next_proxy()
        # 重试3次失败后
        elif 'retry_times' in request.meta and request.meta['retry_times'] > 3:
            self.__fetcher.proxy_feedback('failure', request.meta['proxy'], self._get_cost_time())
            request.meta['proxy'] = self._get_next_proxy()
        return None

    def process_response(self, request, response, spider):
        if isinstance(response, Response):
            # 请求成功,检查是否460了
            if response.status == 200:
                if b'"code":460' in response.body or b'nickname' not in response.body:
                    # self.__fetcher.proxy_feedback('failure', request.meta['proxy'], self._get_cost_time())
                    self.__fetcher.delete_proxy(request.meta['proxy'])
                    spider.logger.debug('proxy %s is banned', request.meta['proxy'])
                    request.meta['proxy'] = self._get_next_proxy()
                    return request
                else:
                    self.__fetcher.proxy_feedback('success', request.meta['proxy'], self._get_cost_time())
            else:
                self.__fetcher.proxy_feedback('failure', request.meta['proxy'], self._get_cost_time())
                request.meta['proxy'] = self._get_next_proxy()
                return request
        return response

    def process_exception(self, request, exception, spider):
        if isinstance(exception, TimeoutError) or isinstance(exception, ConnectionAbortedError)\
                or isinstance(exception, ConnectError) or isinstance(exception, ConnectionLost)\
                or isinstance(exception, ConnectionDone) or isinstance(exception, TCPTimedOutError):
            self.__fetcher.proxy_feedback('failure', request.meta['proxy'], self._get_cost_time())
            request.meta['proxy'] = self._get_next_proxy()
            return request
        return None

    def _get_next_proxy(self):
        return self.__fetcher.get_proxy()

    def _get_cost_time(self):
        return (time.time() - self.__start_time) * 1000

    def _delete_proxy(self, proxy):
        self.__fetcher.delete_proxy(proxy)
