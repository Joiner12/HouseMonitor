import scrapy, Post
from YaohaoScrapy.items import YaohaoscrapyItem
from urllib import parse


class YaohaosSpider(scrapy.Spider):
    name = "YaohaoS"
    allowed_domains = ["cdzjryb.com"]
    # start_urls = ["https://zw.cdzjryb.com/lottery/accept/index"]
    start_urls = ["https://zw.cdzjryb.com/lottery/accept/projectList"]

    def parse(self, response):
        trs = response.xpath('//table/tr')
        for tr in trs:
            print(tr.xpath('//td[4]/text()').extract())
        # post请求
        Post()
        # https://zw.cdzjryb.com/lottery/accept/projectList
        """"""
        # url = response.xpath('//a[@id="projectList"]/@href').extract()
        # item = YaohaoscrapyItem()
        # # https://zw.cdzjryb.com/lottery/accept/projectList
        # # new_url = parse.urljoin(response.url, url[0].replace('./', ''))
        # yield scrapy.Request(parse.urljoin(response.url,
        #                                    url[0].replace('./', '')),
        #                      callback=self.get_registration_house)

    def get_registration_house(self, response):
        print(response.url)
        # '//*[@type="checkbox"]"'
        # /html[1]/body[1]/div[2]/table[1]/tbody[1]/tr[1]/td[2]
        trs = response.xpath('//*[@id="_projectInfo"]/tr')
        for tr in trs:
            print(tr.xpath('//td[4]/text()').extract())

        # '[@id="_projectInfo"]/tr/td[1]'
