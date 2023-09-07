"""
description: 封装快速接诊接口
time: 2022/3/01
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

class speedPlaceAnOrder:
    # 获取用户信息
    def getInfo(self, moudle_name, case_name, request_method, url, data):
        url = url + str(_t)
        return request_common(moudle_name, case_name, request_method, url=url, data=data)

    # 药品搜索
    def selectMedicineStock(self, moudle_name, case_name, request_method, url, data):
        url = url + str(_t)
        return request_common(moudle_name, case_name, request_method, url=url, data=data)

    # 快速下单
    def speedPlaceAnOrder(self, moudle_name, case_name, request_method, url, data,batchNo,total, packUnit, specs, retailPrice, jobId, deptId, doctorId,
                     manufacturer, stock, clinicId, namePinyin, manufacturerPinyin, packAmount, stockId, newPrice, medicineId, expireDate, supplierId, medicineName):

        data["drugSubstratStockDtos"][0]["medicineId"] = medicineId
        data["drugSubstratStockDtos"][0]["medicineName"] = medicineName
        data["drugSubstratStockDtos"][0]["unit"] = packUnit
        data["drugSubstratStockDtos"][0]["detItemFeeSumamt"] = retailPrice
        data["drugSubstratStockDtos"][0]["batchNo"] = batchNo
        data["drugSubstratStockDtos"][0]["manufacturer"] = manufacturer
        data["drugSubstratStockDtos"][0]["cntUnit"] = packUnit
        data["drugSubstratStockDtos"][0]["salePrice"] = retailPrice
        data["drugSubstratStockDtos"][0]["pric"] = retailPrice
        data["drugSubstratStockDtos"][0]["spec"] = specs
        data["drugSubstratStockDtos"][0]["medListname"] = medicineName
        data["visitOrderSpeeds"][0]["salePrice"] = retailPrice
        data["visitOrderSpeeds"][0]["amountUnit"] = packUnit
        data["visitOrderSpeeds"][0]["total"] = total
        data["visitOrderSpeeds"][0]["batchNo"] = batchNo
        data["visitOrderSpeeds"][0]["packUnit"] = packUnit
        data["visitOrderSpeeds"][0]["medicineName"] = medicineName
        data["visitOrderSpeeds"][0]["retailPrice"] = retailPrice
        data["visitOrderSpeeds"][0]["specs"] = specs
        data["visitOrderSpeeds"][0]["manufacturer"] = manufacturer
        data["visitOrderSpeeds"][0]["stock"] = stock
        data["visitOrderSpeeds"][0]["id"] = medicineId
        data["visitOrderSpeeds"][0]["clinicId"] = clinicId
        data["visitOrderSpeeds"][0]["namePinyin"] = namePinyin
        data["visitOrderSpeeds"][0]["manufacturerPinyin"] = manufacturerPinyin
        data["visitOrderSpeeds"][0]["packAmount"] = packAmount
        data["visitOrderSpeeds"][0]["stockId"] = stockId
        data["visitOrderSpeeds"][0]["medicineId"] = medicineId
        data["visitOrderSpeeds"][0]["expireDate"] = expireDate
        data["visitOrderSpeeds"][0]["supplierId"] = supplierId
        data["visitOrderSpeeds"][0]["newPrice"] = newPrice
        data["patientRegisterVO"]["jobId"] = jobId
        data["patientRegisterVO"]["deptId"] = deptId
        data["patientRegisterVO"]["doctorId"] = doctorId
        data["patientRegisterVO"]["visitTime"] = visitTime
        data["visitOrder"]["totalMoney"] = retailPrice

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

    # 已收费-查询
    def chargeManagementInfo(self, moudle_name, case_name, request_method, url, data, visitOrderId):

        url = url + str(visitOrderId) + "?_t=" + str(_t)
        return request_common(moudle_name, case_name, request_method, url=url, data=data)

    # 代收费-校验有无结算单
    def check(self, moudle_name, case_name, request_method, url, data, visitOrderId):
        url = url + str(_t)
        data["cisOrderId"] = visitOrderId
        return request_common(moudle_name, case_name, request_method, url=url, data=data)

    # 收费管理-已收费-退费
    def orderRefund(self, moudle_name, case_name, request_method, url, data, visitOrderId, retailPrice):
        url = url + str(_t)
        data["visitOrder"]["id"] = visitOrderId
        data["refundFee"]["cash"] = retailPrice
        return request_common(moudle_name, case_name, request_method, url=url, data=data)

    # 打印处方笺
    def printPrescription(self,moudle_name, case_name, request_method, url, data, orderNo):
        url = url + str(_t) + "&orderNo=" + orderNo + "&type=0"
        return request_common(moudle_name, case_name, request_method, url=url, data=data)