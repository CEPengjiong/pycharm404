# -*- coding: utf-8 -*-
# @Time    : 2022/4/15 14:57
# @Author  : PengJiong
# @Email   : 18390050274@qq.com
# @File    : HuanzheGuanli.py

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

class HuanzheGuanli:
    # 诊所信息获取
    def getinfo(self, moudle_name, case_name, request_method, url, data):
        url = url + str(_t)
        return request_common(moudle_name, case_name, request_method, url=url, data=data)

    # 病人
    def isExist(self, moudle_name, case_name, request_method, url, data):
        url = url + str(_t) + "&clinicErpCode="
        return request_common(moudle_name, case_name, request_method, url=url, data=data)

    # 访问者页面
    def visitOrderPage(self, moudle_name, case_name, request_method, url, data):
        url = url + str(_t) + "&pageNum=1&pageSize=20" + "&nameOrPhone="
        return request_common(moudle_name, case_name, request_method, url=url, data=data)

    # 用户列表
    def userlist(self, moudle_name, case_name, request_method, url, data):
        url = url + str(_t)
        return request_common(moudle_name, case_name, request_method, url=url, data=data)

    # 文件详细信息
    def fileDetails(self, moudle_name, case_name, request_method, url, data, patientId):
        url = url + str(patientId) + "?_t=" + str(_t)
        return request_common(moudle_name, case_name, request_method, url=url, data=data)

    # 门诊病例
    # def outpatientRecordsPage(self, moudle_name, case_name, request_method, url, data, patientId):
    #     url = url + str(_t) + "&pageNum=1&pageSize=5&patientId=" + str(patientId)
    #     return request_common(moudle_name, case_name, request_method, url=url, data=data)

    # 患者轨迹页面
    def patientTrajectoryPage(self, moudle_name, case_name, request_method, url, data, patientId):
        url = url + str(patientId) + "?_t=" + str(_t)
        return request_common(moudle_name, case_name , request_method, url=url, data=data)

    # 零售记录
    def saleOrders(self, moudle_name, case_name, request_method, url, data, patientId):
        url = url + str(_t) + "&pageNum=1&pageSize=5&patientId=" + str(patientId)
        return request_common(moudle_name, case_name, request_method, url=url, data=data)

    # 随访记录
    def page(self, moudle_name, case_name, request_method, url, data, patientId):
        url = url + str(_t) + "&pageNum=1&pageSize=5&patientId=" + str(patientId)
        return request_common(moudle_name, case_name, request_method, url=url, data=data)

    # 随访管理
    def patienfollowuppage(self, moudle_name, case_name, request_method, url, data):
        url = url + str(_t) + "&pageNum=1&pageSize=10&status=0&beginTime=&endTime="
        return request_common(moudle_name, case_name, request_method, url=url, data=data)

    # 新增随访
    def patienfollowup(self, moudle_name, case_name, request_method, url, data, patientId, doctorId):
        data[0]["patientId"] = patientId
        data[0]["doctorId"] = doctorId
        url = url + str(_t)
        return request_common(moudle_name, case_name, request_method, url=url, data=data)