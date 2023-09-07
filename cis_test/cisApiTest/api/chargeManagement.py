"""
description: 封装收费管理接口
time: 2021/12/05
author: chenling
"""
from utils.request_common import request_common
import api_config

_t = str(api_config._t)


class chargeManagement:

    # 获取接诊列表
    def chargeManagementPage(self, moudle_name, case_name, request_method, url, data):

        if case_name == "待收费查询":
            url = url + _t + "&pageNum=1&pageSize=20&status=0"
        elif case_name == "已收费查询":
            url = url + _t + "&pageNum=1&pageSize=20&status=2"
        elif case_name == "欠费查询":
            url = url + _t + "&pageNum=1&pageSize=20&status=1"
        else:
            url = url + _t + "&pageNum=1&pageSize=20&status=3"

        return request_common(moudle_name, case_name, request_method, url=url, data=data)