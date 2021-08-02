# -*- coding:utf-8 -*-
# from pyecharts.faker import Faker
from pyecharts.charts import Pie, Bar, EffectScatter
from pyecharts.globals import SymbolType, ThemeType, ChartType
from pyecharts import options as opts
from readDataFromExcel import DataFromExcel

CommuterData = DataFromExcel(
    r"D:\Code\HouseMonitor\TimeVisual\data\Commuter.xlsx").getData()
fastSpeed = CommuterData.iloc[:, 7].tolist()
fastDate = ["{}天".format(i) for i in range(len(fastSpeed))]
speedFig_1 = (
    EffectScatter(init_opts=opts.InitOpts(
        theme=ThemeType.LIGHT, page_title="speed"))
    .add_xaxis(fastDate)
    .add_yaxis("speed", fastSpeed, symbol=SymbolType.ARROW)
    .set_global_opts(title_opts=opts.TitleOpts(title="Speed"))
)
speedFig_1.render(r"D:\Code\HouseMonitor\TimeVisual\html\TimePyEcharts_1.html")
# %% motor data
