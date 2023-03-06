import scrapy
# from YaohaoScrapy.items import YaohaoscrapyItem
# from urllib import parse


class YaohaosSpider(scrapy.Spider):
    name = "YaohaoS"
    allowed_domains = ["cdzjryb.com"]
    start_urls = ["https://zw.cdzjryb.com/lottery/accept/index"]

    def parse(self, response):
        yield scrapy.Request(
            url="https://zw.cdzjryb.com/lottery/accept/projectList",
            callback=self.parse,
            dont_filter=True)

    def get_registration_house(self, response):
        quatar_name = response.xpath(
            '//table//tbody/tr[1]/td[4]/text()').extract()
        print(quatar_name)
        # trs = response.xpath('//table//tbody/tr[1]/td[1]/text()').extract()
        # for tr in trs:
        #     print(tr.xpath('//td[4]/text()').extract())
