# -*- coding:utf-8 -*-
# 后处理文件
import os
import re


def MergeRepeat():
    OriginLines = list()
    ModifiedLines = list()
    DictLines = dict()
    TextPath = r"D:\Code\HouseMonitor\src\DataMining\Glowing\text"
    with open(os.path.join(TextPath, 'love1.txt'), 'r', encoding="utf-8") as f:
        OriginLines = f.readlines()

    if len(OriginLines) == 0:
        print("origin file is null")
        return

    for k in OriginLines:
        k1 = k.replace("\n", "")
        k2 = k1.split(sep="|")
        dict_keys = list(DictLines.keys())
        if len(k2) == 3:
            if k2[0] in dict_keys:
                # 👍 👎
                PreUpDown = (DictLines[k2[0]])
                UpPre = int(PreUpDown[0].replace('👍', ''))
                DownPre = int(PreUpDown[1].replace('👎', ''))
                UpNew = int(k2[1].replace('👍', ''))
                DownNew = int(k2[-1].replace('👎', ''))
                DictLines[k2[0]] = ('👍'+str(UpPre+UpNew),
                                    '👎'+str(DownPre+DownNew))
            else:
                DictLines[k2[0]] = (k2[1], k2[-1])

    if len(DictLines) > 0:
        OutLines = list()
        for i_key, i_value in DictLines.items():
            LineTemp = i_key+"|"+str(i_value[0])+"|"+str(i_value[1])+"\n"
            OutLines.append(LineTemp)

        # write out
        with open(os.path.join(TextPath, 'love1-new.txt'), 'w', encoding="utf-8") as f:
            f.writelines(OutLines)
    print("lii")


def MergeRepeat_1():
    OriginLines = list()
    ModifiedLines = list()
    DictLines = dict()
    TextPath = r"D:\Code\HouseMonitor\src\DataMining\Glowing\text"
    with open(os.path.join(TextPath, 'chp1.txt'), 'r', encoding="utf-8") as f:
        OriginLines = f.readlines()

    if len(OriginLines) == 0:
        print("origin file is null")
        return

    for k in OriginLines:
        if not k in ModifiedLines:
            ModifiedLines.append(k)

    with open(os.path.join(TextPath, 'chp-new.txt'), 'w', encoding="utf-8") as f:
        f.writelines(ModifiedLines)


if __name__ == "__main__":
    MergeRepeat()
