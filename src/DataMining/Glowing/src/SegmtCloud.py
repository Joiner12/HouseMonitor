# -*- coding:utf-8 -*-
# 对所有数据进行分词并且绘制图云
import jieba
from wordcloud import WordCloud, ImageColorGenerator
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import os
import nltk
import re
from scipy.ndimage import gaussian_gradient_magnitude
# rootPath = r"D:\Code\HouseMonitor\src\DataMining\Glowing"
rootPath = r"D:\Codes\HouseMonitor\src\DataMining\Glowing"


class SegCloud():
    def __init__(self, SrcFile=os.path.join(rootPath, r"text\allinone.txt")):
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
        textCutFre = textCutFre.most_common(50)

        # list → dict
        textCutFreDict = {}
        for k in textCutFre:
            textCutFreDict[k[0]] = k[-1]

        # 词云
        font = 'C:/Windows/Fonts/simhei.ttf'
        figureColor = np.array(
            Image.open(os.path.join(rootPath, r"img\cover3.png")))
        # figureColor = figureColor[::3, ::3]
        markColor = figureColor.copy()
        markColor[markColor.sum(axis=2) == 0] = 255

        # 图片边缘区分
        edges = np.mean([
            gaussian_gradient_magnitude(markColor[:, :, i] / 255., 2)
            for i in range(3)
        ],
                        axis=0)
        markColor[edges > 0.08] = 255
        wc = WordCloud(font_path=font,
                       background_color="white",
                       mask=markColor,
                       max_font_size=40,
                       random_state=42,
                       relative_scaling=0)
        wc.generate_from_frequencies(textCutFreDict)
        # color_mark
        plt.imshow(wc)
        bimgColor = ImageColorGenerator(figureColor)
        plt.figure(figsize=(10, 10))
        plt.title("word cloud ")
        plt.imshow(wc.recolor(color_func=bimgColor), interpolation="bilinear")
        plt.axis("off")
        plt.show()

        plt.figure(figsize=(10, 10))
        plt.title("Original Image")
        plt.imshow(figureColor)

        plt.figure(figsize=(10, 10))
        plt.title("edges map")
        plt.imshow(edges)
        plt.show()


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
