# -*- coding: utf-8 -*-
# @Time    : 2022/4/28 17:41
# @Author  : PengJiong
# @Email   : 18390050274@qq.com
# @File    : vip.py

import time
from utils.request_common import request_common
import datetime as DT

import api_config


endtime = DT.date.today()
beginTime = endtime - DT.timedelta(days=10)
t = time.time()
_t = int(t)

# 格式化成2021-09-13 11:45:39形式
visitTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

class vip:
    # 会员列表
    def vippage(self, moudle_name, case_name, request_method, url, data):
        url = url + str(_t) + "&pageNum=1&pageSize=10beginTime=&endTime="
        return request_common(moudle_name, case_name, request_method, url=url, data=data)

    # 新增会员
    def vipvip(self, moudle_name, case_name, request_method, url, data, phone, name):
        url = url + str(_t)
        data["phone"] = phone
        data["name"] = name
        return request_common(moudle_name, case_name, request_method, url=url, data=data)

    # 取得新增会员Id
    def vippage(self, moudle_name, case_name, request_method, url, data):
        url = url + str(_t) + "&pageNum=1&pageSize=10beginTime=&endTime="
        return request_common(moudle_name, case_name, request_method, url=url, data=data)

    # 会员详情
    def logpage(self, moudle_name, case_name, request_method, url, data, vipId):
        url = url + str(_t) + "&pageNum=1&pageSize=10&vipId=" + str(vipId)
        return request_common(moudle_name, case_name, request_method, url=url, data=data)

    # 会员设置
    def setUpInfo(self, moudle_name, case_name, request_method, url, data):
        url = url + str(_t)
        return request_common(moudle_name, case_name, request_method, url=url, data=data)

    # # 会员设置保存
    # def setUp(self, moudle_name, case_name, request_method, url, data):
    #     return request_common(moudle_name, case_name, request_method, url=url, data=data)
