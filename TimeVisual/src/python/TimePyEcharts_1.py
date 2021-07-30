# -*- coding:utf-8 -*-
from pyecharts.faker import Faker
from pyecharts.charts import Pie
from pyecharts.charts import Bar
from pyecharts import options as opt
bar = Bar()
bar.add_xaxis(["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"])
bar.add_yaxis("商家A", [5, 20, 36, 10, 75, 90])

# %%
x = [list(z) for z in zip(Faker.choose(), Faker.values())]
pie_1 = Pie()
# bar.render(r"D:\Code\HouseMonitor\TimeVisual\src\html\TimePyEcharts_1.html")
