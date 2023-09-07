"""
description: 积分管理接口
time: 2022/06/14
author: chenling
"""
import time
from utils.request_common import request_common
import datetime as DT
import api_config

# 转换成13位时间戳
endTime = DT.date.today()
beginTime = endTime - DT.timedelta(days=10)
t = time.time()
_t = int(t)


# 格式化成2022-09-13 11:45:39形式
visitTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

class Integral:

    # 我的积分
    def myIntegral(self, moudle_name, case_name, request_method, url, data):
        url = url + str(_t)
        return request_common(moudle_name, case_name, request_method, url=url, data=data)

    # 积分详情
    def integralPage(self, moudle_name, case_name, request_method, url, data):
        url = url + str(_t) + "&pageNum=1&pageSize=10&beginTime=" + str(api_config.week_ago) + "&endTime=" + str(api_config.today)
        return request_common(moudle_name, case_name, request_method, url=url, data=data)

    # 领劵中心
    def center(self, moudle_name, case_name, request_method, url, data):
        url = url + str(_t) + "&current=1&size=4&useFlag=0"
        return request_common(moudle_name, case_name, request_method, url=url, data=data)

    # 我的优惠券
    def couponpage(self, moudle_name, case_name, request_method, url, data):
        url = url + str(_t) + "&current=1&size=4&useFlag=0"
        return request_common(moudle_name, case_name, request_method, url=url, data=data)

    # 礼品中心
    def tGiftStock (self, moudle_name, case_name, request_method, url, data):
        url = url + str(_t) + "&pageNum=1&pageSize=6&clinicId=39461"
        return request_common(moudle_name, case_name, request_method, url=url, data=data)
