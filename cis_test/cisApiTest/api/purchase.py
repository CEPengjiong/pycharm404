"""
description: 封装采购入库接口
time: 2022/4/12
author: chenling
"""
import time
from utils.request_common import request_common
import datetime as DT
import api_config
import logging
import requests
import os
import sys

# 转换成13位时间戳
endTime = DT.date.today()
beginTime = endTime - DT.timedelta(days=10)
t = time.time()
_t = int(t)

# 格式化成2021-09-13 11:45:39形式
visitTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())


curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
# excel导入模块存放地址
template = rootPath + r"\data\牛黄解毒丸.xls"
files = {'file': ("牛黄解毒丸.xls", open(template, 'rb'), 'application/vnd.ms-excel', {'Expires': '0'})}

class purchase:

    # 采购入库-excel上传
    def excelImport(self, moudle_name, case_name, request_method, url, data):
        host_url = api_config.get_env()
        url = host_url + url + str(api_config._t)
        logging.info("模块：{}    用例名称：{}\n请求方式：{}\n请求地址的url：{}；\n请求的body:{}".format(moudle_name, case_name, request_method, url, data))
        return requests.post(url=url, headers=api_config.excelImportHeader, files=files, verify=False)

    # 查询供应商列表
    def supplierList(self, moudle_name, case_name, request_method, url, data):
        url = url + str(_t)
        return request_common(moudle_name, case_name, request_method, url=url, data=data)

    # 查询库存药品
    def medicineStockByPurchase(self, moudle_name, case_name, request_method, url, data):
        url = url + str(_t)
        return request_common(moudle_name, case_name, request_method, url=url, data=data)

    # 新增入库
    def newPurchase(self, moudle_name, case_name, request_method, url, data, supplierId, newMedicine, unitUnanimous, purchaseUnit, purchaseUnitPrice, purchaseAmount, retailUnit, batchNo,
                    expireTime, medicineName, specs, manufacturer, type, retailPrice):
        url = url + str(_t)
        data["supplierId"] = supplierId

        data["detailList"][0]["amount"] = purchaseAmount
        data["detailList"][0]["batchNo"] = batchNo
        data["detailList"][0]["costPrice"] = retailPrice
        data["detailList"][0]["expireTime"] = expireTime
        data["detailList"][0]["newMedicine"] = newMedicine
        data["detailList"][0]["predictAmount"] = purchaseAmount
        data["detailList"][0]["retailUnit"] = retailUnit
        data["detailList"][0]["unit"] = purchaseUnit
        data["detailList"][0]["unitPrice"] = purchaseUnitPrice
        data["detailList"][0]["unitUnanimous"] = unitUnanimous
        data["detailList"][0]["purchaseDetailVo"]["manufacturer"] = manufacturer
        data["detailList"][0]["purchaseDetailVo"]["medicineName"] = medicineName
        data["detailList"][0]["purchaseDetailVo"]["purchaseUnit"] = purchaseUnit
        data["detailList"][0]["purchaseDetailVo"]["retailPrice"] = retailPrice
        data["detailList"][0]["purchaseDetailVo"]["specs"] = specs
        data["detailList"][0]["purchaseDetailVo"]["type"] = type

        totalMoney = purchaseAmount * int(purchaseUnitPrice)
        data["medicinePurchase"]["invoiceTime"] = visitTime
        data["medicinePurchase"]["totalMoney"] = totalMoney

        return request_common(moudle_name, case_name, request_method, url=url, data=data)

    # 查询入库列表
    def purchaseList(self, moudle_name, case_name, request_method, url, data):
        url = url + str(_t) + "&pageNum=1&pageSize=10&state=&beginTime=&endTime="
        return request_common(moudle_name, case_name, request_method, url=url, data=data)

    # 查看入库记录
    def queryInfo(self, moudle_name, case_name, request_method, url, data, id):
        url = url + str(id) + "?_t=" + str(_t)
        return request_common(moudle_name, case_name, request_method, url=url, data=data)

    # 退货
    def tmedicinepurchasereturns(self, moudle_name, case_name, request_method, url, data, id, supplierId, supplierName, createTime,
                                 name, amount, returnableAmount, id2, medicineId, unitPrice, batchNo2, expireTime2, unit, retailPrice2, purchaseUnit2, purchaseAmount2, specs2, manufacturer2, medicineName2):
        data["medicinePurchaseId"] = id

        data["medicinePurchaseReturnsDetails"][0]["amount"] = amount
        data["medicinePurchaseReturnsDetails"][0]["batchNo"] = batchNo2
        data["medicinePurchaseReturnsDetails"][0]["expireTime"] = expireTime2
        data["medicinePurchaseReturnsDetails"][0]["id"] = id2
        data["medicinePurchaseReturnsDetails"][0]["manufacturer"] = manufacturer2
        data["medicinePurchaseReturnsDetails"][0]["medicineId"] = medicineId
        data["medicinePurchaseReturnsDetails"][0]["medicineName"] = medicineName2
        data["medicinePurchaseReturnsDetails"][0]["purchaseAmount"] = purchaseAmount2
        data["medicinePurchaseReturnsDetails"][0]["purchaseUnit"] = purchaseUnit2
        data["medicinePurchaseReturnsDetails"][0]["purchaseUnitPrice"] = unitPrice
        data["medicinePurchaseReturnsDetails"][0]["retailPrice"] = retailPrice2
        data["medicinePurchaseReturnsDetails"][0]["returnableAmount"] = returnableAmount
        data["medicinePurchaseReturnsDetails"][0]["specs"] = specs2
        data["medicinePurchaseReturnsDetails"][0]["unit"] = unit

        data["medicinePurchaseReturnsDetails"][0]["unitPrice"] = unitPrice * 10

        data["medicinePurchaseReturns"]["createTime"] = createTime
        data["medicinePurchaseReturns"]["name"] = name
        data["medicinePurchaseReturns"]["supplierId"] = supplierId
        data["medicinePurchaseReturns"]["supplierName"] = supplierName
        data["medicinePurchaseReturns"]["retTotalMoeny"] = unitPrice * 10

        url = url + str(_t)
        return request_common(moudle_name, case_name, request_method, url=url, data=data)


    # 暂存
    def temporaryStorage(self, moudle_name, case_name, request_method, url, data, supplierId, purchaseUnit, purchaseUnitPrice, retailUnit, batchNo,
                    expireTime, medicineName, specs, manufacturer, type, retailPrice, medicineId):
        url = url + str(_t)
        data["supplierId"] = supplierId

        data["detailList"][0]["amount"] = 10
        data["detailList"][0]["unit"] = purchaseUnit
        data["detailList"][0]["retailUnit"] = retailUnit
        data["detailList"][0]["batchNo"] = batchNo
        data["detailList"][0]["costPrice"] = retailPrice
        data["detailList"][0]["expireTime"] = expireTime
        data["detailList"][0]["medicineId"] =medicineId
        data["detailList"][0]["unitPrice"] = purchaseUnitPrice

        data["detailList"][0]["purchaseDetailVo"]["medicineName"] = medicineName
        data["detailList"][0]["purchaseDetailVo"]["manufacturer"] = manufacturer
        data["detailList"][0]["purchaseDetailVo"]["purchaseUnit"] = purchaseUnit
        data["detailList"][0]["purchaseDetailVo"]["retailPrice"] = retailPrice
        data["detailList"][0]["purchaseDetailVo"]["specs"] = specs
        data["detailList"][0]["purchaseDetailVo"]["type"] = type

        totalMoney = 10 * int(purchaseUnitPrice)
        data["medicinePurchase"]["invoiceTime"] = visitTime
        data["medicinePurchase"]["totalMoney"] = totalMoney

        return request_common(moudle_name, case_name, request_method, url=url, data=data)

    # 暂存入库单详情
    def selPurchaseDetail(self, moudle_name, case_name, request_method, url, data, id):

        url =url + str(id) + "?_t=" + str(api_config._t)
        return request_common(moudle_name, case_name, request_method, url=url, data=data)

    # 暂存-入库
    def newPurchaseTS(self, moudle_name, case_name, request_method, url, data, id, billNo, totalMoney, supplierId, clinicId, createBy, createTime, invoiceTime, id2, medicinePurchaseId,
                      medicineId, amount, retailQuantity, returnableAmount, unitPrice, batchNo, expireTime, unitId, costPrice, medicineName, specs, manufacturer, retailPrice, type, supplierName, unit):

        data["supplierId"] = supplierId
        data["purchaseTime"] = visitTime
        data["supplierName"] = supplierName

        data["medicinePurchase"]["id"] = id
        data["medicinePurchase"]["billNo"] = billNo
        data["medicinePurchase"]["totalMoney"] = totalMoney
        data["medicinePurchase"]["supplierId"] = supplierId
        data["medicinePurchase"]["clinicId"] = clinicId
        data["medicinePurchase"]["createBy"] = createBy
        data["medicinePurchase"]["createTime"] = createTime
        data["medicinePurchase"]["invoiceTime"] = invoiceTime

        data["detailList"][0]["id"] = id2
        data["detailList"][0]["medicinePurchaseId"] = medicinePurchaseId
        data["detailList"][0]["medicineId"] = medicineId
        data["detailList"][0]["amount"] = amount
        data["detailList"][0]["retailQuantity"] = retailQuantity
        data["detailList"][0]["returnableAmount"] = returnableAmount
        data["detailList"][0]["unitPrice"] = unitPrice
        data["detailList"][0]["batchNo"] = batchNo
        data["detailList"][0]["expireTime"] = expireTime
        data["detailList"][0]["createBy"] = createBy
        data["detailList"][0]["createTime"] = createTime
        data["detailList"][0]["unit"] = unit
        data["detailList"][0]["unitId"] = unitId
        data["detailList"][0]["retailUnit"] = unit
        data["detailList"][0]["costPrice"] = costPrice
        data["detailList"][0]["purchaseDetailVo"]["medicineName"] = medicineName
        data["detailList"][0]["purchaseDetailVo"]["specs"] = specs
        data["detailList"][0]["purchaseDetailVo"]["manufacturer"] = manufacturer
        data["detailList"][0]["purchaseDetailVo"]["retailPrice"] = retailPrice
        data["detailList"][0]["purchaseDetailVo"]["type"] = type

        url =url + str(api_config._t)
        return request_common(moudle_name, case_name, request_method, url=url, data=data)


    # 暂存入库删除
    def purchaseDelete(self, moudle_name, case_name, request_method, url, data, id):

        url =url + str(id)
        return request_common(moudle_name, case_name, request_method, url=url, data=data)

    # 云药房入库列表
    def centerPurchaseList(self, moudle_name, case_name, request_method, url, data):
        url = url + str(api_config._t) + "&drugType=0&name=牛黄解毒丸"
        return request_common(moudle_name, case_name, request_method, url=url, data=data)
    # 中心药品库采购入库
    def centerNewPurchase(self,moudle_name, case_name, request_method, url, data, supplierId, retailUnit,  medicineName, specs, manufacturer, barCode, type, approvalNumber,retailPrice, purchaseUnit, medicareFlag, centerMedicineCode):
        url = url + str(api_config._t)
        data["supplierId"] =supplierId
        data["purchaseTime"] = visitTime
        data["detailList"][0]["retailUnit"] = retailUnit
        data["detailList"][0]["unit"] = retailUnit
        data["detailList"][0]["purchaseDetailVo"]["medicineName"] = medicineName
        data["detailList"][0]["purchaseDetailVo"]["specs"] = specs
        data["detailList"][0]["purchaseDetailVo"]["manufacturer"] = manufacturer
        data["detailList"][0]["purchaseDetailVo"]["barCode"] = barCode
        data["detailList"][0]["purchaseDetailVo"]["type"] = type
        data["detailList"][0]["purchaseDetailVo"]["approvalNumber"] = approvalNumber
        data["detailList"][0]["purchaseDetailVo"]["retailPrice"] = retailPrice
        data["detailList"][0]["purchaseDetailVo"]["purchaseUnit"] = purchaseUnit
        data["detailList"][0]["purchaseDetailVo"]["medicareFlag"] = medicareFlag
        data["detailList"][0]["purchaseDetailVo"]["centerMedicineCode"] = centerMedicineCode
        data["medicinePurchase"]["invoiceTime"] = visitTime
        return request_common(moudle_name, case_name, request_method, url=url, data=data)