# -*- coding:utf-8 -*-
# from pyecharts.charts import Page, Grid
from pyecharts.charts import Pie
from pyecharts import options as opts

big_title = (Pie().set_global_opts(title_opts=opts.TitleOpts(
    title="2019-nCov",
    title_textstyle_opts=opts.TextStyleOpts(font_size=40,
                                            color='#111111',
                                            border_radius=True,
                                            border_color="white"),
    pos_top=0)).render("..//html//title1.html"))
