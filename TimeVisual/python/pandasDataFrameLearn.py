# -*- coding:utf-8 -*-
"""
    panda data frame learn
    ref:
    https://blog.csdn.net/xtfge0915/article/details/52938740
"""
from readDataFromExcel import DataFromExcel
# import pandas as pd


""" 
    数据读取——single sheet
"""
testData = DataFromExcel(
    r"D:\Code\HouseMonitor\TimeVisual\data\Commuter.xlsx").getData()
print(testData)
# 通过列名字索引
d1 = testData['日期']
print(d1, type(d1))
d2 = testData.日期
d3 = (d2[1])

# 通过列号读取数据
print(testData.iloc[:, 7])
print(testData.iloc[:, 3:])
print(testData.iloc[:, 5:7])

# 通过行号读取数据
print(testData.iloc[1, :])
print(testData.iloc[1, 5])

# series to list
print(testData.iloc[:, 7].tolist())

# %%
""" 
    数据读取——multiple sheet
"""
df_1 = DataFromExcel(r"D:\Code\HouseMonitor\TimeVisual\data\gatte-test.xlsx")
exlsData_1 = df_1.getData()
if isinstance(exlsData_1, dict):
    keysDict = exlsData_1.keys()
    for k in keysDict:
        print(k)
    # sheet_20210315 = exlsData_1['2021-03-15']
# print(sheet_20210315)
