# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class HotzhihuItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    QuestionContent = scrapy.Field()
    QuestionKeyWord = scrapy.Field()
    QuestionAnswersId = scrapy.Field()
    QuestionAnswersDetail = scrapy.Field()
