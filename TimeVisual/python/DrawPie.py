# -*- coding:utf-8 -*-
from pyecharts import options as opts
from pyecharts.charts import Pie
from pyecharts.faker import Faker
""" 
    函数:
        调用pyecharts绘制饼状图
    定义:
        def DrawPie(value):
    输入:
        {'list_name',list_value}
        list_name,name(list)
        list_value,value(list)
        renderfile,渲染输出文件
    输出:
        c,html

"""


def DrawPie(valueDict, renderfile="..//html//pie.html"):
    data_b = [list(z) for z in zip(valueDict.keys(), valueDict.values())]
    c = (
        Pie().add(
            "",
            data_b,
            radius=["30%", "55%"],
            label_opts=opts.LabelOpts(
                position="outside",
                # formatter="{a|{a}}{abg|}\n{hr|}\n {b|{b}: }{c}  {per|{d}%}  ",
                formatter="{b|{b}: }{c}  {per|{d}%}  ",
                background_color="#eee",
                border_color="#aaa",
                border_width=1,
                border_radius=4,
                rich={
                    "a": {
                        "color": "#999",
                        "lineHeight": 22,
                        "align": "center"
                    },
                    "abg": {
                        "backgroundColor": "#e3e3e3",
                        "width": "100%",
                        "align": "right",
                        "height": 22,
                        "borderRadius": [4, 4, 0, 0],
                    },
                    "hr": {
                        "borderColor": "#aaa",
                        "width": "100%",
                        "borderWidth": 0.5,
                        "height": 0,
                    },
                    "b": {
                        "fontSize": 16,
                        "lineHeight": 33
                    },
                    "per": {
                        "color": "#eee",
                        "backgroundColor": "#334455",
                        "padding": [2, 4],
                        "borderRadius": 2,
                    },
                },
            ),
        ).set_global_opts(title_opts=opts.TitleOpts(
            title="Pie-Daily")).render(renderfile))
    return c
