# -*- coding: utf-8 -*-
# @Time    : 2022/8/10 15:47
# @Author  : PengJiong
# @Email   : 18390050274@qq.com
# @File    : pachong4.py

import os
import re
import csv
import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook, load_workbook

url = "https://movie.douban.com/top250"

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
}
resp = requests.get(url, headers=headers)
# print(resp.text)
page_content = resp.text

#解析数据
obj = re.compile(r'<li>.*?<div class="item">.*?<span class="title">(?P<name>.*?)'
                 r'</span>.*?<p class="">.*?<br>(?P<year>.*?)&nbsp.*?<span '
                 r'class="rating_num" property="v:average">(?P<score>.*?)</span>.*?'
                 r'<span>(?P<num>.*?)人评价</span>', re.S)

#开始匹配
result = obj.finditer(page_content)

f = open("../data.csv", mode="w")
csvwriter = csv.writer(f)
for it in result:
#     print(it.group("name"))
#     print(it.group("score"))
#     print(it.group("num"))
#     print(it.group("year").strip())
    dic = it.groupdict()
    dic['year'] = dic['year'].strip()
    csvwriter.writerow(dic.values())

f.close()
print("over!")