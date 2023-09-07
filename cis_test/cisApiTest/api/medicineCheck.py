"""
description: 封装库存盘点接口
time: 2022/4/12
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

class medicineCheck:


    # 药品搜索
    def selectMedicineStock(self, moudle_name, case_name, request_method, url, data):
        url = url + str(_t)
        return request_common(moudle_name, case_name, request_method, url=url, data=data)

    # 查询药品库存
    def selDrugStock(self, moudle_name, case_name, request_method, url, data, medicineId, batchNo, supplierId):
        url = url + str(_t) + "&medicineId=" + str(medicineId) + "&batchNo=" + str(batchNo) + "&supplierId=" + str(supplierId)
        return request_common(moudle_name, case_name, request_method, url=url, data=data)

    #变更
    def medicineCheck(self, moudle_name, case_name, request_method, url, data, medicineId, batchNo, supplierId,bookPackAmount,expireDate,inboundDate,medicineName,newCostPrice,packUnit,retailPrice,specs,stockId,supplierName,totalAmount):
        url = url + str(_t)
        data["medicineCheckDetails"][0]["batchNo"] = batchNo
        data["medicineCheckDetails"][0]["bookPackAmount"] = bookPackAmount
        data["medicineCheckDetails"][0]["checkPackAmount"] = bookPackAmount
        data["medicineCheckDetails"][0]["expireDate"] = expireDate
        data["medicineCheckDetails"][0]["inboundDate"] = inboundDate
        data["medicineCheckDetails"][0]["medicineId"] = medicineId
        data["medicineCheckDetails"][0]["medicineName"] = medicineName
        data["medicineCheckDetails"][0]["newCostPrice"] = newCostPrice
        data["medicineCheckDetails"][0]["packUnit"] = packUnit
        data["medicineCheckDetails"][0]["retailPrice"] = retailPrice
        data["medicineCheckDetails"][0]["specs"] = specs
        data["medicineCheckDetails"][0]["stockId"] = stockId
        data["medicineCheckDetails"][0]["supplierId"] = supplierId
        data["medicineCheckDetails"][0]["supplierName"] = supplierName
        data["medicineCheckDetails"][0]["totalAmount"] = totalAmount
        return request_common(moudle_name, case_name, request_method, url=url, data=data)

    # 查询总成本盈亏
    def costTotal(self, moudle_name, case_name, request_method, url, data):
        url = url + str(_t) + "&checkerId=&stateFlag=&beginTime="
        return request_common(moudle_name, case_name, request_method, url=url, data=data)

    # 获取盘点列表
    def medicineCheckList(self, moudle_name, case_name, request_method, url, data):
        url = url + str(_t) + "&pageNum=1&pageSize=10&checkerId=&stateFlag=&beginTime=&endTime="
        return request_common(moudle_name, case_name, request_method, url=url, data=data)

    # 查看盘点详情
    def medicineCheckDetails(self, moudle_name, case_name, request_method, url, data, id):
        url = url + str(_t) + "&id=" + str(id)
        return request_common(moudle_name, case_name, request_method, url=url, data=data)

    # 删除暂存盘点
    def medicineCheckDelete(self, moudle_name, case_name, request_method, url, data, id):
        url = url + str(id)
        return request_common(moudle_name, case_name, request_method, url=url, data=data)