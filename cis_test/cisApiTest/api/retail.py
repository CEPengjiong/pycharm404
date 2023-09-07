"""
description: 封装药品零售接口
time: 2022/3/10
author: chenling
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

class retail:
    # 获取用户信息
    def getInfo(self, moudle_name, case_name, request_method, url, data):
        url = url + str(_t)
        return request_common(moudle_name, case_name, request_method, url=url, data=data)

    # 药品搜索
    def selectMedicineStock(self, moudle_name, case_name, request_method, url, data):
        url = url + str(_t)
        return request_common(moudle_name, case_name, request_method, url=url, data=data)

    # 零售下单
    def retailPlaceAnOrder(self, moudle_name, case_name, request_method, url, data, batchNo, total, packUnit, specs, retailPrice, manufacturer, stock, clinicId, namePinyin, manufacturerPinyin, packAmount, stockId, newPrice, medicineId, expireDate, supplierId, medicineName):

        data["visitOrder"]["totalMoney"] = retailPrice
        data["drugSubstratStockDtos"][0]["medicineId"] = medicineId
        data["drugSubstratStockDtos"][0]["unit"] = packUnit
        data["drugSubstratStockDtos"][0]["batchNo"] = batchNo

        data["saleDrugsOrderDetails"][0]["salePrice"] = retailPrice
        data["saleDrugsOrderDetails"][0]["total"] = total
        data["saleDrugsOrderDetails"][0]["batchNo"] = batchNo
        data["saleDrugsOrderDetails"][0]["packUnit"] = packUnit
        data["saleDrugsOrderDetails"][0]["medicineName"] = medicineName
        data["saleDrugsOrderDetails"][0]["retailPrice"] = retailPrice
        data["saleDrugsOrderDetails"][0]["specs"] = specs
        data["saleDrugsOrderDetails"][0]["manufacturer"] = manufacturer
        data["saleDrugsOrderDetails"][0]["stock"] = stock
        data["saleDrugsOrderDetails"][0]["id"] = medicineId
        data["saleDrugsOrderDetails"][0]["clinicId"] = clinicId
        data["saleDrugsOrderDetails"][0]["namePinyin"] = namePinyin
        data["saleDrugsOrderDetails"][0]["manufacturerPinyin"] = manufacturerPinyin
        data["saleDrugsOrderDetails"][0]["packAmount"] = packAmount
        data["saleDrugsOrderDetails"][0]["stockId"] = stockId
        data["saleDrugsOrderDetails"][0]["medicineId"] = medicineId
        data["saleDrugsOrderDetails"][0]["expireDate"] = expireDate
        data["saleDrugsOrderDetails"][0]["supplierId"] = supplierId
        data["saleDrugsOrderDetails"][0]["newPrice"] = newPrice

        url = url + str(_t)
        return request_common(moudle_name, case_name, request_method, url=url, data=data)

    # 校验是否处方药
    def checkedPrescriptionsDrug(self, moudle_name, case_name, request_method, url, data, visitOrderId, orderType):

        data["visitOrderId"] = visitOrderId
        data["orderType"] = orderType
        url = url + str(_t)
        return request_common(moudle_name, case_name, request_method, url=url, data=data)

    # 收费
    def charge(self, moudle_name, case_name, request_method, url, data, visitOrderId, retailPrice):

        if case_name == "欠费":
            data["visitOrder"]["id"] = visitOrderId
            # data["chargeRecord"]["cash"] = retailPrice
            data["chargeRecord"]["receivableMoney"] = retailPrice
            data["chargeRecord"]["arrearsMoney"] = retailPrice
        else:
            data["visitOrder"]["id"] = visitOrderId
            data["chargeRecord"]["cash"] = retailPrice
            data["chargeRecord"]["receivableMoney"] = retailPrice
            data["chargeRecord"]["receivedMoney"] = retailPrice
        url = url + str(_t)
        return request_common(moudle_name, case_name, request_method, url=url, data=data)

    # 挂单
    def entryOrders(self, moudle_name, case_name, request_method, url, data, batchNo, total, packUnit, medicineName, specs, retailPrice, manufacturer, stock, id, clinicId, namePinyin,
                    manufacturerPinyin, packAmount, stockId, newPrice, medicineId, expireDate, supplierId):
        data["saleDrugsOrderDetails"][0]["salePrice"] = retailPrice
        data["saleDrugsOrderDetails"][0]["batchNo"] = batchNo
        data["saleDrugsOrderDetails"][0]["total"] = total
        data["saleDrugsOrderDetails"][0]["packUnit"] = packUnit
        data["saleDrugsOrderDetails"][0]["medicineName"] = medicineName
        data["saleDrugsOrderDetails"][0]["specs"] = specs
        data["saleDrugsOrderDetails"][0]["retailPrice"] = retailPrice
        data["saleDrugsOrderDetails"][0]["manufacturer"] = manufacturer
        data["saleDrugsOrderDetails"][0]["stock"] = stock
        data["saleDrugsOrderDetails"][0]["id"] = id
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

    # 挂单列表
    def pendingOrderList(self, moudle_name, case_name, request_method, url, data):
        url = url + str(_t)
        return request_common(moudle_name, case_name, request_method, url=url, data=data)

    #挂单详情
    def pendingOrderDetails(self, moudle_name, case_name, request_method, url, data, saleOrderId):
        url = url + str(saleOrderId) + "?_t=" + str(_t)
        return request_common(moudle_name, case_name, request_method, url=url, data=data)

    # 挂单后下单
    def retailPlaceAnOrder2(self, moudle_name, case_name, request_method, url, data, batchNo, total, packUnit, specs, retailPrice, manufacturer, stock, clinicId, namePinyin, manufacturerPinyin, packAmount, stockId, newPrice, medicineId, expireDate, supplierId, medicineName, saleDetailId):

        data["visitOrder"]["totalMoney"] = retailPrice
        data["drugSubstratStockDtos"][0]["medicineId"] = medicineId
        data["drugSubstratStockDtos"][0]["unit"] = packUnit
        data["drugSubstratStockDtos"][0]["batchNo"] = batchNo

        data["saleDrugsOrderDetails"][0]["clinicId"] = clinicId
        data["saleDrugsOrderDetails"][0]["supplierId"] = supplierId
        data["saleDrugsOrderDetails"][0]["packUnit"] = packUnit
        data["saleDrugsOrderDetails"][0]["newPrice"] = newPrice
        data["saleDrugsOrderDetails"][0]["manufacturer"] = manufacturer
        data["saleDrugsOrderDetails"][0]["specs"] = specs
        data["saleDrugsOrderDetails"][0]["total"] = total
        data["saleDrugsOrderDetails"][0]["expireDate"] = expireDate
        data["saleDrugsOrderDetails"][0]["id"] = medicineId
        data["saleDrugsOrderDetails"][0]["stock"] = stock
        data["saleDrugsOrderDetails"][0]["batchNo"] = batchNo
        data["saleDrugsOrderDetails"][0]["saleDetailId"] = saleDetailId
        data["saleDrugsOrderDetails"][0]["salePrice"] = retailPrice
        data["saleDrugsOrderDetails"][0]["medicineId"] = medicineId
        data["saleDrugsOrderDetails"][0]["namePinyin"] = namePinyin
        data["saleDrugsOrderDetails"][0]["medicineName"] = medicineName
        data["saleDrugsOrderDetails"][0]["retailPrice"] = retailPrice
        data["saleDrugsOrderDetails"][0]["manufacturerPinyin"] = manufacturerPinyin
        data["saleDrugsOrderDetails"][0]["packAmount"] = packAmount
        data["saleDrugsOrderDetails"][0]["stockId"] = stockId

        url = url + str(_t)
        return request_common(moudle_name, case_name, request_method, url=url, data=data)

    # 零售退费
    def orderRefund(self, moudle_name, case_name, request_method, url, data, visitOrderId, retailPrice):
        data["visitOrder"]["id"] = visitOrderId
        data["refundFee"]["cash"] = retailPrice
        url = url + str(_t)
        return request_common(moudle_name, case_name, request_method, url=url, data=data)

    # 删除挂单
    def deleteSaleOrder(self, moudle_name, case_name, request_method, url, data, saleOrderId):
        url = url + str(saleOrderId)
        return request_common(moudle_name, case_name, request_method, url=url, data=data)

    # 挂单收费
    def charge2(self, moudle_name, case_name, request_method, url, data, visitOrderId, retailPrice, saleOrderId):

        data["visitOrder"]["id"] = visitOrderId
        data["chargeRecord"]["cash"] = retailPrice
        data["chargeRecord"]["receivableMoney"] = retailPrice
        data["chargeRecord"]["receivedMoney"] = retailPrice
        data["saleOrderId"] = saleOrderId
        url = url + str(_t)
        return request_common(moudle_name, case_name, request_method, url=url, data=data)

    # 零售纪录查询
    def saleOrders(self, moudle_name, case_name, request_method, url, data):

        url = url + str(_t) + "&pageNum=1&pageSize=10&beginTime=" + str(api_config.today) + "&endTime=" + str(api_config.today)
        return request_common(moudle_name, case_name, request_method, url=url, data=data)