# -*- coding:utf-8 -*-
import pyecharts.options as opts
from pyecharts.charts import Line
from pyecharts.commons.utils import JsCode
from datetime import datetime
from pyecharts.faker import Faker


def DrawLine(xData=Faker.choose(), yData=Faker.values()):
    xDataIn = xData
    yDataIn = yData
    # js color
    background_color_js = (
        "new echarts.graphic.LinearGradient(0, 0, 0, 1, "
        "[{offset: 0, color: '#C9E6EF'}, {offset: 1, color: '#287086'}], false)"
    )
    area_color_js = (
        "new echarts.graphic.LinearGradient(0, 0, 0, 1, "
        "[{offset: 0, color: '#eb64fb'}, {offset: 1, color: '#3fbbff0d'}], false)"
    )

    c = (
        Line(init_opts=opts.InitOpts(bg_color=JsCode(
            background_color_js), page_title="Line "+datetime.now().strftime('%Y-%m-%d')))
        .add_xaxis(xaxis_data=xDataIn)
        .add_yaxis(
            series_name="Period Event",
            y_axis=yDataIn,
            is_smooth=True,
            is_symbol_show=True,
            symbol="circle",
            symbol_size=6,
            linestyle_opts=opts.LineStyleOpts(color="#fff"),
            label_opts=opts.LabelOpts(
                is_show=True, position="top", color="white"),
            itemstyle_opts=opts.ItemStyleOpts(
                color="red", border_color="#fff", border_width=3
            ),
            tooltip_opts=opts.TooltipOpts(is_show=True),
            areastyle_opts=opts.AreaStyleOpts(
                color=JsCode(area_color_js), opacity=1),
        )
        .set_global_opts(
            # title_opts=opts.TitleOpts(
            #     title="Daily-Activity",
            #     pos_top="10%",
            #     pos_left="center",
            #     title_textstyle_opts=opts.TextStyleOpts(
            #         color="#fff", font_size=20),
            # ),
            xaxis_opts=opts.AxisOpts(
                type_="category",
                boundary_gap=False,
                axislabel_opts=opts.LabelOpts(margin=30, color="#ffffff63"),
                axisline_opts=opts.AxisLineOpts(is_show=False),
                axistick_opts=opts.AxisTickOpts(
                    is_show=True,
                    length=25,
                    linestyle_opts=opts.LineStyleOpts(color="#ffffff1f"),
                ),
                splitline_opts=opts.SplitLineOpts(
                    is_show=True, linestyle_opts=opts.LineStyleOpts(color="#ffffff1f")
                ),
            ),
            yaxis_opts=opts.AxisOpts(
                type_="value",
                position="right",
                axislabel_opts=opts.LabelOpts(margin=20, color="#ffffff63"),
                axisline_opts=opts.AxisLineOpts(
                    linestyle_opts=opts.LineStyleOpts(color="#fff")
                ),
                axistick_opts=opts.AxisTickOpts(
                    is_show=True,
                    length=15,
                    linestyle_opts=opts.LineStyleOpts(color="#ffffff1f"),
                ),
                splitline_opts=opts.SplitLineOpts(
                    is_show=True, linestyle_opts=opts.LineStyleOpts(color="#ffffff1f")
                ),
            ),
            legend_opts=opts.LegendOpts(
                is_show=True,
                textstyle_opts=opts.TextStyleOpts(font_size=20, color="#1B69D4", font_family=('Berlin Sans FB'))),
        )
        .render("..//html//lineTest.html")
    )
    return c


if __name__ == "__main__":
    if True:
        xDataIn = ['78', 'AOA\\AOD', '开会', 'paper', '发票', 'visual-code']
        yDataIn = [42, 5, 107, 52, 79, 60]
    else:
        xDataIn = ["78", "15", "16", "17", "18", "19", "20", "21", "22", "23"]
        yDataIn = [393, 438, 485, 631, 689, 824, 987, 1000, 1100, 1200]
    DrawLine(xDataIn, yDataIn)
