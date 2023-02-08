import scrapy
from Lianjia.items import LianjiaItem


class LianjiaSpider(scrapy.Spider):
    name = "lianjia_qingyang"
    allowed_domains = ["cd.lianjia.com"]
    start_urls = ["https://cd.lianjia.com/xiaoqu/qingyang/"]

    def parse(self, response):
        title = response.xpath(
            r"/html/body/div[4]/div[1]/ul/li[1]/div[1]/div[1]/a").extract_first()

        print(title)
        pass
        # 存放信息
        # items = []
        # for each in response.xpath("//div[@class='clear xiaoquListItem']"):
        #     # 将得到的数据封装到一个 `LianjiaItem` 对象
        #     item = LianjiaItem()
        #     #extract()方法返回的都是unicode字符串
        #     name = each.xpath(
        #         "/html/body/div[4]/div[1]/ul/li[13]/div[2]/div[1]/div[1]"
        #     ).extract()
        #     title = each.xpath("h4/text()").extract()
        #     info = each.xpath("p/text()").extract()

        #     #xpath返回的是包含一个元素的列表
        #     item['name'] = name[0]
        #     item['title'] = title[0]
        #     item['info'] = info[0]

        #     items.append(item)