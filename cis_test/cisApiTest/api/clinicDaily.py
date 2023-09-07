"""
description: 封装今日日报接口
time: 2022/06/10
author: chenling
"""
from utils.request_common import request_common
import api_config

_t = str(api_config._t)


class clinicDaily:

    # 今日日报菜单接口
    def clinicDaily(self, moudle_name, case_name, request_method, url, data):

        url = url + _t + "&createTime=" + str(api_config.today)

        return request_common(moudle_name, case_name, request_method, url=url, data=data)


