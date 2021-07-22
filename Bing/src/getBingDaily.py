# -*- coding:utf-8 -*-
"""
    功能(类)：
        获取bing每日壁纸，保存到指定文件夹
    类定义:
        class getBing():
    类参数:
        self,固有参数
        option_get,函数选项。1,获取当日focus on;2,获取最近几天focus on.
        tar_pic_folder,图像文件保存路径，默认.//bings

"""
import requests
from selenium import webdriver
# import os
from os import path
# import Beautifulsoap
from bs4 import BeautifulSoup


class getBing():
    def __init__(self, option_get=1, tar_pic_folder=".//bings"):
        super().__init__()
        self.driver_path = r"D:\Code\HouseMonitor\src\DataMining\Glowing\chromedriver.exe"
        self.tar_pic_folder = tar_pic_folder
        img_direct_urls = []
        warning_1 = r"web driver check "
        if path.isfile(self.driver_path):
            print(warning_1+"succeed")
        else:
            print(warning_1+"failed")
        if option_get == 1:
            img_direct_urls = self.__getBingWallPaperToday()
        elif option_get == 2:
            img_direct_urls = self.__getBingWallPaperRecent()
        else:
            pass
        degu = 1

    # 以双下划线"__"开始的函数为私有函数
    # 获取最近五天壁纸

    def __getBingWallPaperRecent(self):
        img_urls = []
        return img_urls

    # 获取当天壁纸
    def __getBingWallPaperToday(self):
        img_urls = list()
        html = requests.get(url="https://cn.bing.com/?mkt=zh-CN")
        bs_html = BeautifulSoup(html, 'html.parser')
        img_url = bs_html.find(name='div', attrs={"id": "bgImgProgLoad"})
        img_urls[0] = img_url
        return img_urls

    # 保存图片
    def __saveImages(self):
        pass


def return_func(x):
    print("return some thing to somebody")
    y = x+1
    return y


if __name__ == "__main__":
    gb = getBing(tar_pic_folder=r"D:\Code\HouseMonitor\Bing\src\bings")
    # b = return_func(1)
    # debug_line = 1
