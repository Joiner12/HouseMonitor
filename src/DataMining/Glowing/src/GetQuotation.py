# -*- coding:utf-8 -*-
"""
    获取彩虹屁语录
    cheat man https://lovelive.tools/
    chp https://chp.shadiao.app/
"""
import requests
from selenium import webdriver
# from pyquery import PyQuery
import time
from random import random
import os


class Quotation():
    def __init__(self):
        self.Urls = ["https://lovelive.tools/", "https://chp.shadiao.app/"]
        self.words_love = list()
        self.words_chp = list()
        self.ExecutablePath = r"D:\Codes\HouseMonitor\src\DataMining\Glowing\chromedriver.exe"
        self.TextPath = r"D:\Codes\HouseMonitor\src\DataMining\Glowing\text"

    # https://lovelive.tools/

    def getQuotation_love(self):
        words_cnt_love = 0
        LoopCnt_love = 0
        browser_1 = webdriver.Chrome(executable_path=self.ExecutablePath)
        browser_1.set_window_size(480, 800)
        browser_1.implicitly_wait(30)  # 隐性等待，最长等5秒
        browser_1.get(self.Urls[0])
        while True:
            LoopCnt_love += 1
            if True:
                piece_btn = browser_1.find_element_by_css_selector(
                    '.ant-btn-primary')
            else:
                piece_btn = browser_1.find_elements_by_link_text("再来一条")
            piece_btn.click()
            # quotation
            if False:  # x_path
                showText = browser_1.find_element_by_xpath(
                    '//*[@id="root"]/div/div[2]/div/div/div/div/div/div[1]/div[2]'
                )
            else:  # css_selector
                showText = browser_1.find_element_by_css_selector(
                    '.contentBox___1_WSy .showText___2saEi ')
            # comment
            showComment_up = browser_1.find_element_by_xpath(
                '//*[@id="root"]/div/div[2]/div/div/div/div/div/div[2]/div[1]/div/button[1]/span'
            )

            showComment_down = browser_1.find_element_by_xpath(
                '//*[@id="root"]/div/div[2]/div/div/div/div/div/div[2]/div[1]/div/button[2]/span'
            )
            cur_words = showText.text + "|" + showComment_up.text + \
                "|"+showComment_down.text+"\n"
            # cur_words = cur_words.encode("gbk", "ignore").decode("gbk")
            # 重复检测
            with open(os.path.join(self.TextPath, "love0.txt"),
                      'r',
                      encoding='utf-8') as f:
                self.words_love = f.readlines()
            if not cur_words in self.words_love:
                print(words_cnt_love, cur_words)
                self.words_love.append(cur_words)
                with open(os.path.join(self.TextPath, "love0.txt"),
                          'w',
                          encoding='utf-8') as f:
                    f.writelines(self.words_love)
                words_cnt_love += 1

            # 写文件
            if LoopCnt_love % 10 == 0:
                time.sleep(4 + random())
            time.sleep(2 + random())

    """
        https://chp.shadiao.app/
    """

    def getQuotation_chp(self):
        LoopCnt_chp = 0
        words_cnt_chp = 0
        browser_2 = webdriver.Chrome(executable_path=self.ExecutablePath)
        browser_2.set_window_size(480, 800)
        browser_2.implicitly_wait(30)  # 隐性等待，最长等30秒
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

            # 重复检测
            with open(os.path.join(self.TextPath, "chp0.txt"),
                      'r',
                      encoding='utf-8') as f:
                self.words_chp = f.readlines()
            if not cur_words in self.words_chp:
                self.words_chp.append(cur_words)
                print(words_cnt_chp, cur_words)
                words_cnt_chp += 1
                with open(os.path.join(self.TextPath, "chp0.txt"),
                          'w',
                          encoding='utf-8') as f:
                    f.writelines(self.words_chp)
            LoopCnt_chp += 1
            # 写文件
            if LoopCnt_chp % 10 == 0:
                time.sleep(4 + random())
            time.sleep(2 + random())
        # browser_2.quit()


def testFcn():
    FilePath = os.path.dirname(os.path.abspath(__file__))
    dege = 1


if __name__ == "__main__":
    tQ = Quotation()
    if False:
        tQ.getQuotation_love()
    else:
        tQ.getQuotation_chp()
