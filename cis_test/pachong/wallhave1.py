# -*- coding: utf-8 -*-
# @Time    : 2022/9/15 19:23
# @Author  : PengJiong
# @Email   : 18390050274@qq.com
# @File    : wallhave1.py

import requests
import parsel

# 随便打开一张wallhaven壁纸，观察链接规律，开头都是一样的，比如：https://w.wallhaven.cc/full/1k/wallhaven-1k6ljv.jpg；保留这个开头
# 要注意不同图片链接区别有三处，长度六位的id（比如'1k6ljv'），id前两位作为中间的一个成分（比如'1k'），末尾的后缀有jpg与png两种，后续主要围绕这些进行更改
head = 'https://w.wallhaven.cc/full/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36 Edg/103.0.1264.77'}
# 这里检索第一页和第二页的图片，即 page=1 & page=2
for i in range(1, 3):
    url = f'https://wallhaven.cc/toplist?page={i}'
    response = requests.get(url=url, headers=headers)
    response.encoding = response.apparent_encoding
    selector = parsel.Selector(response.text)
    # 查找所有div并返回字符串
    divs = selector.css('div[class="thumb-info"]').getall()
    print(divs)
    # 以下两个列表分别保留图片id与后缀
    srcs = list()
    spans = list()
    png = 'png'
    for div in divs:
        # 提取id
        src = div.split('tags/')[1]
        src = src.split('"><i class')[0]
        srcs.append(src)
        # 若文件为png即设置为1，jpg为0
        if png in div:
            spans.append(1)
        else:
            spans.append(0)
    # 遍历当前page所有图片
    for i in range(len(srcs)):
        my_src = srcs[i]
        my_span = spans[i]
        # 缝合链接
        tail = my_src + '.jpg'
        if my_span == 1:
            tail = tail.replace('jpg', 'png')
        img_url = head + tail[0:2] + '/wallhaven-' + tail
        print(img_url)
        img_content = requests.get(url=img_url).content
        # 保存二进制图片，定义保存路径
        with open('D:\Backup\Documents\My Videos\图片' + tail, mode='wb') as f:
            f.write(img_content)
print('done')
