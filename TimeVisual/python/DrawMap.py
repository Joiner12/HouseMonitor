# -*- coding:utf-8 -*-
from pyecharts import options as opts
from pyecharts.charts import Geo
from pyecharts.globals import ChartType, SymbolType


def DrawMap():
    c = (Geo(init_opts=opts.InitOpts(page_title="Map-CDC")).add_schema(
        maptype="china").add(
            "",
            [("北京", 55), ("上海", 66), ("长沙", 77), ("武汉", 88)],
            type_=ChartType.EFFECT_SCATTER,
            color="white",
        ).add(
            "geo",
            [("成都", "上海"), ("成都", "拉萨"), ("成都", "武汉"), ("上海", "拉萨")],
            type_=ChartType.LINES,
            effect_opts=opts.EffectOpts(symbol=SymbolType.ARROW,
                                        symbol_size=2,
                                        color="blue"),
            linestyle_opts=opts.LineStyleOpts(curve=0.2),
        ).set_series_opts(label_opts=opts.LabelOpts(
            is_show=False)).set_global_opts(title_opts=opts.TitleOpts(
                title="CDC")).render("..//html//geoTest.html"))
    return c


if __name__ == "__main__":
    DrawMap()
