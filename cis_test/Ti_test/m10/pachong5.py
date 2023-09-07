# -*- coding: utf-8 -*-
# @Time    : 2022/8/12 13:51
# @Author  : PengJiong
# @Email   : 18390050274@qq.com
# @File    : pachong5.py
import requests
import re

domain = "https://www.dytt89.com/"

resp = requests.get(domain, verify=False) # verify 去掉安全严重
resp.encoding = 'gb2312' # 指定字符集
# print(resp.text)

#拿到ul里面的li
obj1 = re.compile(r"2022必看热片.*?<ul>(?P<ul>.*?)</ul>", re.S)
obj2 = re.compile(r"<a href='(?P<href>.*?)'", re.S)
obj3 = re.compile(r'◎片　　名(?P<movie>.*?)<br />'r'.*?<td '
                  r'style="WORD-WRAP: break-word" bgcolor="#fdfddf"><a href="(?P<download>.*?)">', re.S)

result1 = obj1.finditer(resp.text)
child_href_list = []
for it in result1:
    ul = it.group('ul')

    # 提取子页面链接：
    result2 = obj2.finditer(ul)
    for itt in result2:
        #拼接子页面的url地址： 域名+子页面地址
        child_href = domain + itt.group('href').strip("/")
        child_href_list.append(child_href) # 把子页面链接保存起来
        print(child_href)


#提取子页面内容
for href in child_href_list:
    child_resp = requests.get(href, verify=False)
    child_resp.encoding = 'gb2312'
    # print(child_resp.text)
    result3 = obj3.search(child_resp.text)
    print(result3.group("movie"))
    print(result3.group("download"))
    # break   #测试