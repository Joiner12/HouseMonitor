import json
from pyecharts import options as opts
from pyecharts.charts import WordCloud
from os import path
from pyecharts.globals import SymbolType
""" 
    函数:
        调用pyecharts绘制词云
    定义:
        def DrawWordCloud(words, renderfile="", backgroundpic="")
    输入:
        words,词频+词语
        renderfile,渲染输出文件
        backgroundpic,背景图片
    输出:
        c,html

"""


def DrawWordCloud(words, renderfile="", backgroundpic=""):
    if not path.isfile(backgroundpic):
        c = (
            WordCloud()
            .add("",
                 words,
                 word_size_range=[80, 100],
                 # 将图片放在指定位置，然后读取
                 shape=SymbolType.ROUND_RECT)
            .set_global_opts(title_opts=opts.TitleOpts(title="WordCloud-自定义图片"))
            .render(renderfile)
        )
    else:
        c = (
            WordCloud()
            .add("",
                 words,
                 word_size_range=[60, 100],
                 # 将图片放在指定位置，然后读取
                 mask_image=backgroundpic,
                 shape=SymbolType.ROUND_RECT)
            .set_global_opts(title_opts=opts.TitleOpts(title="WordCloud-自定义图片"))
            .render(renderfile)
        )
    print("缺氧过后的爱情\n")
    return c


if __name__ == "__main__":
    #
    data = [("跨", "12"), ("垮", "50"), ("夸", "7"), ("kua", "20"),
            ("跨", "3"), ("垮", "15"), ("夸", "21"), ("kua", "18"),
            ("跨", "12"), ("垮", "31"), ("夸", "7"), ("kua", "23")]
    pic = r"D:\Code\HouseMonitor\TimeVisual\html\pic\zan.png"
    DrawWordCloud(
        data,
        renderfile=r"D:\Code\HouseMonitor\TimeVisual\html\wordcloud_custom_mask_image.html",
        backgroundpic=pic)
