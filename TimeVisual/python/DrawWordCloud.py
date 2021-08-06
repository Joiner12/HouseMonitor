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
    if False:
        data = [("幺鸡", "12"), ("垮", "50"), ("🀍", "7"), ("LOL", "20"),
                ("🔞", "3"), ("pubg", "15"), ("🤣", "21"), ("杠", "18"),
                ("🈹", "12"), ("⚅", "7"), ("🤏", "23"), ("蹦子", "18"),
                ("下棋", "15")]
        pic = "..//pic//zan.png"
        DrawWordCloud(
            data,
            renderfile="..//html//wordcloud_custom_mask_image.html",
            backgroundpic="")
    else:
        import jieba
        cutOut = list()
        with open("allinone.txt", 'r', encoding="utf-8") as f:
            OriginLines = f.readlines()
        for k in OriginLines:
            seg_list = jieba.cut_for_search(k)  # 搜索引擎模式
            excludWords = [',', '?', '。', '，', '？', '（',
                           '(', ')', '）', '~', '!', '《', '》', '...', '~', '..', '；', '你', '我', '的']
            for j in seg_list:
                if not j in excludWords:
                    cutOut.append(j)
        wordsDict = dict()
        for k in cutOut:
            if k in wordsDict.keys():
                wordsDict[k] += 1
            else:
                wordsDict[k] = 1
        wordsOut = list()
        cnt = 0
        for kk, vk in zip(wordsDict.keys(), wordsDict.values()):
            cnt += 1
            if cnt == 1:
                wordsOut.append(('爽', vk))
            elif cnt == 2:
                wordsOut.append(('子', vk))
            elif cnt == 3:
                wordsOut.append(('哥', vk))
            else:
                cnt = 0
        wordsOut.append(("垮", "3000"))
        DrawWordCloud(
            wordsOut,
            renderfile="..//html//wordcloud_custom_mask_image.html",
            backgroundpic="..//pic//zan.png")
