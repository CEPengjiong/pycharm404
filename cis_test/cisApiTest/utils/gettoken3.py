# -*- coding: utf-8 -*-
# @Time    : 2022/10/31 10:39
# @Author  : PengJiong
# @Email   : 18390050274@qq.com
# @File    : gettoken3.py
import urllib.request
import requests
import os
import re

url = "https://g1cis.tyzsls.com/prod-api/clinic/medicine/info/selectMedicineStock?_t=1640677463"
url1 = "https://g1cis.tyzsls.com/prod-api/clinic/tclinicbase/testToken?phone="

file = open('b.txt','w')
with open('phone.txt') as phone:
    for ph in phone:
        content = ph
        rq = urllib.request.urlopen(url1+content).read()
        # token = re.findall('"access_token":"(.*?)"',rq)
        # res = rq.content.decode('utf-8')
        str2 = str(rq, encoding="utf-8")
        token = re.findall('"access_token":"(.*?)"', str2)
        print(token)
        token.append('\n')
        file.writelines(token)
