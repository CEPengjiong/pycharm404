# -*- coding: utf-8 -*-
# @Time    : 2022/4/2 16:32
# @Author  : PengJiong
# @Email   : 18390050274@qq.com
# @File    : pachong1.py
#
# from urllib.request import urlopen
#
# url = "http://www.baidu.com"
# re = urlopen(url)
#
# print(re.read())

import urllib.request
import os
import re



def douban(url):
    r = urllib.request.urlopen(url)
    html = r.read().decode('utf-8')
    result = re.feindall(r'https://img\d.doubanio.com/img/celebrity/medium/.*.jpg', html)
    result2 = re.findall(r'(?<=title=").\S+', html)
    result2.pop()
    result3 = sorted(set(result2), key=result2.index)
    result3.pop(-3)
    if not os.path.exists('douban'):
        os.makedirs('douban')
    i = 0
    for link in result:
        filename = 'douban\\' + str(result3[i]) + '.jpg'
        i += 1
        with open(filename, 'w') as file:
            urllib.request.urlretrieve(link, filename)

url = 'https://movie.douban.com/subject/26260853/celebrities'
if __name__=='__main__':
    douban(url)