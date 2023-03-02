import scrapy
# from YaohaoScrapy.items import YaohaoscrapyItem
# from urllib import parse


class YaohaosSpider(scrapy.Spider):
    name = "YaohaoS"
    allowed_domains = ["cdzjryb.com"]
    start_urls = ["https://zw.cdzjryb.com/lottery/accept/index"]

    def start_requests(self):
        for k in range(10):
            yield scrapy.Request(
                url="https://zw.cdzjryb.com/lottery/accept/projectList",
                callback=self.parse)

    def parse(self, response):
        trs = response.xpath('//table/tr')
        for tr in trs:
            print(tr.xpath('//td[4]/text()').extract())

    def get_registration_house(self, response):
        pass
