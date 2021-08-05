#%% :和→用法解释
# -*- coding:utf-8 -*-
from typing import Any, Optional, Sequence, Tuple, Union


def fund(a,
         font_style: Optional[str] = None,
         font_weight: Optional[str] = None,
         font_family: Optional[str] = None):
    print(a)
    opts: dict = {
        'font_style': font_style,
        'font_weight': font_weight,
        'font_family': font_family
    }
    print(opts)


fund(1)

#%% dataframe 数据拼接
"""
https://blog.csdn.net/sc179/article/details/108169436

"""
# 单列的内连接
import pandas as pd
import numpy as np
# 定义df1
df1 = pd.DataFrame({
    'alpha': ['A', 'B', 'B', 'C', 'D', 'E'],
    'feature1': [1, 1, 2, 3, 3, 1],
    'feature2': ['low', 'medium', 'medium', 'high', 'low', 'high']
})
# 定义df2
df2 = pd.DataFrame({
    'alpha': ['A', 'A', 'B', 'F'],
    'pazham': ['apple', 'orange', 'pine', 'pear'],
    'kilo': ['high', 'low', 'high', 'medium'],
    'price': np.array([5, 6, 5, 7])
})
# 基于共同列alpha的内连接
df3 = pd.merge(df1, df2, how='inner', on='alpha')

print(df1)
print(df2)
print(df3)

#
df1 = pd.DataFrame({
    'key': ['K0', 'K1', 'K2', 'K3', 'K4', 'K5'],
    'A': ['A0', 'A1', 'A2', 'A3', 'A4', 'A5']
})
df2 = pd.DataFrame({'key': ['K0', 'K1', 'K2'], 'B': ['B0', 'B1', 'B2']})

# lsuffix和rsuffix设置连接的后缀名
df3 = df1.join(df2, lsuffix='_caller', rsuffix='_other', how='inner')

print(df1)
print(df2)
print(df3)

#
df1 = pd.Series([1.1, 2.2, 3.3], index=['i1', 'i2', 'i3'])
df2 = pd.Series([4.4, 5.5, 6.6], index=['i2', 'i3', 'i4'])
print(df1)
print(df2)

# 行拼接
df3 = pd.concat([df1, df2])

print(df1)
print(df2)
print(df3)

# %% 动态修改dataframe
"""
https://blog.csdn.net/qq_39783601/article/details/104436303
https://www.yiibai.com/pandas/python_pandas_dataframe.html
"""
import pandas as pd
import numpy as np

initData = {'起始': 1, '终止': 2, '事件': 3, '时长': 5}
testData = pd.DataFrame(columns=['起始', '终止', '事件', '时长', 'other'])
testData = testData.append(initData, ignore_index=True)

#%%
from datetime import datetime

datetime.now()
a = datetime.strptime("2021-8-1", '%Y-%m-%d')
print(datetime.now() > datetime.strptime("2021-08-8", '%Y-%m-%d'))

#%%
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
testData = DataFromExcel("..//data//Commuter.xlsx").getData()
testData = testData['Sheet1']
print(testData)
# 通过列名字索引
# d1 = testData['日期']
# print(d1, type(d1))
# d2 = testData.日期
# d3 = (d2[1])

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
