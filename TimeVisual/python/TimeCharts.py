# -*- coding:utf-8 -*-
"""
    根据gatte-test.xlsx中记录的数据生成各种pyehcharts图。
"""
from os import path
from readDataFromExcel import DataFromExcel
from datetime import datetime


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
            daily pie(根据dateDraw设置参数绘制饼图)
        definition: 
            dailyPie(self,dateDraw):
        params:
            dateDraw,需要绘图的日期
        return:
            pyecharts-Pie

    """

    def dailyPie(self, dateDraw="today"):
        # 字典|列表——形参
        # today
        if dateDraw == "today":
            # sheet name
            key_name = list(self.exlsData.keys())
            print(datetime.now().day)
        else:
            print("让我感到为难的\t是挣扎的自由")


if __name__ == "__main__":
    Tc_1 = TimeCharts(r'D:\Codes\HouseMonitor\TimeVisual\data\gatte-test.xlsx')
    Tc_1.dailyPie()
