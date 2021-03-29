import scrapy


class Zhihu1Spider(scrapy.Spider):
    name = 'zhihu_1'
    if False:
        allowed_domains = ['https://www.zhihu.com']
        start_urls = ['http://https://www.zhihu.com/question/409693519']
    else:
        allowed_domains = ['https://www.runoob.com']
        start_urls = ['https://www.runoob.com/w3cnote/scrapy-detail.html']
        
    def parse(self, response):
        filename = "zhihu.html"
        open(filename, 'w').write(response.body)
