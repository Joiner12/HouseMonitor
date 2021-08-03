# -*- coding:utf-8 -*-
import jieba
from DrawWordCloud import DrawWordCloud

key_dict = dict()
lyric_back = ["天空灰得像哭过",
              "离开你以后",
              "并没有更自由",
              "酸酸的空气",
              "嗅出我们的距离",
              "一幕锥心的结局",
              "像呼吸般无法停息",
              "抽屉泛黄的日记",
              "榨干了回忆",
              "那笑容是夏季",
              "你我的过去",
              "被顺时针地忘记",
              "缺氧过后的爱情",
              "粗心的眼泪是多余",
              "我知道你我都没有错",
              "只是忘了怎么退后",
              "信誓旦旦给了承诺",
              "却被时间扑了空",
              "我知道我们都没有错",
              "只是放手会比较好过",
              "最美的爱情",
              "回忆里待续",
              "天空灰得像哭过",
              "离开你以后",
              "并没有更自由",
              "酸酸的空气",
              "嗅出我们的距离",
              "一幕锥心的结局",
              "像呼吸般无法停息",
              "抽屉泛黄的日记",
              "榨干了回忆",
              "那笑容是夏季",
              "你我的过去",
              "被顺时针地忘记",
              "缺氧过后的爱情",
              "粗心的眼泪是多余",
              "我知道你我都没有错",
              "只是忘了怎么退后",
              "信誓旦旦给了承诺",
              "却被时间扑了空",
              "我知道我们都没有错",
              "只是放手会比较好过",
              "最美的爱情",
              "回忆里待续",
              "我知道你我都没有错",
              "只是忘了怎么退后",
              "信誓旦旦给了承诺",
              "却被时间扑了空",
              "我知道你我都没有错",
              "只是放手会比较好过",
              "最美的爱情",
              "回忆里待续"]
for k in lyric_back:
    seg_list = jieba.cut(k)
    prt_str = ""
    exclue_words = ["的","了","是","地"]
    for j in seg_list:
        if j in exclue_words:
            continue
        if j in key_dict.keys():
            key_dict[j] += 1
        else:
            key_dict[j] = 1
data_encounter = list()
for x, y in zip(key_dict.keys(), key_dict.values()):
    encounter_temp = (x, str(y))
    data_encounter.append(encounter_temp)
DrawWordCloud(data_encounter, renderfile=r"D:\Code\HouseMonitor\TimeVisual\html\退后.html")
