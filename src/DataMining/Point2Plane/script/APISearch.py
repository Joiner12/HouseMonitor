# -*- coding:utf-8-*-
"""
搜索给定位置周边环境
"""
from requests import get


class APISearch():
    UrlPart = {
        "urlhead":
        "https://restapi.amap.com/v3/place/around?key=6de2b5a95a0e35fc03782b55d455d8c4",
        "key": "&key=6de2b5a95a0e35fc03782b55d455d8c4",
        "keywords": "&keywords=学校|学校",
        "location": "&location=104.01775,30.489013",
        "radius": "&=5000"
    }

    def __init__(self):
        super().__init__()
        # 验证网站链接是否正确
        if True:
            TestUrl = self.UrlPart["urlhead"] + self.UrlPart[
                "location"] + self.UrlPart["radius"] + self.UrlPart["keywords"]
        else:
            TestUrl = "https://restapi.amap.com/v3/place/around?key=6de2b5a95a0e35fc03782b55d455d8c4&location=116.473168,39.993015&radius=10000&types=011100"
        html = get(TestUrl).json()
        pois = html['pois']
        for k in pois:
            print(k["type"] + "\n")
            # if k["type"].contains('科教文化服务;学校'):
            #     print(k)
        print(html["info"])

    # 搜索周边的学校
    def School(self):
        pass


if __name__ == "__main__":
    aps = APISearch()
