"""
description: 封装首页接口
time: 2022/3/11
author: chenling
"""

from utils.request_common import request_common
import datetime as DT
import api_config


class homePage:

    def homePage(self, moudle_name, case_name, request_method, url, data):

        if case_name == "今日数据播报":
            url = url + str(api_config._t) + "&createTime=" + str(api_config.today)
        elif case_name == "预约挂号二维码":
            url = url + str(api_config._t) + "&isIntegral=0"
        elif case_name == "库存分析列表":
            url =url + str(api_config._t) + "&pageNum=1&pageSize=5"
        elif case_name == "近效期预警统计列表":
            url = url + str(api_config._t) + "&pageNum=1&pageSize=5"
        elif case_name == "诊所资源":
            url = url + str(api_config._t) + "&pageNum=1&pageSize=4&isIntegral=0"
        elif case_name == "会员注册二维码":
            url = url + str(api_config._t) + "3&isIntegral=2"
        elif case_name == "同安易购活动":
            url = url + str(api_config._t) + "&pageNum=1&pageSize=100"
        else:
            url = url + str(api_config._t)

        return request_common(moudle_name, case_name, request_method, url=url, data=data)