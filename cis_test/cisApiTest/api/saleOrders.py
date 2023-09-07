# -*- coding: utf-8 -*-
# @Time    : 2022/3/10 9:52
# @Author  : PengJiong
# @Email   : 18390050274@qq.com
# @File    : saleOrders.py.py

## 封装快速接诊接口
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

class saleOrders:
    # 获取用户信息
    def getInfo(self, moudle_name, case_name, request_method, url, data):
        url = url + str(_t)
        return request_common(moudle_name, case_name, request_method, url=url, data=data)

    # 药品零售菜单
    def pendingOrderList(self, moudle_name, case_name, request_method, url, data):
        url = url + str(_t)
        return request_common(moudle_name, case_name, request_method, url=url, data=data)

    # 药品搜索
    def selectMedicineStock(self, moudle_name, case_name, request_method, url, data):
        url = url + str(_t)
        return request_common(moudle_name, case_name, request_method, url=url, data=data)

    # 下单收费
    def speedPlaceAnOrder(self, moudle_name, case_name, request_method, url, data, retailPrice, medicineId,
                          batchNo, total, packUnit, medicineName, specs, stock, clinicId,
                          namePinyin,manufacturerPinyin, packAmount, stockId, newPrice, expireDate, supplierId):
        data["visitOrder"]["totalMoney"] = retailPrice
        data["drugSubstratStockDtos"][0]["medicineId"] = medicineId
        data["drugSubstratStockDtos"][0]["batchNo"] = batchNo
        data["drugSubstratStockDtos"][0]["unit"] = packUnit
        data["saleDrugsOrderDetails"][0]["salePrice"] = retailPrice
        data["saleDrugsOrderDetails"][0]["total"] = total
        data["saleDrugsOrderDetails"][0]["batchNo"] = batchNo
        data["saleDrugsOrderDetails"][0]["packUnit"] = packUnit
        data["saleDrugsOrderDetails"][0]["medicineName"] = medicineName
        data["saleDrugsOrderDetails"][0]["specs"] = specs
        data["saleDrugsOrderDetails"][0]["retailPrice"] = retailPrice
        data["saleDrugsOrderDetails"][0]["stock"] = stock
        data["saleDrugsOrderDetails"][0]["id"] = medicineId
        data["saleDrugsOrderDetails"][0]["clinicId"] = clinicId
        data["saleDrugsOrderDetails"][0]["namePinyin"] = namePinyin
        data["saleDrugsOrderDetails"][0]["manufacturerPinyin"] = manufacturerPinyin
        data["saleDrugsOrderDetails"][0]["packAmount"] = packAmount
        data["saleDrugsOrderDetails"][0]["stockId"] = stockId
        data["saleDrugsOrderDetails"][0]["newPrice"] = newPrice
        data["saleDrugsOrderDetails"][0]["medicineId"] = medicineId
        data["saleDrugsOrderDetails"][0]["expireDate"] = expireDate
        data["saleDrugsOrderDetails"][0]["supplierId"] = supplierId
        url = url + str(_t)
        return request_common(moudle_name, case_name, request_method, url=url, data=data)

    # 检查药物处方
    def checkedPrescriptionsDrug(self, moudle_name, case_name, request_method, url, data, visitOrderId, orderType):
        data["visitOrderId"] = visitOrderId
        data["orderType"] = orderType
        url = url + str(_t)
        return request_common(moudle_name, case_name, request_method, url=url, data=data)

    # 确定支付
    def charge(self, moudle_name, case_name, request_method, url, data, visitOrderId, retailPrice):
        if case_name == "欠费":
            data["visitOrder"]["id"] = visitOrderId
            data["chargeRecord"]["cash"] = retailPrice
            data["chargeRecord"]["receivableMoney"] = retailPrice
            data["chargeRecord"]["arrearsMoney"] = retailPrice
        else:
            data["visitOrder"]["id"] = visitOrderId
            data["chargeRecord"]["cash"] = retailPrice
            data["chargeRecord"]["receivableMoney"] = retailPrice
            data["chargeRecord"]["receivedMoney"] = retailPrice
        url = url + str(_t)
        return request_common(moudle_name, case_name, request_method, url=url, data=data)

    # 零售记录菜单
    def saleOrders1(self, moudle_name, case_name, request_method, url, data):
        url = url + str(_t) + "&pageNum=1&pageSize=1"
        return request_common(moudle_name, case_name, request_method, url=url, data=data)

    # 订单退款核实
    def orderRefundVerify(self, moudle_name, case_name, request_method, url, data, visitOrderId):
        url = url + str(visitOrderId) + "?_t=" + _t
        return request_common(moudle_name, case_name, request_method, url=url, data=data)

    # 订单退款
    def orderRefund(self, moudle_name, case_name, request_method, url, data, visitOrderId, retailPrice):
        data["visitOrder"]["id"] = visitOrderId
        data["refundFee"]["cash"] = retailPrice
        url = url + str(_t)
        return request_common(moudle_name, case_name, request_method, url=url, data=data)

