"""
description: 封装接诊列表接口
time: 2021/11/24
author: chenling
"""

import time
from utils.request_common import request_common
import datetime as DT
import api_config

_t = str(api_config._t)
# 格式化成2021-09-13 11:45:39形式
followDate = time.strftime("%Y-%m-%d 00:00:00", time.localtime())

class selRegisterInfoList:

    # 获取接诊列表
    def listQuery(self, moudle_name, case_name, request_method, url, data):
        url = url + _t + "&pageNum=1&pageSize=10&beginTime=&endTime="
        return request_common(moudle_name, case_name, request_method, url=url, data=data)

    def patienfollowup(self, moudle_name, case_name, request_method, url, data, patientId, doctorId):
        url = url + _t
        data[0]["patientId"] = patientId
        data[0]["doctorId"] = doctorId
        data[0]["followDate"] = followDate
        return request_common(moudle_name, case_name, request_method, url=url, data=data)

    def particulars(self, moudle_name, case_name, request_method, url, data, visitOrderId):
        url = url + str(visitOrderId) + "?_t=" + _t
        return request_common(moudle_name, case_name, request_method, url=url, data=data)