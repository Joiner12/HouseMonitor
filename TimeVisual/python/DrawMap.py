# -*- coding:utf-8 -*-
from pyecharts import options as opts
from pyecharts.charts import Geo
from pyecharts.globals import ChartType, SymbolType
import pandas as pd


def DrawMap():
    # load data from excle
    FlightArrialFile = "FlightArrial.xlsx"
    FlightDepartureFile = "FlightDeparture.xlsx"
    ArrialInfo = pd.read_excel(FlightArrialFile)
    DepartureInfo = pd.read_excel(FlightDepartureFile)
    FromCd = DepartureInfo['目的地'].to_list()
    ToCd = ArrialInfo['始发地'].to_list()
    FromCdD = dict()
    ToCdD = dict()
    for k in FromCd:
        if k in FromCdD.keys():
            FromCdD[k] += 1
        else:
            FromCdD[k] = 1

    for j in ToCd:
        if j in ToCdD.keys():
            ToCdD[j] += 1
        else:
            ToCdD[j] = 1
    geoData1 = list()
    geoData2 = list()
    geoData3 = list()
    for k1, k2 in zip(FromCdD.keys(), FromCdD.values()):
        geoData1.append((k1, k2))
        geoData2.append(("成都", k1))

    for k1, k2 in zip(ToCdD.keys(), ToCdD.values()):
        geoData3.append((k1, "成都"))
    geoAd = geoData2.extend(geoData3)
    c = (Geo(init_opts=opts.InitOpts(page_title="Map-CDC")).add_schema(
        maptype="china").add(
            "",
            geoData1,
            type_=ChartType.EFFECT_SCATTER,
            color="white",
    ).add(
            "geo",
            geoAd,
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
