"""
description: 封装随访管理接口
time: 2022/05/12
author: chenling
"""
from utils.request_common import request_common
import api_config

_t = str(api_config._t)


class patienfollowup:

    # 待随访列表
    def patienfollowupPage(self, moudle_name, case_name, request_method, url, data):
        if case_name == "新增随访后查询":
            url = url + _t + "&pageNum=1&pageSize=10&status=0&beginTime=&endTime=&nameOrPhone=接口测试"
        elif case_name == "已随访列表":
            url = url + _t + "&pageNum=1&pageSize=10&status=1&beginTime=&endTime=&nameOrPhone=接口测试"
        else:
            url = url + _t + "&pageNum=1&pageSize=10&status=0&beginTime=&endTime="

        return request_common(moudle_name, case_name, request_method, url=url, data=data)

    # 获取患者ID
    def visitOrderPage(self, moudle_name, case_name, request_method, url, data):
        url = url + _t + "&pageNum=1&pageSize=5&nameOrPhone=" + "接口测试"
        return request_common(moudle_name, case_name, request_method, url=url, data=data)

    # 新增随访
    def patienfollowup(self, moudle_name, case_name, request_method, url, data, patientId, doctorId):
        url = url + _t
        data[0]["patientId"] = patientId
        data[0]["followDate"] = api_config.visitTime
        data[0]["doctorId"] = doctorId
        return request_common(moudle_name, case_name, request_method, url=url, data=data)

    # 根据id查询
    def patienfollowupId(self, moudle_name, case_name, request_method, url, data, id):
        url = url + str(id)
        return request_common(moudle_name, case_name, request_method, url=url, data=data)

    # 修改随访
    def patienfollowupUpdate(self, moudle_name, case_name, request_method, url, data, id, clinicId, clinicVip, doctorId, patientId, followDate, name, phone, birthday, age):
        data["age"] = [age]
        data["id"] = id
        data["clinicId"] = clinicId
        data["clinicVip"] = clinicVip
        data["doctorId"] = doctorId
        data["patientId"] = patientId
        data["followDate"] = followDate
        data["name"] = name
        data["phone"] = phone
        data["birthday"] = birthday
        return request_common(moudle_name, case_name, request_method, url=url, data=data)

    # 删除随访
    def patienfollowupDelete(self, moudle_name, case_name, request_method, url, data, id):
        url = url + str(id)
        return request_common(moudle_name, case_name, request_method, url=url, data=data)

    # 查看已随访详情
    def patienfollowupDetail(self, moudle_name, case_name, request_method, url, data, id2):
        url = url + str(id2) + "?_t=" + _t
        return request_common(moudle_name, case_name, request_method, url=url, data=data)

