# -*- coding:utf-8 -*-
"""
    获取彩虹屁语录
    cheat man https://lovelive.tools/
    chp https://chp.shadiao.app/
"""
import requests
from selenium import webdriver
from pyquery import PyQuery
import time
import csv
import pandas as pd
from pandas import DataFrame
from random import random


class Quotation():

    def __init__(self):
        self.Urls = ["https://lovelive.tools/", "https://chp.shadiao.app/"]
        self.words_love = list()
        self.words_chp = list()

    # https://lovelive.tools/
    def getQuotation_love(self):
        repeat_cnt_1 = 0
        test_cnt = 0
        browser_1 = webdriver.Chrome(
            executable_path=r"D:\Code\HouseMonitor\src\DataMining\Glowing\chromedriver.exe")
        browser_1.set_window_size(480, 800)
        browser_1.implicitly_wait(30)  # 隐性等待，最长等10秒
        browser_1.get(self.Urls[0])
        while True:
            piece_btn = browser_1.find_element_by_css_selector(
                '.ant-btn.active')
            piece_btn.click()
            # quotation
            if False:  # x_path
                showText = browser_1.find_element_by_xpath(
                    '//*[@id="root"]/div/div[2]/div/div/div/div/div/div[1]/div[2]')
            else:  # css_selector
                showText = browser_1.find_element_by_css_selector(
                    '.contentBox___1_WSy .showText___2saEi ')
            # comment
            showComment_up = browser_1.find_element_by_xpath(
                '//*[@id="root"]/div/div[2]/div/div/div/div/div/div[2]/div[1]/div/button[1]/span')

            showComment_down = browser_1.find_element_by_xpath(
                '//*[@id="root"]/div/div[2]/div/div/div/div/div/div[2]/div[1]/div/button[2]/span')
            cur_words = showText.text + "|" + showComment_up.text + \
                "|"+showComment_down.text+"\n"
            print(cur_words)
            # cur_words = cur_words.encode("gbk", "ignore").decode("gbk")
            if repeat_cnt_1 > 1:
                break
            # 重复检测
            if not cur_words in self.words_love:
                self.words_love.append(cur_words)
                test_cnt += 1
                repeat_cnt_1 = 0
            else:
                repeat_cnt_1 += 1
        time.sleep(1+random())
        browser_1.quit()
        # write to file
        with open(r"D:\Code\HouseMonitor\src\DataMining\Glowing\text\love.txt", 'a', encoding="utf-8") as f:
            f.writelines(self.words_love)
    """
        https://chp.shadiao.app/
    """

    def getQuotation_chp(self):
        repeat_cnt_2 = 0
        LoopCnt = 0
        browser_2 = webdriver.Chrome(
            executable_path=r"D:\Code\HouseMonitor\src\DataMining\Glowing\chromedriver.exe")
        browser_2.set_window_size(480, 800)
        browser_2.implicitly_wait(30)  # 隐性等待，最长等10秒
        browser_2.get(self.Urls[1])
        while True:
            # span_random
            # piece_btn = browser_2.find_element_by_css_selector(
            #     '.mdl-button--accent.mdl-button--accent.mdl-button--raised, .mdl-button--accent.mdl-button--accent.mdl-button--fab')
            piece_btn = browser_2.find_element_by_id('span_random')
            piece_btn.click()
            # quotation
            showText = browser_2.find_element_by_css_selector(
                '.mdl-textfield__input')
            cur_words = showText.text + "\n"
            print(cur_words)
            if repeat_cnt_2 > 1:
                print("self stop")
                break
            # 重复检测
            if not cur_words in self.words_chp:
                self.words_chp.append(cur_words)
                repeat_cnt_2 = 0
            else:
                repeat_cnt_2 += 1
            LoopCnt += 1
            # 写文件
            if LoopCnt % 100 == 0:
                LoopCnt = 0
                with open(r"D:\Code\HouseMonitor\src\DataMining\Glowing\text\chp.txt", 'a', encoding='utf-8') as f:
                    f.writelines(self.words_chp)
                self.words_chp = list()
                time.sleep(2)
            time.sleep(1+random())
        browser_2.quit()


def testFcn():
    cnt = 0
    print(50 % 20)


if __name__ == "__main__":
    tQ = Quotation()
    # tQ.getQuotation_love()
    tQ.getQuotation_chp()
