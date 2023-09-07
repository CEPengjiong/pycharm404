"""
description: 封装门诊日志接口
time: 2022/06/13
author: chenling
"""
from utils.request_common import request_common
import api_config

_t = str(api_config._t)


class clinicLog:

    # 门诊日志菜单
    def clinicLog(self, moudle_name, case_name, request_method, url, data):

        url = url + _t + "&pageNum=1&pageSize=10&beginTime=&endTime="

        return request_common(moudle_name, case_name, request_method, url=url, data=data)
