import scrapy
import sys
reload(sys)
sys.setdefaultencoding("utf-8")


class Lianjia1Spider(scrapy.Spider):
    name = 'Lianjia_1'
    allowed_domains = ['lianjia.com']
    start_urls = ['https://cd.lianjia.com/']

    def parse(self, response):
        pass
