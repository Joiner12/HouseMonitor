# -*- coding:utf-8 -*-
"""
    根据gatte-test.xlsx中记录的数据生成各种pyehcharts图。
"""
from os import path
from readDataFromExcel import DataFromExcel
import math
from datetime import datetime
import pandas as pd
from DrawBar import DrawBar
from DrawMap import DrawMap
from DrawLine import DrawLine
from DrawWordCloud import DrawWordCloud
from DrawPie import DrawPie
from GetFlightInfo import FlightInfo
from pyecharts.charts import Page
from bs4 import BeautifulSoup


class TimeCharts():
    def __init__(self, excelFile):
        self.exlsData = list()
        # 数据文件检查
        # todo:*.xlsx文件后缀检查
        if path.isfile(excelFile):
            self.gatte = excelFile
            df = DataFromExcel(self.gatte)
            self.exlsData = df.getData()
        else:
            self.gatte = "not a exist file"
            print("%s,doesn't exist\n" % (excelFile))

    """
        function:
            获取指定日期(2021-8-1)段内的记录数据
        definition:
            getDateSpecTime(self, startDay: str = "today", endDay: str = "today")
        params:
            startDay,起始日期
            endDay,结束日期
        return:
            pyecharts-Pie
    """

    def getDateSpecTime(self, startDay: str = "today", endDay: str = "today"):
        setTimeStrFormat = '%Y-%m-%d'
        retSegData = pd.DataFrame(columns=['起始', '终止', '事件', '时长', 'other'])
        if startDay == "today":
            startDay_i = datetime.now()
        else:
            startDay_i = datetime.strptime(startDay, setTimeStrFormat)

        if endDay == "today":
            endDay_i = datetime.now()
        else:
            endDay_i = datetime.strptime(endDay, setTimeStrFormat)

        key_name = list(self.exlsData.keys())
        for k in key_name:
            curSheet = self.exlsData[k]
            startTickList = curSheet['起始'].tolist()
            for j in startTickList:
                # 'datetime.time' -> 'datetime.datetime'
                jJudge = j.strftime(setTimeStrFormat)
                jJudge = datetime.strptime(jJudge, setTimeStrFormat)
                if jJudge >= startDay_i and jJudge <= endDay_i:
                    curIndex = startTickList.index(j)

                    retSegData = retSegData.append(
                        {
                            '起始': curSheet.iloc[curIndex, 0],
                            '终止': curSheet.iloc[curIndex, 1],
                            '事件': curSheet.iloc[curIndex, 2],
                            '时长': curSheet.iloc[curIndex, 3],
                            'other': curSheet.iloc[curIndex, 4],
                        },
                        ignore_index=True)
        return retSegData

    """
        function:
                daily pie(根据dateDraw设置参数绘制饼图)
        definition:
                def dailyPie(self,startDay: str = "today", endDay: str = "today")
        params:
                startDay,起始日期
                endDay,结束日期
        return:
                pyecharts-Pie

    """

    def dailyPie(self, startDay: str = "today", endDay: str = "today"):
        # today
        startDayIn = startDay
        endDayIn = endDay
        dataDraw = self.getDateSpecTime(startDayIn, endDayIn)
        pieData = mergeListToDict(dataDraw['事件'].tolist(),
                                  dataDraw['时长'].tolist())
        return DrawPie(pieData)

    """
        function:
            绘制一段时间内事件图云(默认为最近一周事件)
        definition:
            periodWordCloud(self)
        params:
            startDay,起始日期
            endDay,结束日期
        return:
            pyecharts-Pie
    """

    def periodWordCloud(self):
        word_dict = dict()
        curSheet = self.exlsData[list(self.exlsData.keys())[-1]]
        eventList = curSheet['事件'].tolist()
        eventStr = str()
        for j in eventList:
            eventStr += str(j)+"-"
        eventSplit = eventStr.split("-")
        for k in eventSplit:
            if k in word_dict.keys():
                word_dict[k] += 1
            else:
                word_dict[k] = 1
        word_mesh = list()
        for i in word_dict.keys():
            word_mesh.append([i, word_dict[i]])
        return DrawWordCloud(word_mesh, renderfile="..//html//wordCloudTest.html",
                             backgroundpic=" ")

    """
        function:
            绘制一段时间内事件时序图(默认为最近一天事件)
        definition:
            dailyLine(self, day="today")
        params:
            day,日期('%Y-%m-%d')
        return:
            pyecharts-Line
    """

    def dailyLine(self, day="today"):
        setTimeStrFormat = '%Y-%m-%d'
        if day == "today":
            Day_i = datetime.now()
        else:
            Day_i = datetime.strptime(day, setTimeStrFormat)

        key_name = list(self.exlsData.keys())
        event_x = list()
        event_y = list()
        for k in key_name:
            curSheet = self.exlsData[k]
            startTickList = curSheet['起始'].tolist()
            for j in startTickList:
                # 'datetime.time' -> 'datetime.datetime'
                jJudge = j.strftime(setTimeStrFormat)
                jJudge = datetime.strptime(jJudge, setTimeStrFormat)
                if jJudge == Day_i:
                    curIndex = startTickList.index(j)
                    event_x.append(str(curSheet.iloc[curIndex, 2]))
                    event_y.append(curSheet.iloc[curIndex, 3])
        if True:
            xDataIn = ['78', 'AOA\\AOD', '开会', 'paper', '发票', 'visual-code']
            yDataIn = [42, 5, 107, 52, 79, 60]
        else:
            xDataIn = event_x
            yDataIn = event_y
        return DrawLine(xDataIn, yDataIn)

    """
        function:
            绘制一段时间内事件柱状图(默认为最近一天事件)
        definition:
            dailyBar(self, day="today")
        params:
            day,日期('%Y-%m-%d')
        return:
            pyecharts-Bar
    """

    def dailyBar(self, day="today"):
        setTimeStrFormat = '%Y-%m-%d'
        if day == "today":
            Day_i = datetime.now()
        else:
            Day_i = datetime.strptime(day, setTimeStrFormat)

        key_name = list(self.exlsData.keys())
        event_x = list()
        event_y = list()
        for k in key_name:
            curSheet = self.exlsData[k]
            startTickList = curSheet['起始'].tolist()
            for j in startTickList:
                # 'datetime.time' -> 'datetime.datetime'
                jJudge = j.strftime(setTimeStrFormat)
                jJudge = datetime.strptime(jJudge, setTimeStrFormat)
                if jJudge == Day_i:
                    curIndex = startTickList.index(j)
                    event_x.append(str(curSheet.iloc[curIndex, 2]))
                    event_y.append(curSheet.iloc[curIndex, 3])
        if True:
            xDataIn = ['78', 'AOA\\AOD', '开会', 'paper', '发票', 'visual-code']
            yDataIn = [42, 5, 107, 52, 79, 60]
        else:
            xDataIn = event_x
            yDataIn = event_y
        return DrawBar(xDataIn, yDataIn)
    """
    函数:
        航班信息
    定义:
        flightMap(self)
    输入:
        updateData,bool
    输出:
        pyecharts,geo
    """

    def flightMap(self, updateData=False):
        if updateData:
            dateStamp = datetime.now().strftime("%Y-%m-%d")
            ArrivalFile = "..//data//"+dateStamp+"A.xlsx"
            DepartureFile = "..//data//"+dateStamp+"D.xlsx"
            FlightInfo(ArrivalFile, DepartureFile)
        else:
            ArrivalFile = "..//data//FlightArrival.xlsx"
            DepartureFile = "..//data//FlightDeparture.xlsx"
        return DrawMap(FlightArrivalFile=ArrivalFile,
                       FlightDepartureFile=DepartureFile)


"""
    函数:
        将两个list合并为dict，list_name标签列表，list_value值列表
    定义:
        def mergeListToDict(list_name, list_value)
    输入:
        list_name,name(list)
        list_value,value(list)
    输出:
        {'list_name',list_value}
"""


def mergeListToDict(list_name, list_value):
    # 删除nan
    list_name_c = list()
    for i in list_name:
        if isinstance(i, float):
            if not math.isnan(i):
                list_name_c.append(i)
        else:
            list_name_c.append(i)

    list_value_c = [x for x in list_value if not math.isnan(x)]
    mergeDict = dict()
    for k, j in zip(list_name_c, list_value_c):
        if k in list(mergeDict.keys()):
            mergeDict[k] = j + mergeDict[k]
        else:
            mergeDict[k] = j
    return mergeDict


"""
    main page
"""


def mainPage():
    mainHtml = "..//html//mainpage.html"
    Tc_1 = TimeCharts('..//data//gatte-test.xlsx')
    pieCt = Tc_1.dailyPie(startDay="2021-08-02", endDay="2021-08-04")
    wordcloudCt = Tc_1.periodWordCloud()
    lineCt = Tc_1.dailyLine("2021-8-5")
    barCt = Tc_1.dailyBar()
    mapCt = Tc_1.flightMap(updateData=False)
    # main page
    mainpage = Page(page_title="MainDaily😁",  # layout=Page.DraggablePageLayout
                    )
    mainpage.add(pieCt)
    mainpage.add(lineCt)
    mainpage.add(mapCt)
    mainpage.add(barCt)
    mainpage.add(wordcloudCt)
    mainpage.render(mainHtml)
    # 调整main page 布局
    # adjustMainPage(mainHtml)
    print("main page run finished...")


def adjustMainPage(mainpagefile="..//html//mainpage.html"):
    with open(mainpagefile, "r+", encoding='utf-8') as html:
        html_bf = BeautifulSoup(html, 'lxml')

        divs = html_bf.select('.chart-container')
        # pie
        divs[0]['style'] = "width:900px;height:500px;position:absolute;" + \
            "top:85px;left:0px;border-style:solid;border-color:#444444;border-width:0px;"
        # map
        divs[2]["style"] = "width:900px;height:500px;position:absolute;" + \
            "top:85px;left:960px;border-style:solid;border-color:#444444;border-width:0px;"
        # line
        divs[1]["style"] = "width:900px;height:480px;position:absolute;" + \
            "top:600px;left:0px;border-style:solid;border-color:#444444;border-width:0px;"
        # bar
        divs[3]["style"] = "width:900px;height:480px;position:absolute;" + \
            "top:600px;left:960px;border-style:solid;border-color:#444444;border-width:0px;"
        # wordcloud
        divs[4]["style"] = "width:300px;height:300px;position:absolute;" + \
            "top:200px;left:760px;border-style:solid;border-color:#444444;border-width:0px;"

        body = html_bf.find("body")
        body["style"] = "background-color:#D6D7C5;"
        # 增加header标签
        header = html_bf.find("header")
        if header is None:
            header = html_bf.new_tag("header")
            html_bf.html.body.insert(1, header)
        header.string = datetime.now().strftime("%Y-%m-%d")
        header["style"] = "background-color:#D6D7C5;font-size:50px;" + \
            "text-align:center;font-family:'Impact'"
        # 增加分割线
        hr = html_bf.find("hr")
        if hr is None:
            hr = html_bf.new_tag("hr")
            html_bf.html.body.insert(2, hr)
        html_new = str(html_bf)
        html.seek(0, 0)
        html.truncate()
        html.write(html_new)
        html.close()


if __name__ == "__main__":
    if False:
        mainPage()
    else:
        adjustMainPage()
