# -*- coding: utf-8 -*-
# @Time    : 2022/9/15 10:12
# @Author  : PengJiong
# @Email   : 18390050274@qq.com
# @File    : wallhaven.py
import requests
import time
from lxml import etree

headers = {
    # 参数UA，用以模拟浏览器向服务器发送请求
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)Chrome/94.0.4606.61 Safari/537.36 Edg/94.0.992.31',
    # 参数cookie，用以登录图片网站，可获取NSFW类型的图片
    # 'cookie': '(填入自己的cookie地址)',
}


# 可使用代理ip，防止自身ip被封
# proxy = {'https': 'https://101.200.185.203:16818'}

def get_urls(__page__):
    # 初始化一个空列表，用以存储壁纸的图像链接
    src_urls = []
    # 根据页码不同，定制不同的URL
    base_url = 'https://wallhaven.cc/toplist'
    if page == 1:
        list_url = base_url
    else:
        # 根据不同的页面选择添加不同的连接符
        list_url = base_url + "?page=" + str(page)

    # 获取壁纸集URL的请求对象
    list_request = requests.get(url=list_url, headers=headers)
    # 根据xpath语法，获取单个壁纸的URL的列表
    list_tree = etree.HTML(list_request.text)
    list_urls = list_tree.xpath('//a[@class="preview"]/@href')

    # 循环该壁纸列表
    for img_url in list_urls:
        # 获取当前壁纸的图像链接的请求对象
        img_request = requests.get(url=img_url, headers=headers)
        # 根据xpath语法，获取当前壁纸的图像链接，并添加至src_list中
        img_tree = etree.HTML(img_request.text)
        j = img_tree.xpath('//img[@id="wallpaper"]/@src')[0]
        src_urls.append(j)
    return src_urls


def save_img(__url__):
    # 获取传入的参数url的请求对象
    request = requests.get(url=url, headers=headers)
    # 由于图像链接中包含图像名称的信息，可将图像名称分离出来
    name = str(url)[-20:]
    # 存储于本地wallhaven文件夹中
    with open('./wallhaven/' + name, "wb") as fp:
        fp.write(request.content)
    fp.close()


if __name__ == '__main__':
    # 获取起始页码与结束页码
    start_page = int(input('Please input the starting page:'))
    end_page = int(input('Please input the ending page:'))

    print('Start the download...')
    for page in range(start_page, end_page + 1):
        # 获取单个壁纸的图像链接
        for url in get_urls(page):
            print(url)
            # 将该壁纸存储本地
            save_img(url)
            # 每存储一张图片，休眠10秒
            # time.sleep(10)
        # 每存储一页图片，休眠15秒
        # time.sleep(15)
    print('The download has completed.')

