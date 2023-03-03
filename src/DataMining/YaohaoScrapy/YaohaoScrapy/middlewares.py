# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
from scrapy.http.response.html import HtmlResponse
# useful for handling different item types with a single interface
# from itemadapter import is_item, ItemAdapter
# rewrite middleware
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time
from random import random


class YaohaoscrapyDownloaderMiddleware:

    def __init__(self):
        self.driver = webdriver.Edge(
            executable_path=
            r"D:\Code\HouseMonitor\src\DataMining\Yaohao\driver\msedgedriver.exe",
            capabilities={
                "browserName": "MicrosoftEdge",
                "version": "",
                "platform": "WINDOWS",
                "ms:edgeOptions": {
                    'extensions': [],
                    'args': ['--headless']
                }
            })

    def __del__(self):
        self.driver.close()

    def process_request(self, request, spider):
        # 主页跳转
        page = request.meta.get('page', 1)
        if request.url == "https://zw.cdzjryb.com/lottery/accept/index":
            try:
                # print('使用 selenium 请求页面:{}'.format(request.url))
                self.driver.get(request.url)
                WebDriverWait(self.driver,
                              (By.XPATH, "/html/body/div[3]/ul[2]/a[1]/li"))
                self.driver.find_element(
                    By.XPATH, "/html/body/div[3]/ul[2]/a[1]/li").click()
                time.sleep(2 + 2 * random())
                # 将最后渲染得到的页面源码作为响应返回

                return HtmlResponse(url=self.driver.current_url,
                                    body=self.driver.page_source,
                                    request=request,
                                    encoding='utf-8')
            except:
                return HtmlResponse(url=request.url,
                                    status=500,
                                    request=request)

        if request.url == "https://zw.cdzjryb.com/lottery/accept/projectList":
            try:
                # print('使用 selenium 请求页面:{}'.format(request.url))
                self.driver.get(request.url)
                WebDriverWait(self.driver,
                              (By.XPATH, "/html/body/div[3]/ul[2]/a[1]/li"))
                # 点击下一页更新
                next_button = self.driver.find_element(
                    By.XPATH, "/html/body/div[2]/div[3]/a[8]")
                next_button.click()
                if False:
                    page_num = self.driver.find_element(
                        By.CSS_SELECTOR,
                        "body > div.nav.nav-nobg > div.pages-box > a.on").text
                    cut_str = "*" * 20 + "\r\n" + '|{: ^18}|\r\n'.format(
                        int(page_num)) + "*" * 20
                    print(cut_str)
                time.sleep(1 + 2 * random())
                return HtmlResponse(url=self.driver.current_url,
                                    body=self.driver.page_source,
                                    request=request,
                                    encoding='utf-8',
                                    status=200)
            except:
                return HtmlResponse(url=request.url,
                                    status=500,
                                    request=request)

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info("Spider opened: %s" % spider.name)


class YaohaoscrapySpiderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, or item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Request or item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info("Spider opened: %s" % spider.name)


# class YaohaoscrapyDownloaderMiddleware:
#     # Not all methods need to be defined. If a method is not defined,
#     # scrapy acts as if the downloader middleware does not modify the
#     # passed objects.

#     @classmethod
#     def from_crawler(cls, crawler):
#         # This method is used by Scrapy to create your spiders.
#         s = cls()
#         crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
#         return s

#     def process_request(self, request, spider):
#         # Called for each request that goes through the downloader
#         # middleware.

#         # Must either:
#         # - return None: continue processing this request
#         # - or return a Response object
#         # - or return a Request object
#         # - or raise IgnoreRequest: process_exception() methods of
#         #   installed downloader middleware will be called
#         return None

#     def process_response(self, request, response, spider):
#         # Called with the response returned from the downloader.

#         # Must either;
#         # - return a Response object
#         # - return a Request object
#         # - or raise IgnoreRequest
#         return response

#     def process_exception(self, request, exception, spider):
#         # Called when a download handler or a process_request()
#         # (from other downloader middleware) raises an exception.

#         # Must either:
#         # - return None: continue processing this exception
#         # - return a Response object: stops process_exception() chain
#         # - return a Request object: stops process_exception() chain
#         pass

#     def spider_opened(self, spider):
#         spider.logger.info("Spider opened: %s" % spider.name)
