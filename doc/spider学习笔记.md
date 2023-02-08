# Spider学习笔记

[TOC]



## 1.Scrapy一目了然

SCRAPPY(/ˈSkreɪpaɪ/)是一个应用程序框架，用于抓取网站和提取结构化数据，这些数据可用于广泛的有用应用程序，如数据挖掘、信息处理或历史存档。

## 2.安装指南

## 3.基本概念

本教程将指导您完成以下任务：

1. 创建新的Scrapy项目
2. 写一篇 [spider](https://www.osgeo.cn/scrapy/topics/spiders.html#topics-spiders) 对网站进行爬网并提取数据
3. 使用命令行导出抓取的数据
4. 将spider改为递归跟踪链接
5. 使用蜘蛛参数

#### 3.1 创建项目

在开始抓取之前，你必须建立一个新的零碎项目。输入要在其中存储代码并运行的目录：

```shell
scrapy startproject project_name
```

这将创建一个 `tutorial` 目录包含以下内容：

```
tutorial/
    scrapy.cfg            # deploy configuration file

    tutorial/             # project's Python module, you'll import your code from here
        __init__.py

        items.py          # project items definition file

        middlewares.py    # project middlewares file

        pipelines.py      # project pipelines file

        settings.py       # project settings file

        spiders/          # a directory where you'll later put your spiders
            __init__.py
```

### 1.1 terminal shell

```bash
# 生成爬虫指令
scrapy genspider itcast "itcast.cn"

```

## Reference

1. [Scrapy 2.5 documentation — Scrapy 2.5.0 documentation](https://docs.scrapy.org/en/latest/)
2. [从原理到实战，一份详实的 Scrapy 爬虫教程_菜鸟学Python的博客-CSDN博客](https://blog.csdn.net/cainiao_python/article/details/119224134)
3. [Python Scrapy中文教程，Scrapy框架快速入门！ (biancheng.net)](http://c.biancheng.net/view/2027.html)
4. [Scrapy 入门教程 | 菜鸟教程 (runoob.com)](https://www.runoob.com/w3cnote/scrapy-detail.html)

