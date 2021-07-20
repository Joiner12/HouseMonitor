# -*- coding:utf-8 -*-
import requests
r = requests.get(
    url="https://www.chongbuluo.com/plugin.php?id=wq_sign")
print(r.text)
