# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class YaohaoscrapyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 区域
    district = scrapy.Field()
    # 项目名称
    project_name = scrapy.Field()
    # 预售证号
    pre_sale_id = scrapy.Field()
    # 预售范围
    pre_sale_range = scrapy.Field()
    # 住房套数
    house_total_num = scrapy.Field()
    # 开发商咨询电话
    developer_phone = scrapy.Field()
    # 登记开始时间
    registration_start_time = scrapy.Field()
    # 登记结束时间
    registration_end_time = scrapy.Field()
    # 名单外人员资格已释放时间
    # 名单内人员资格已释放时间
    # 预审码取得截止时间
    # 项目报名状态
    registration_status = scrapy.Field()
    # 登记规则
