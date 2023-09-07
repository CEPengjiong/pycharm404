# -*- coding: utf-8 -*-
# @Time    : 2022/9/2 11:50
# @Author  : PengJiong
# @Email   : 18390050274@qq.com
# @File    : medicinebreakage.py
import time
from utils.request_common import request_common
import datetime as DT
import api_config

# 转换成13位时间戳
endTime = DT.date.today()
beginTime = endTime - DT.timedelta(days=10)
t = time.time()
_t = int(t)


# 格式化成2021-09-13 11:45:39形式
visitTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

class medicinebreakage:

    # 损毁列表
    def medicinebreakage(self, moudle_name, case_name, request_method, url, data):
        url = url + str(_t) + "&pageNum=1&pageSize=10&total=0&beginTime=&endTime="
        return request_common(moudle_name, case_name, request_method, url=url, data=data)

    # 药品搜索
    def selectBreakageMedicineStock(self, moudle_name, case_name, request_method, url, data):
        # data["name"] = name
        # data["drugType"] = drugType
        url = url + str(_t)
        return request_common(moudle_name, case_name, request_method, url=url, data=data)

    # 选择首个药品
    def selDrugStock(self, moudle_name, case_name, request_method, url, data, medicineId):
        url = url + str(_t) + "&batchNo=&supplierId=&medicineId=" + str(medicineId)
        return request_common(moudle_name, case_name, request_method, url=url, data=data)

    # 保存报损药品信息
    def saveAndDrugStock(self, moudle_name, case_name, request_method, url, data, medicineId,
                         medicineName, manufacturer, specs, pieceNumber,
                         packUnit, newPrice):
        url = url + str(_t)
        data["medicineId"] = medicineId
        data["medicineName"] = medicineName
        data["manufacturer"] = manufacturer
        data["specs"] = specs
        data["pieceNumber"] = pieceNumber
        data["packUnit"] = packUnit
        data["newPrice"] = newPrice
        return request_common(moudle_name, case_name, request_method, url=url, data=data)

    # 损毁列表
    def medicinebreakage1(self, moudle_name, case_name, request_method, url, data):
        url = url + str(_t) + "&pageNum=1&pageSize=10&total=0&beginTime=&endTime="
        return request_common(moudle_name, case_name, request_method, url=url, data=data)

    # 撤销报损药品
    def cancelAndAddStock(self, moudle_name, case_name, request_method, url, data, medicineId,
                         medicineName, manufacturer, specs, batchNo, medicineType, pieceNumber,
                         packUnit, newPrice, medicineTypeStr, typeStr, createBy, createTime,
                          clinicId, id):
        url = url + str(_t)
        data["id"] = id
        data["medicineTypeStr"] = medicineTypeStr
        data["typeStr"] = typeStr
        data["createBy"] = createBy
        data["createTime"] = createTime
        data["clinicId"] = clinicId
        data["medicineId"] = medicineId
        data["medicineName"] = medicineName
        data["manufacturer"] = manufacturer
        data["specs"] = specs
        data["batchNo"] = batchNo
        data["medicineType"] = medicineType
        data["pieceNumber"] = pieceNumber
        data["packUnit"] = packUnit
        data["newPrice"] = newPrice


        return request_common(moudle_name, case_name, request_method, url=url, data=data)
