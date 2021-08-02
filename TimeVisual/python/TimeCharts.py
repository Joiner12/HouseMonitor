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

    def dailyPie(self, dateDraw):
        # 字典|列表——形参
        pass


if __name__ == "__main__":
    curTime = datetime.now().strftime('%Y-%m-%d')
    print(curTime, type(curTime))
