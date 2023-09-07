"""
description: 封装预约列表接口
time: 2021/12/10
author: chenling
"""

import time
from utils.request_common import request_common
import datetime as DT
import api_config


class patientRegister:

    # 获取用户信息
    def getInfo(self, moudle_name, case_name, request_method, url, data):
        url = url + str(api_config._t)
        return request_common(moudle_name, case_name, request_method, url=url, data=data)

    # 获取预约列表
    def patientRegisterList(self, moudle_name, case_name, request_method, url, data, doctorId):
        url = url + str(api_config._t) + "&pageNum=1&pageSize=10&beginTime=&endTime=&doctorId=" + str(doctorId)
        print("预约列表url=", url)
        return request_common(moudle_name, case_name, request_method, url=url, data=data)

    # 新增预约挂号
    def registration(self, moudle_name, case_name, request_method, url, data,  deptId, jobId, doctorId):

        data["deptId"] = deptId
        data["jobId"] = jobId
        data["doctorId"] = doctorId
        data["visitTime"] = api_config.visitTime

        url = url + str(api_config._t)
        return request_common(moudle_name, case_name, request_method, url=url, data=data)

    def cancelCheck(self,moudle_name, case_name, request_method, url, data, registerId):

        url = url + str(registerId) + "&cause="
        return request_common(moudle_name, case_name, request_method, url=url, data=data)