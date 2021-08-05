# -*- coding:utf-8 -*-
# from pyecharts.faker import Faker
from pyecharts.charts import Pie, Bar, EffectScatter
from pyecharts.globals import SymbolType, ThemeType, ChartType
from pyecharts import options as opts
from readDataFromExcel import DataFromExcel

# https://gallery.pyecharts.org/#/Pie/pie_rich_label
CommuterData_o = DataFromExcel(
    "..//data//Commuter.xlsx").getData()
CommuterData = CommuterData_o['Sheet1']
fastSpeed = CommuterData.iloc[:, 7].tolist()
fastDate = ["{}天".format(i) for i in range(len(fastSpeed))]
speedFig_1 = (
    EffectScatter(init_opts=opts.InitOpts(
        theme=ThemeType.LIGHT, page_title="speed"))
    .add_xaxis(fastDate)
    .add_yaxis("speed",
               fastSpeed,
               symbol=SymbolType.ARROW)
    .set_global_opts(title_opts=opts.TitleOpts(title="Speed"))
)
speedFig_1.render("..//html//TimePyEcharts_1.html")
# %% motor data
