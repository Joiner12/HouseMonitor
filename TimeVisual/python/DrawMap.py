# -*- coding:utf-8 -*-
from pyecharts import options as opts
from pyecharts.charts import Geo
from pyecharts.globals import ChartType, SymbolType


def DrawMap():
    c = (
        Geo(init_opts=opts.InitOpts(page_title="Map-CDC"))
        .add_schema(maptype="成都")
        .add(
            "",
            [("青羊区", 55), ("成华区", 66), ("温江区", 77), ("武侯区", 88)],
            type_=ChartType.EFFECT_SCATTER,
            color="white",
        )
        .add(
            "geo",
            [("青羊区", "成华区"), ("青羊区", "温江区"), ("青羊区", "武侯区"), ("成华区", "温江区")],
            type_=ChartType.LINES,
            effect_opts=opts.EffectOpts(
                symbol=SymbolType.ARROW, symbol_size=2, color="blue"
            ),
            linestyle_opts=opts.LineStyleOpts(curve=0.2),
        )
        .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
        .set_global_opts(title_opts=opts.TitleOpts(title="CDC"))
        .render("..//html//geoTest.html")
    )
    return c


if __name__ == "__main__":
    DrawMap()
