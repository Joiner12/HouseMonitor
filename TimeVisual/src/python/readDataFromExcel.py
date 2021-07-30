# -*- coding:utf-8 -*-
"""
    功能：
         读取Excel文本中的时间、事件等数据到标准数据
"""

import pandas as pd


class DataFromExcel():
    exlsData = list()  # excel读取的数据

    def __init__(self, exlsFile):
        self.exlsData = "每一次记忆的翻腾 \n即美好又翻腾\n思念让旧情有余温\n将我困在早应该要离开的空城"
        print("每一次记忆的翻腾 \n即美好又翻腾\n思念让旧情有余温\n将我困在早应该要离开的空城")

    def getData(self):
        return self.exlsData


if __name__ == "__main__":
    df = DataFromExcel("只是那点不安")
    exlsData = df.getData()
