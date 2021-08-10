# -*- coding:utf-8 -*-
import pyecharts.options as opts
from pyecharts.charts import Bar
from pyecharts.faker import Faker
from pyecharts.commons.utils import JsCode
from datetime import datetime


def DrawBar(xData=Faker.choose(), yData=Faker.values()):
    xDataIn = xData
    yDataIn = yData
    c = (
        Bar(init_opts=opts.InitOpts(page_title="Bar " +
            datetime.now().strftime('%Y-%m-%d')))
        .add_xaxis(xDataIn)
        .add_yaxis("Daily Event", yDataIn, category_gap="60%")
        .set_series_opts(
            itemstyle_opts={
                "normal": {
                    "color": JsCode(
                        """new echarts.graphic.LinearGradient(0, 0, 0, 1, [{
                offset: 0,
                color: 'rgba(0, 244, 255, 1)'
            }, {
                offset: 1,
                color: 'rgba(0, 77, 167, 1)'
            }], false)"""
                    ),
                    "barBorderRadius": [8, 8, 8, 8],
                    "shadowColor": "rgb(0, 160, 221)",
                }
            }
        )
        .set_global_opts(title_opts=opts.TitleOpts(title=""),
                         yaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(formatter="{value} /min")))
        .render("..//html//barTest.html")
    )
    return c


if __name__ == "__main__":
    DrawBar()
