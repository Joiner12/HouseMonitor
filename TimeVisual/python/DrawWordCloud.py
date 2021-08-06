from pyecharts import options as opts
from pyecharts.charts import WordCloud
from os import path
from pyecharts.globals import SymbolType
from datetime import datetime
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


def DrawWordCloud(words, renderfile, backgroundpic=""):
    c = WordCloud(init_opts=opts.InitOpts(
        page_title="word cloud "+datetime.now().strftime('%Y-%m-%d'),
        theme="shine"))
    if not path.isfile(backgroundpic):
        c.add("",
              words,
              word_size_range=[20, 80],
              # 将图片放在指定位置，然后读取
              # mask_image=backgroundpic,
              shape="circle")
    else:
        c.add("",
              words,
              word_size_range=[20, 80],
              # 将图片放在指定位置，然后读取
              # mask_image=backgroundpic,
              shape="circle")

    c.render(renderfile)
    print("缺氧过后的爱情\n")
    return c


if __name__ == "__main__":
    #
    data = [("幺鸡", "12"), ("垮", "50"), ("🀍", "7"), ("LOL", "20"),
            ("🔞", "3"), ("pubg", "15"), ("🤣", "21"), ("杠", "18"),
            ("🈹", "12"), ("⚅", "7"), ("🤏", "23"), ("蹦子", "18"),
            ("下棋", "15")]
    pic = "..//pic//zan.png"
    DrawWordCloud(
        data,
        renderfile="..//html//wordcloud_custom_mask_image.html",
        backgroundpic="")
