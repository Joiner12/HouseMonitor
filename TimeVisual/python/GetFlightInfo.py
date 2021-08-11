# -*- coding:utf-8 -*-
"""
    获取双流机场进出港航班信息
    http://www.cdairport.com/flightInfor.aspx?t=4
    Reference:
    1.https://zhuanlan.zhihu.com/p/394268763
    2.https://www.cnblogs.com/sanduzxcvbnm/p/10250222.html
"""
import requests
from bs4 import BeautifulSoup
import pandas as pd


class FlightInfo():
    arrivalUlrHead = r"http://www.cdairport.com/flightInfor.aspx?t=4&attribute=A&time=0&page="
    departureUrlHead = r"http://www.cdairport.com/flightInfor.aspx?t=4&attribute=D&time=0&page="
    htmlSelector = 'table'
    FlightInfoData = {'Arrial': None, 'Departure': None}

    def __init__(self):
        super().__init__()
        # check flight info
        self._getArrialInfo()
        self._getDepartureInfo()

    def _getArrialInfo(self):
        self.FlightInfoData['Arrial'] = getTableFromUrl(
            self.arrivalUlrHead, self.htmlSelector)
        print("我向你奔赴而来")

    def _getDepartureInfo(self):
        self.FlightInfoData['Departure'] = getTableFromUrl(
            self.departureUrlHead, self.htmlSelector)
        print("你就是星辰大海")

    def GetFlightData(self):
        return self.FlightInfoData


def getTableFromUrl(urlhead, selector):
    FlightInfo = pd.DataFrame()
    for k in range(1, 100, 1):
        url = urlhead+str(k)
        html = requests.get(url)
        # check html status
        if not html.status_code == 200:
            break
        soup = BeautifulSoup(html.text, "lxml")
        # 'table[class="arlineta departab"]'

        tab = soup.select(selector)[0]
        # prettify()优化代码,[0]从pd.read_html返回的list中提取出DataFrame
        curPage = pd.read_html(tab.prettify(), header=0)[0]
        if not curPage.empty:
            FlightInfo = pd.concat([FlightInfo, curPage])
        else:
            break
    # print(FlightInfo)
    return FlightInfo


if __name__ == "__main__":
    # getTableFromUrl(r"http://www.cdairport.com/flightInfor.aspx?t=4&attribute=A&time=0&page=",
    #                 'table')
    Fi = FlightInfo()
    a = Fi.GetFlightData()
