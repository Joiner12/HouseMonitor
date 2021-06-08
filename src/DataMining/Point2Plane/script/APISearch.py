# -*- coding:utf-8-*-
"""
搜索给定位置周边环境
"""
from requests import get


class APISearch():
    UrlHead = "https://restapi.amap.com/v5/place/text?"
    APIKey = "key=d510b9d4b6de357d6084b22a7fb7b0a2"
    # key=<用户的key>&location=116.473168,39.993015&radius=10000

    def __init__(self):
        super().__init__()
        # 验证网站链接是否正确
        if True:
            TestUrl = self.UrlHead+self.APIKey + \
                "&keywords=北京大学&types=010101"
        else:
            TestUrl = "https://restapi.amap.com/v3/place/text?keywords=北京大学&city=beijing&output=xml&offset=20&page=1&key=d510b9d4b6de357d6084b22a7fb7b0a2&extensions=all"
        html = get(TestUrl).json()
        print(html["info"])

    # 搜索周边的学校
    def School(self):
        pass


if __name__ == "__main__":
    aps = APISearch()
