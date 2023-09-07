# -*- coding: utf-8 -*-
# @Time    : 2022/2/28 16:00
# @Author  : PengJiong
# @Email   : 18390050274@qq.com
# @File    : pendingOrderList.py
"""
封装药品零售
"""

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

class pendingOrderList:

    # 获取用户信息
    def getInfo(self, moudle_name, case_name, request_method, url, data):
        url = url + str(_t)
        return request_common(moudle_name, case_name, request_method, url=url, data=data)

    # #药品零售列表
    # def pendingOrderList(self, moudle_name, case_name, request_method, url, data):
    #     url = url + str(_t)
    #     return request_common(moudle_name, case_name, request_method, url=url, data=data)

    # 搜索(无）药品
    def selectMedicineStock(self, moudle_name, case_name, request_method, url, data):

        url = url + str(_t)
        return request_common(moudle_name, case_name, request_method, url=url, data=data)

    # 收费发药
    def retailPlaceAnOrder(self, moudle_name, case_name, request_method, url, data, unit, specs, retailPrice,
                     manufacturer, stock, clinicId, namePinyin, manufacturerPinyin, medicineId, medicineName):

        data["visitOrder"]["totalMoney"] = retailPrice
        data["drugSubstratStockDtos"][0]["medicineId"] = medicineId
        data["drugSubstratStockDtos"][0]["unit"] = unit
        data["drugSubstratStockDtos"][0]["salePrice"] = retailPrice
        data["drugSubstratStockDtos"][0]["packUnit"] = unit
        data["drugSubstratStockDtos"][0]["medicineName"] = medicineName
        data["drugSubstratStockDtos"][0]["specs"] = specs
        data["saleDrugsOrderDetails"][0]["retailPrice"] = retailPrice
        data["saleDrugsOrderDetails"][0]["manufacturer"] = manufacturer
        data["saleDrugsOrderDetails"][0]["stock"] = stock
        data["saleDrugsOrderDetails"][0]["id"] = medicineId
        data["saleDrugsOrderDetails"][0]["clinicId"] = clinicId
        data["saleDrugsOrderDetails"][0]["medicineId"] = medicineId

        url = url + str(_t)
        return request_common(moudle_name, case_name, request_method, url=url, data=data)

    #确定现金支付
    def checkedPrescriptionsDrug(self, moudle_name, case_name, request_method, url, data, visitOrderId, orderType):

        data["visitOrderId"] = visitOrderId
        data["orderType"] = orderType
        url = url + str(_t)
        return request_common(moudle_name, case_name, request_method, url=url, data=data)

    #确定支付
    def charge(self, moudle_name, case_name, request_method, url, data, visitOrderId, retailPrice):

        data["visitOrder"]["id"] = visitOrderId
        data["chargeRecord"]["cash"] = retailPrice
        data["chargeRecord"]["receivableMoney"] = retailPrice
        data["chargeRecord"]["receivedMoney"] = retailPrice

        if case_name == "欠费":
            data["visitOrder"]["id"] = visitOrderId
            data["chargeRecord"]["cash"] = retailPrice
            data["chargeRecord"]["receivableMoney"] = retailPrice
            data["chargeRecord"]["arrearsMoney"] = retailPrice

        url = url + str(_t)
        return request_common(moudle_name, case_name, request_method, url=url, data=data)

    #支付完成列表校验
    def pendingOrderList(self, moudle_name, case_name, request_method, url, data):
        url = url + str(_t)
        return request_common(moudle_name, case_name, request_method, url=url, data=data)