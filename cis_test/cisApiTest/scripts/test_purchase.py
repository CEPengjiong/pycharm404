"""
description: 采购入库接口测试用例
time: 2022/4/12
author: chenling
"""
import json
import logging
import allure
import pytest
import os
import sys
from utils.assert_common import assert_common
from utils.ReadTabDataUtils import read_test_data
from api.api_factory import ApiFactory
import api_config

@allure.feature("药房管理模块")
class TestPurchase:
    curPath = os.path.abspath(os.path.dirname(__file__))
    rootPath = os.path.split(curPath)[0]
    sys.path.append(rootPath)
    data_path = rootPath + r"\data\purchase.xls"
    # excel导入模块存放地址
    template = rootPath + r"\data\牛黄解毒丸.xls"

    '''
    @allure.severity装饰器按严重性级别来标记case　　　
    执行指定测试用例 --allure-severities blocker
    BLOCKER = 'blocker'　　阻塞缺陷
    CRITICAL = 'critical'　严重缺陷
    NORMAL = 'normal'　　  一般缺陷
    MINOR = 'minor'　　    次要缺陷
    TRIVIAL = 'trivial'　　轻微缺陷　
    '''

    @allure.story("采购入库菜单")
    @allure.severity("BLOCKER")
    @allure.description("001-采购入库-新增入库-excel导入")
    @pytest.mark.parametrize("moudle_name,case_name,request_method,request_url,req_data,code,exc_data", read_test_data(data_path, "excel导入", None, 1, 2, 3, 4, 7, 8, 9))
    def test_purchaseExcel_case(self, moudle_name, case_name, request_method, request_url, req_data, code, exc_data,  clinic_login):

        global batchNo,expireTime,manufacturer,medicineName,newMedicine,purchaseAmount,purchaseUnit,\
            purchaseUnitPrice,retailPrice,retailUnit,specs,type,unitUnanimous,supplierId,id,supplierName,createTime,\
            name,amount,returnableAmount,id2,medicineId,unitPrice,batchNo2,expireTime2,unit,retailPrice2,purchaseUnit2,purchaseAmount2,specs2,manufacturer2,medicineName2

        if case_name == "excel导入":
            res_text = ApiFactory.get_purchase().excelImport(moudle_name=moudle_name, case_name=case_name, request_method=request_method, url=request_url, data=json.loads(req_data))
            logging.info("返回结果：{}".format(res_text.json()))
            assert_common(res_text, msg=exc_data)
            batchNo = res_text.json().get("data").get("purchaseDetailVos")[0].get("batchNo")
            expireTime = res_text.json().get("data").get("purchaseDetailVos")[0].get("expireTime")
            manufacturer = res_text.json().get("data").get("purchaseDetailVos")[0].get("manufacturer")
            medicineName = res_text.json().get("data").get("purchaseDetailVos")[0].get("medicineName")
            newMedicine = res_text.json().get("data").get("purchaseDetailVos")[0].get("newMedicine")
            purchaseAmount = res_text.json().get("data").get("purchaseDetailVos")[0].get("purchaseAmount")
            purchaseUnit = res_text.json().get("data").get("purchaseDetailVos")[0].get("purchaseUnit")
            purchaseUnitPrice = res_text.json().get("data").get("purchaseDetailVos")[0].get("purchaseUnitPrice")
            retailPrice = res_text.json().get("data").get("purchaseDetailVos")[0].get("retailPrice")
            retailUnit = res_text.json().get("data").get("purchaseDetailVos")[0].get("retailUnit")
            specs = res_text.json().get("data").get("purchaseDetailVos")[0].get("specs")
            type = res_text.json().get("data").get("purchaseDetailVos")[0].get("type")
            unitUnanimous = res_text.json().get("data").get("purchaseDetailVos")[0].get("unitUnanimous")
        elif case_name == "新增入库":
            res_text = ApiFactory.get_purchase().newPurchase(moudle_name=moudle_name, case_name=case_name, request_method=request_method, url=request_url, data=json.loads(req_data), supplierId=supplierId,
                                                             newMedicine=newMedicine, unitUnanimous=unitUnanimous, purchaseAmount=purchaseAmount, purchaseUnit=purchaseUnit, purchaseUnitPrice=purchaseUnitPrice, retailUnit=retailUnit, batchNo=batchNo, expireTime=expireTime,
                                                             medicineName=medicineName, specs=specs, manufacturer=manufacturer, type=type, retailPrice=retailPrice)
            logging.info("返回结果：{}".format(res_text.json()))
            assert_common(res_text, msg=exc_data)
        elif case_name == "查看入库列表":
            res_text = ApiFactory.get_purchase().purchaseList(moudle_name=moudle_name, case_name=case_name, request_method=request_method, url=request_url, data=json.loads(req_data))
            logging.info("返回结果：{}".format(res_text.json()))
            assert_common(res_text, msg=exc_data)
            id = res_text.json().get("data").get("records")[0].get("id")
        elif case_name == "查看入库记录":
            res_text = ApiFactory.get_purchase().queryInfo(moudle_name=moudle_name, case_name=case_name, request_method=request_method, url=request_url, data=json.loads(req_data), id=id)
            logging.info("返回结果：{}".format(res_text.json()))
            assert_common(res_text, msg=exc_data)
            supplierName = res_text.json().get("data").get("supplierName")
            createTime = res_text.json().get("data").get("createTime")
            name = res_text.json().get("data").get("name")
            amount = res_text.json().get("data").get("medicinePurchaseReturnsDetailVOS")[0].get("amount")
            returnableAmount = res_text.json().get("data").get("medicinePurchaseReturnsDetailVOS")[0].get("returnableAmount")
            id2 = res_text.json().get("data").get("medicinePurchaseReturnsDetailVOS")[0].get("id")
            medicineId = res_text.json().get("data").get("medicinePurchaseReturnsDetailVOS")[0].get("medicineId")
            medicineName2 = res_text.json().get("data").get("medicinePurchaseReturnsDetailVOS")[0].get("medicineName")
            unitPrice = res_text.json().get("data").get("medicinePurchaseReturnsDetailVOS")[0].get("unitPrice")
            batchNo2 = res_text.json().get("data").get("medicinePurchaseReturnsDetailVOS")[0].get("batchNo")
            expireTime2 = res_text.json().get("data").get("medicinePurchaseReturnsDetailVOS")[0].get("expireTime")
            unit = res_text.json().get("data").get("medicinePurchaseReturnsDetailVOS")[0].get("unit")
            retailPrice2 = res_text.json().get("data").get("medicinePurchaseReturnsDetailVOS")[0].get("retailPrice")
            purchaseUnit2 = res_text.json().get("data").get("medicinePurchaseReturnsDetailVOS")[0].get("purchaseUnit")
            purchaseAmount2 = res_text.json().get("data").get("medicinePurchaseReturnsDetailVOS")[0].get("purchaseAmount")
            specs2 = res_text.json().get("data").get("medicinePurchaseReturnsDetailVOS")[0].get("specs")
            manufacturer2 = res_text.json().get("data").get("medicinePurchaseReturnsDetailVOS")[0].get("manufacturer")
        elif case_name == "退货":
            res_text = ApiFactory.get_purchase().tmedicinepurchasereturns(moudle_name=moudle_name, case_name=case_name, request_method=request_method, url=request_url, data=json.loads(req_data), id=id, supplierName=supplierName, supplierId=supplierId, createTime=createTime, name=name, amount=amount,
                                                                          returnableAmount=returnableAmount, id2=id2, medicineId=medicineId, unitPrice=unitPrice, batchNo2=batchNo2, expireTime2=expireTime2, unit=unit, retailPrice2=retailPrice2, purchaseUnit2=purchaseUnit2,
                                                                          purchaseAmount2=purchaseAmount2, specs2=specs2, manufacturer2=manufacturer2, medicineName2=medicineName2)
            logging.info("返回结果：{}".format(res_text.json()))
            assert_common(res_text, msg=exc_data)
        elif case_name == "查看退货记录":
            res_text = ApiFactory.get_purchase().queryInfo(moudle_name=moudle_name, case_name=case_name,
                                                           request_method=request_method, url=request_url,
                                                           data=json.loads(req_data), id=id)
            logging.info("返回结果：{}".format(res_text.json()))
            assert_common(res_text, msg=exc_data)
        else:
            res_text = ApiFactory.get_purchase().supplierList(moudle_name=moudle_name, case_name=case_name, request_method=request_method, url=request_url, data=json.loads(req_data))
            logging.info("返回结果：{}".format(res_text.json()))
            assert_common(res_text, msg=exc_data)
            supplierId = res_text.json().get("data")[0].get("supplierId")



    @allure.story("采购入库菜单")
    @allure.severity("BLOCKER")
    @allure.description("002-采购入库-新增入库-系统导入-暂存-入库")
    @pytest.mark.parametrize("moudle_name,case_name,request_method,request_url,req_data,code,exc_data", read_test_data(data_path, "系统导入", None, 1, 2, 3, 4, 7, 8, 9))
    def test_purchaseSys_case(self, moudle_name, case_name, request_method, request_url, req_data, code, exc_data,  clinic_login):

        global batchNo,expireTime,manufacturer,medicineName,packUnit,newPrice,retailPrice,specs,type,supplierId,medicineId,id,\
            createBy,billNo,totalMoney,clinicId,createTime,invoiceTime,version,id2,medicinePurchaseId,amount,retailQuantity,returnableAmount,unitPrice,unitId,costPrice,supplierName,unit

        if case_name == "查询供应商":
            res_text = ApiFactory.get_purchase().supplierList(moudle_name=moudle_name, case_name=case_name, request_method=request_method, url=request_url, data=json.loads(req_data))
            logging.info("返回结果：{}".format(res_text.json()))
            assert_common(res_text, msg=exc_data)
            supplierId = res_text.json().get("data")[0].get("supplierId")
        elif case_name == "查询库存药品":
            res_text = ApiFactory.get_purchase().medicineStockByPurchase(moudle_name=moudle_name, case_name=case_name, request_method=request_method, url=request_url, data=json.loads(req_data))
            logging.info("返回结果：{}".format(res_text.json()))
            assert_common(res_text, msg=exc_data)
            batchNo = res_text.json().get("data")[0].get("batchNo")
            expireTime = res_text.json().get("data")[0].get("expireDate")
            manufacturer = res_text.json().get("data")[0].get("manufacturer")
            medicineName = res_text.json().get("data")[0].get("medicineName")
            medicineId = res_text.json().get("data")[0].get("medicineId")
            newPrice = res_text.json().get("data")[0].get("newPrice")
            packUnit = res_text.json().get("data")[0].get("packUnit")
            retailPrice = res_text.json().get("data")[0].get("retailPrice")
            specs = res_text.json().get("data")[0].get("specs")
            type = res_text.json().get("data")[0].get("type")
        elif case_name == "查看入库列表":
            res_text = ApiFactory.get_purchase().purchaseList(moudle_name=moudle_name, case_name=case_name,
                                                              request_method=request_method, url=request_url,
                                                              data=json.loads(req_data))
            logging.info("返回结果：{}".format(res_text.json()))
            assert_common(res_text, msg=exc_data)
            id = res_text.json().get("data").get("records")[0].get("id")
        elif case_name == "暂存":
            res_text = ApiFactory.get_purchase().temporaryStorage(moudle_name=moudle_name, case_name=case_name, request_method=request_method, url=request_url, data=json.loads(req_data), supplierId=supplierId,
                                                             medicineId=medicineId, purchaseUnit=packUnit, purchaseUnitPrice=newPrice, retailUnit=packUnit, batchNo=batchNo, expireTime=expireTime,
                                                             medicineName=medicineName, specs=specs, manufacturer=manufacturer, type=type, retailPrice=retailPrice)
            logging.info("返回结果：{}".format(res_text.json()))
            assert_common(res_text, msg=exc_data)
        elif case_name == "编辑":
            res_text = ApiFactory.get_purchase().selPurchaseDetail(moudle_name=moudle_name, case_name=case_name,
                                                              request_method=request_method, url=request_url,
                                                              data=json.loads(req_data), id=id)
            logging.info("返回结果：{}".format(res_text.json()))
            assert_common(res_text, msg=exc_data)
            createBy = res_text.json().get("data").get("detailList")[0].get("createBy")
            billNo = res_text.json().get("data").get("medicinePurchase").get("billNo")
            totalMoney = res_text.json().get("data").get("medicinePurchase").get("totalMoney")
            clinicId = res_text.json().get("data").get("medicinePurchase").get("clinicId")
            createTime = res_text.json().get("data").get("medicinePurchase").get("createTime")
            invoiceTime = res_text.json().get("data").get("medicinePurchase").get("invoiceTime")
            version = res_text.json().get("data").get("medicinePurchase").get("version")
            id2 = res_text.json().get("data").get("detailList")[0].get("id")
            medicinePurchaseId = res_text.json().get("data").get("detailList")[0].get("medicinePurchaseId")
            amount = res_text.json().get("data").get("detailList")[0].get("amount")
            retailQuantity = res_text.json().get("data").get("detailList")[0].get("retailQuantity")
            returnableAmount = res_text.json().get("data").get("detailList")[0].get("returnableAmount")
            unitPrice = res_text.json().get("data").get("detailList")[0].get("unitPrice")
            unit = res_text.json().get("data").get("detailList")[0].get("unit")
            unitId = res_text.json().get("data").get("detailList")[0].get("unitId")
            costPrice = res_text.json().get("data").get("detailList")[0].get("costPrice")
            supplierName = res_text.json().get("data").get("supplierName")

        elif case_name == "暂存-入库":
            res_text = ApiFactory.get_purchase().newPurchaseTS(moudle_name=moudle_name, case_name=case_name, request_method=request_method, url=request_url, data=json.loads(req_data), id=id, billNo=billNo, totalMoney=totalMoney, supplierId=supplierId,
                                                               clinicId=clinicId, createBy=createBy, createTime=createTime, invoiceTime=invoiceTime, id2=id2, medicinePurchaseId=medicinePurchaseId, medicineId=medicineId, amount=amount,
                                                               retailQuantity=retailQuantity, returnableAmount=returnableAmount, unitPrice=unitPrice, batchNo=batchNo, expireTime=expireTime, unitId=unitId, costPrice=costPrice, medicineName=medicineName,
                                                               specs=specs, manufacturer=manufacturer, retailPrice=retailPrice, type=type, supplierName=supplierName, unit=unit)

            logging.info("返回结果：{}".format(res_text.json()))
            assert_common(res_text, msg=exc_data)


    @allure.story("采购入库菜单")
    @allure.severity("BLOCKER")
    @allure.description("003-采购入库-新增入库-系统导入-暂存-删除")
    @pytest.mark.parametrize("moudle_name,case_name,request_method,request_url,req_data,code,exc_data", read_test_data(data_path, "删除暂存", None, 1, 2, 3, 4, 7, 8, 9))
    def test_purchaseDelete_case(self, moudle_name, case_name, request_method, request_url, req_data, code, exc_data,  clinic_login):

        global batchNo,expireTime,manufacturer,medicineName,packUnit,newPrice,retailPrice,specs,type,supplierId,medicineId,id,\
            createBy,billNo,totalMoney,clinicId,createTime,invoiceTime,version,id2,medicinePurchaseId,amount,retailQuantity,returnableAmount,unitPrice,unitId,costPrice,supplierName,unit

        if case_name == "查询供应商":
            res_text = ApiFactory.get_purchase().supplierList(moudle_name=moudle_name, case_name=case_name, request_method=request_method, url=request_url, data=json.loads(req_data))
            logging.info("返回结果：{}".format(res_text.json()))
            assert_common(res_text, msg=exc_data)
            supplierId = res_text.json().get("data")[0].get("supplierId")
        elif case_name == "查询库存药品":
            res_text = ApiFactory.get_purchase().medicineStockByPurchase(moudle_name=moudle_name, case_name=case_name, request_method=request_method, url=request_url, data=json.loads(req_data))
            logging.info("返回结果：{}".format(res_text.json()))
            assert_common(res_text, msg=exc_data)
            batchNo = res_text.json().get("data")[0].get("batchNo")
            expireTime = res_text.json().get("data")[0].get("expireDate")
            manufacturer = res_text.json().get("data")[0].get("manufacturer")
            medicineName = res_text.json().get("data")[0].get("medicineName")
            medicineId = res_text.json().get("data")[0].get("medicineId")
            newPrice = res_text.json().get("data")[0].get("newPrice")
            packUnit = res_text.json().get("data")[0].get("packUnit")
            retailPrice = res_text.json().get("data")[0].get("retailPrice")
            specs = res_text.json().get("data")[0].get("specs")
            type = res_text.json().get("data")[0].get("type")
        elif case_name == "查看入库列表":
            res_text = ApiFactory.get_purchase().purchaseList(moudle_name=moudle_name, case_name=case_name,
                                                              request_method=request_method, url=request_url,
                                                              data=json.loads(req_data))
            logging.info("返回结果：{}".format(res_text.json()))
            assert_common(res_text, msg=exc_data)
            id = res_text.json().get("data").get("records")[0].get("id")
        elif case_name == "暂存":
            res_text = ApiFactory.get_purchase().temporaryStorage(moudle_name=moudle_name, case_name=case_name, request_method=request_method, url=request_url, data=json.loads(req_data), supplierId=supplierId,
                                                             medicineId=medicineId, purchaseUnit=packUnit, purchaseUnitPrice=newPrice, retailUnit=packUnit, batchNo=batchNo, expireTime=expireTime,
                                                             medicineName=medicineName, specs=specs, manufacturer=manufacturer, type=type, retailPrice=retailPrice)
            logging.info("返回结果：{}".format(res_text.json()))
            assert_common(res_text, msg=exc_data)
        elif case_name == "删除":
            res_text = ApiFactory.get_purchase().purchaseDelete(moudle_name=moudle_name, case_name=case_name, request_method=request_method, url=request_url, data=json.loads(req_data), id=id)
            logging.info("返回结果：{}".format(res_text.json()))
            assert_common(res_text, msg=exc_data)

    @allure.story("采购入库菜单")
    @allure.severity("BLOCKER")
    @allure.description("003-采购入库-新云药房入库")
    @pytest.mark.parametrize("moudle_name,case_name,request_method,request_url,req_data,code,exc_data", read_test_data(data_path, "云药房入库", None, 1, 2, 3, 4, 7, 8, 9))
    def test_centerPurchase_case(self, moudle_name, case_name, request_method, request_url, req_data, code, exc_data,  clinic_login):

        global supplierId,packUnit,name,approvalNumber,barCode,code2,manufacturer,purchaseUnit,retailPrice,specs,type,medicareFlag

        if case_name == "查询供应商":
            res_text = ApiFactory.get_purchase().supplierList(moudle_name=moudle_name, case_name=case_name, request_method=request_method, url=request_url, data=json.loads(req_data))
            logging.info("返回结果：{}".format(res_text.json()))
            assert_common(res_text, msg=exc_data)
            supplierId = res_text.json().get("data")[0].get("supplierId")

        if case_name == "中心库列表":
            res_text = ApiFactory.get_purchase().centerPurchaseList(moudle_name=moudle_name, case_name=case_name, request_method=request_method, url=request_url, data=json.loads(req_data))
            logging.info("返回结果：{}".format(res_text.json()))
            assert_common(res_text, msg=exc_data)
            approvalNumber = res_text.json().get("data")[0].get("approvalNumber")
            barCode = res_text.json().get("data")[0].get("barCode")
            code2 = res_text.json().get("data")[0].get("code")
            manufacturer = res_text.json().get("data")[0].get("manufacturer")
            medicareFlag = res_text.json().get("data")[0].get("medicareFlag")
            name = res_text.json().get("data")[0].get("name")
            packUnit = res_text.json().get("data")[0].get("packUnit")
            purchaseUnit = res_text.json().get("data")[0].get("purchaseUnit")
            retailPrice = res_text.json().get("data")[0].get("retailPrice")
            specs = res_text.json().get("data")[0].get("specs")
            type = res_text.json().get("data")[0].get("type")

        if case_name == "入库":
            res_text = ApiFactory.get_purchase().centerNewPurchase(moudle_name=moudle_name, case_name=case_name, request_method=request_method, url=request_url, data=json.loads(req_data), supplierId=supplierId,
                                                                retailUnit=packUnit,  medicineName=name, specs=specs, manufacturer=manufacturer, barCode=barCode, type=type, approvalNumber=approvalNumber,
                                                                retailPrice=retailPrice, purchaseUnit=purchaseUnit, medicareFlag=medicareFlag, centerMedicineCode=code2)
            logging.info("返回结果：{}".format(res_text.json()))
            assert_common(res_text, msg=exc_data)