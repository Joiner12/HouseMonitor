# -*- coding:utf-8 -*-
"""
    根据gatte-test.xlsx中记录的数据生成各种pyehcharts图。
"""
from os import path
from readDataFromExcel import DataFromExcel
import math
from DrawPie import DrawPie


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
            curSheetName = key_name[-1]
            curSheetData = self.exlsData[curSheetName]
            pieData = mergeListToDict(
                curSheetData['事件'].tolist(), curSheetData['时长'].tolist())
            DrawPie(pieData)
        else:
            print("让我感到为难的\t是挣扎的自由")


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
            mergeDict[k] = j+mergeDict[k]
        else:
            mergeDict[k] = j
    return mergeDict


if __name__ == "__main__":
    Tc_1 = TimeCharts(r'D:\Code\HouseMonitor\TimeVisual\data\gatte-test.xlsx')
    # Tc_1 = TimeCharts(r'D:\Codes\HouseMonitor\TimeVisual\data\gatte-test.xlsx')
    Tc_1.dailyPie()
