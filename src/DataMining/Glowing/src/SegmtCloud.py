# -*- coding:utf-8 -*-
# 对所有数据进行分词并且绘制图云
import jieba
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import os
import nltk
import re

rootPath = r"D:\Code\HouseMonitor\src\DataMining\Glowing"


class SegCloud():
    def __init__(self, SrcFile=os.path.join(rootPath, "\text\allinone.txt")):
        super().__init__()
        self.SrcFile = SrcFile

    def GenCloud(self):
        d = os.path.dirname(__file__)

        # 词频统计
        text = list()
        text_1 = list()
        with open(self.SrcFile, 'r', encoding="utf-8") as f:
            text = f.readlines()
        for k in text:
            regexp = re.compile(r'\n|,|，|。|.')
            temp = re.sub('\n|,|，|。', '', k)
            text_1.append(temp)

        textCut = list()
        for j in text_1:
            tempCut = jieba.cut(j, cut_all=True)
            for i in tempCut:
                exceptWords = ['', '的', ' ']
                if not i in exceptWords:
                    textCut.append(i)
        textCutFre = nltk.FreqDist(textCut)  # list
        textCutFre = textCutFre.most_common(80)

        # list → dict
        textCutFreDict = {}
        for k in textCutFre:
            textCutFreDict[k[0]] = k[-1]

        # 词云
        font = 'C:/Windows/Fonts/simhei.ttf'
        alice_mask = np.array(Image.open(
            os.path.join(rootPath, "img\rainbow.jpg")))
        wc = WordCloud(font_path=font, background_color=None, max_words=2000,
                       contour_width=3, contour_color='steelblue', mode='RGBA',
                       mask=alice_mask)

        wc.generate_from_frequencies(textCutFreDict)
        plt.imshow(wc, interpolation='bilinear')
        plt.axis("off")

        plt.show()
        plt.imshow(alice_mask, cmap=plt.cm.gray, interpolation='bilinear')
        debugline = 1


def test():
    a = "世事不堪。但你不一样，你永远温柔，永远是那个月亮"
    Acut = jieba.cut(a, cut_all=False)
    temp = list()
    for k in Acut:
        temp.append(k)
    temp = nltk.FreqDist(temp)
    print(temp)


if __name__ == "__main__":
    a = SegCloud()
    a.GenCloud()
    # test()
