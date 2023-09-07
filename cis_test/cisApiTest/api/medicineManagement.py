"""
description: 封装药房管理-药品管理接口
time: 2022/3/14
author: chenling
"""
import time
from utils.request_common import request_common
import datetime as DT
import api_config

class medicineManagement:


    # 药品查询
    def medicineManagement(self, moudle_name, case_name, request_method, url, data):
        if case_name == "中心药品库搜索药品":
            url = url + str(api_config._t) + "&name=牛黄解毒丸&type=1&drugType=0"
        elif case_name == "根据药品名称查询":
            url = url + str(api_config._t) + "&pageNum=1&pageSize=10&drugName=接口测试"
        elif case_name == "云药房查询":
            url = url + str(api_config._t) + "&pageNum=1&pageSize=10&drugType=0&drugName=野"
        else:
            url = url + str(api_config._t) + "&pageNum=1&pageSize=10"
        return request_common(moudle_name, case_name, request_method, url=url, data=data)


    # 新增药品
    def getMedicineInfo(self, moudle_name, case_name, request_method, url, data, medicineId):
        url = url + str(medicineId) + "?_t=" + str(api_config._t)
        return request_common(moudle_name, case_name, request_method, url=url, data=data)

    # 编辑药品
    def medicineInfo(self, moudle_name, case_name, request_method, url, data, medicineId, clinicId, createBy, createTime, effectiveTime):

        data["id"] = medicineId
        data["clinicId"] = clinicId
        data["createBy"] = createBy
        data["createTime"] = createTime
        data["effectiveTime"] = effectiveTime

        return request_common(moudle_name, case_name, request_method, url=url, data=data)

    # 删除药品
    def medicineDelete(self, moudle_name, case_name, request_method, url, data, medicineId):

        url = url + str(medicineId)
        return request_common(moudle_name, case_name, request_method, url=url, data=data)

    # 云药房导入
    def saveBatch(self, moudle_name, case_name, request_method, url, data, approvalNumber, barCode, code2, formulation, insuranceCode, manufacturer, medicareFlag, medicineMinimumNumber, medicineMinimumUnit, medicinePreparationUnit, name, packUnit, province, specs, retailPrice):
        url = url + str(api_config._t)
        data[0]["approvalNumber"] = approvalNumber
        data[0]["barCode"] = barCode
        data[0]["code"] = code2
        data[0]["formulation"] = formulation
        data[0]["insuranceCode"] = insuranceCode
        data[0]["manufacturer"] = manufacturer
        data[0]["medicareFlag"] = medicareFlag
        data[0]["medicineMinimumNumber"] = medicineMinimumNumber
        data[0]["medicineMinimumUnit"] = medicineMinimumUnit
        data[0]["medicinePreparationUnit"] = medicinePreparationUnit
        data[0]["name"] = name
        data[0]["packUnit"] = packUnit
        data[0]["province"] = province
        data[0]["specs"] = specs
        data[0]["retailPrice"] = retailPrice
        return request_common(moudle_name, case_name, request_method, url=url, data=data)

    # 云药房-根据药品名称查询
    def drugNameQuery(self, moudle_name, case_name, request_method, url, data, name):

        url = url + str(api_config._t) + "&pageNum=1&pageSize=10&drugName=" + name
        return request_common(moudle_name, case_name, request_method, url=url, data=data)

    # 药品拆零
    def updateZero(self, moudle_name, case_name, request_method, url, data, medicineId):

        data["id"] = medicineId
        return request_common(moudle_name, case_name, request_method, url=url, data=data)