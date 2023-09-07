"""
description: 封装患者管理接口
time: 2022/05/10
author: chenling
"""
from utils.request_common import request_common
import api_config

_t = str(api_config._t)


class patientManagement:

    # 患者列表
    def visitOrderPage(self, moudle_name, case_name, request_method, url, data):

        url = url + _t + "&pageNum=1&pageSize=20&nameOrPhone=接口测试"

        return request_common(moudle_name, case_name, request_method, url=url, data=data)

    # 档案详情
    def fileDetails(self, moudle_name, case_name, request_method, url, data, patientId):

        url = url + str(patientId) + "?_t=" + _t

        return request_common(moudle_name, case_name, request_method, url=url, data=data)

    # 修改患者信息
    def patientinfo(self, moudle_name, case_name, request_method, url, data, patientId, clinicId, clinicName, createBy, createTime):
        data["patientInfo"]["patientId"] = patientId
        data["patientInfo"]["clinicId"] = clinicId
        data["patientInfo"]["clinicName"] =clinicName
        data["patientInfo"]["createBy"] = createBy
        data["patientInfo"]["createTime"] = createTime
        data["patientInfo"]["updateBy"] = createBy

        return request_common(moudle_name, case_name, request_method, url=url, data=data)

    # 门诊记录
    def outpatientRecordsPage(self, moudle_name, case_name, request_method, url, data, patientId):

         url = url + _t + "&pageNum=1&pageSize=5&patientId=" + str(patientId)
         return request_common(moudle_name, case_name, request_method, url=url, data=data)

    # 门诊记录-详情
    def outpatientRecordsDetail(self, moudle_name, case_name, request_method, url, data, medicalRecordId ,visitOrderId):
        url = url + _t + "&medicalRecordId=" + str(medicalRecordId) + "&visitOrderId=" + str(visitOrderId)
        return request_common(moudle_name, case_name, request_method, url=url, data=data)

    # 患者轨迹
    def patientTrajectoryPage(self, moudle_name, case_name, request_method, url, data, patientId):
        url = url + str(patientId) + "?_t=" + _t
        return request_common(moudle_name, case_name, request_method, url=url, data=data)

    # 零售纪录
    def saleOrders(self, moudle_name, case_name, request_method, url, data, patientId):
        url = url + _t + "&pageNum=1&pageSize=5&patientId=" + str(patientId)
        return request_common(moudle_name, case_name, request_method, url=url, data=data)

    # 零售纪录-详情
    def retailRecordDetailInfo(self, moudle_name, case_name, request_method, url, data, orderId):
        url = url + str(orderId) + "?_t=" + _t
        return request_common(moudle_name, case_name, request_method, url=url, data=data)

    # 随访记录
    def patienfollowup(self, moudle_name, case_name, request_method, url, data, patientId):
        url = url + _t + "&pageNum=1&pageSize=5&patientId=" + str(patientId)
        return request_common(moudle_name, case_name, request_method, url=url, data=data)

    # 随访记录-详情
    def patienfollowupDetail(self, moudle_name, case_name, request_method, url, data, patienfollowupId):
        url = url + str(patienfollowupId) + "?_t=" + _t
        return request_common(moudle_name, case_name, request_method, url=url, data=data)
