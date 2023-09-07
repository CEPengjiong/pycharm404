"""
description: 药品零售接口测试用例
time: 2022/3/10
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

@allure.feature("药品管理模块")
class TestRetail:
    curPath = os.path.abspath(os.path.dirname(__file__))
    rootPath = os.path.split(curPath)[0]
    sys.path.append(rootPath)
    data_path = rootPath + r"\data\retail.xls"

    '''
    @allure.severity装饰器按严重性级别来标记case　　　
    执行指定测试用例 --allure-severities blocker
    BLOCKER = 'blocker'　　阻塞缺陷
    CRITICAL = 'critical'　严重缺陷
    NORMAL = 'normal'　　  一般缺陷
    MINOR = 'minor'　　    次要缺陷
    TRIVIAL = 'trivial'　　轻微缺陷　
    '''

    @allure.story("药品零售菜单")
    @allure.severity("BLOCKER")
    @allure.description("001-查询药品-收费")
    @pytest.mark.parametrize("moudle_name,case_name,request_method,request_url,req_data,code,exc_data",
                             read_test_data(data_path, "收费", None, 1, 2, 3, 4, 7, 8, 9))
    def test_retailPlaceAnOrder_case(self, moudle_name, case_name, request_method, request_url, req_data, code, exc_data, clinic_login):
        global deptId, jobId, doctorId, registerId, visitOrderId, patientId, batchNo, total, pieceTotal, packUnit, specs, retailPrice, manufacturer, stock, id, clinicId, namePinyin, manufacturerPinyin, \
            packAmount, pieceAmount, stockId, newPrice, medicineId, expireDate, supplierId, orderType, medicineName

        if case_name == "getInfo":
            res_text = ApiFactory.get_retail().getInfo(moudle_name=moudle_name, case_name=case_name,
                                                                  request_method=request_method, url=request_url,
                                                                  data=req_data)
            logging.info("返回结果：{}".format(res_text.json()))
            assert_common(res_text, msg=exc_data)
            deptId = res_text.json().get("user").get("deptId")
            jobId = res_text.json().get("user").get("jobId")
            doctorId = res_text.json().get("user").get("userId")

        if case_name == "药品搜索":
            res_text = ApiFactory.get_retail().selectMedicineStock(moudle_name=moudle_name,
                                                                              case_name=case_name,
                                                                              request_method=request_method,
                                                                              url=request_url,
                                                                              data=json.loads(req_data))
            logging.info("返回结果：{}".format(res_text.json()))
            assert_common(res_text, msg=exc_data)
            batchNo = res_text.json().get("data")[0].get("batchNo")
            total = res_text.json().get("data")[0].get("total")
            pieceTotal = res_text.json().get("data")[0].get("pieceTotal")
            packUnit = res_text.json().get("data")[0].get("packUnit")
            specs = res_text.json().get("data")[0].get("specs")
            retailPrice = res_text.json().get("data")[0].get("retailPrice")
            manufacturer = res_text.json().get("data")[0].get("manufacturer")
            stock = res_text.json().get("data")[0].get("stock")
            id = res_text.json().get("data")[0].get("id")
            clinicId = res_text.json().get("data")[0].get("clinicId")
            namePinyin = res_text.json().get("data")[0].get("namePinyin")
            manufacturerPinyin = res_text.json().get("data")[0].get("manufacturerPinyin")
            packAmount = res_text.json().get("data")[0].get("packAmount")
            pieceAmount = res_text.json().get("data")[0].get("pieceAmount")
            stockId = res_text.json().get("data")[0].get("stockId")
            newPrice = res_text.json().get("data")[0].get("newPrice")
            medicineId = res_text.json().get("data")[0].get("medicineId")
            expireDate = res_text.json().get("data")[0].get("expireDate")
            supplierId = res_text.json().get("data")[0].get("supplierId")
            medicineName = res_text.json().get("data")[0].get("medicineName")

        if case_name == "零售下单":
            res_text = ApiFactory.get_retail().retailPlaceAnOrder(moudle_name=moudle_name, case_name=case_name, request_method=request_method, url=request_url, data=json.loads(req_data), batchNo=batchNo, total=total, packUnit=packUnit, specs=specs, retailPrice=retailPrice,
                                                                  manufacturer=manufacturer, stock=stock, clinicId=clinicId, namePinyin=namePinyin, manufacturerPinyin=manufacturerPinyin, packAmount=packAmount, stockId=stockId, newPrice=newPrice, medicineId=medicineId, expireDate=expireDate,
                                                                  supplierId=supplierId, medicineName=medicineName)
            logging.info("返回结果：{}".format(res_text.json()))
            assert_common(res_text, msg=exc_data)
            visitOrderId = res_text.json().get("data").get("visitOrder").get("id")
            orderType = res_text.json().get("data").get("visitOrder").get("orderType")
            logging.info("下单后获取到的visitOrderID为：{}".format(visitOrderId))

        if case_name == "校验是否处方药":
            res_text = ApiFactory.get_retail().checkedPrescriptionsDrug(moudle_name=moudle_name, case_name=case_name, request_method=request_method, url=request_url, data=json.loads(req_data), visitOrderId=visitOrderId, orderType=orderType)
            logging.info("返回结果：{}".format(res_text.json()))
            assert_common(res_text, msg=exc_data)


        if case_name == "收费发药":
            res_text = ApiFactory.get_retail().charge(moudle_name=moudle_name, case_name=case_name, request_method=request_method, url=request_url, data=json.loads(req_data), visitOrderId=visitOrderId, retailPrice=retailPrice)
            logging.info("返回结果：{}".format(res_text.json()))
            assert_common(res_text, msg=exc_data)

    @allure.story("药品零售菜单")
    @allure.severity("BLOCKER")
    @allure.description("002-查询药品-欠费-收费-补交")
    @pytest.mark.parametrize("moudle_name,case_name,request_method,request_url,req_data,code,exc_data", read_test_data(data_path, "欠费", None, 1, 2, 3, 4, 7, 8, 9))
    def test_retailArrearage_case(self, moudle_name, case_name, request_method, request_url, req_data, code, exc_data, clinic_login):
        global registerId, visitOrderId, patientId, batchNo, total, pieceTotal, packUnit, specs, retailPrice, manufacturer, stock, id, clinicId, namePinyin, manufacturerPinyin, \
            packAmount, pieceAmount, stockId, newPrice, medicineId, expireDate, supplierId, orderType, medicineName, saleOrderId

        if case_name == "药品搜索":
            res_text = ApiFactory.get_retail().selectMedicineStock(moudle_name=moudle_name,
                                                                              case_name=case_name,
                                                                              request_method=request_method,
                                                                              url=request_url,
                                                                              data=json.loads(req_data))
            logging.info("返回结果：{}".format(res_text.json()))
            assert_common(res_text, msg=exc_data)
            batchNo = res_text.json().get("data")[0].get("batchNo")
            total = res_text.json().get("data")[0].get("total")
            pieceTotal = res_text.json().get("data")[0].get("pieceTotal")
            packUnit = res_text.json().get("data")[0].get("packUnit")
            specs = res_text.json().get("data")[0].get("specs")
            retailPrice = res_text.json().get("data")[0].get("retailPrice")
            manufacturer = res_text.json().get("data")[0].get("manufacturer")
            stock = res_text.json().get("data")[0].get("stock")
            id = res_text.json().get("data")[0].get("id")
            clinicId = res_text.json().get("data")[0].get("clinicId")
            namePinyin = res_text.json().get("data")[0].get("namePinyin")
            manufacturerPinyin = res_text.json().get("data")[0].get("manufacturerPinyin")
            packAmount = res_text.json().get("data")[0].get("packAmount")
            pieceAmount = res_text.json().get("data")[0].get("pieceAmount")
            stockId = res_text.json().get("data")[0].get("stockId")
            newPrice = res_text.json().get("data")[0].get("newPrice")
            medicineId = res_text.json().get("data")[0].get("medicineId")
            expireDate = res_text.json().get("data")[0].get("expireDate")
            supplierId = res_text.json().get("data")[0].get("supplierId")
            medicineName = res_text.json().get("data")[0].get("medicineName")

        if case_name == "零售下单":
            res_text = ApiFactory.get_retail().retailPlaceAnOrder(moudle_name=moudle_name, case_name=case_name, request_method=request_method, url=request_url, data=json.loads(req_data), batchNo=batchNo, total=total, packUnit=packUnit, specs=specs, retailPrice=retailPrice,
                                                                  manufacturer=manufacturer, stock=stock, clinicId=clinicId, namePinyin=namePinyin, manufacturerPinyin=manufacturerPinyin, packAmount=packAmount, stockId=stockId, newPrice=newPrice, medicineId=medicineId, expireDate=expireDate,
                                                                  supplierId=supplierId, medicineName=medicineName)
            logging.info("返回结果：{}".format(res_text.json()))
            assert_common(res_text, msg=exc_data)
            visitOrderId = res_text.json().get("data").get("visitOrder").get("id")
            orderType = res_text.json().get("data").get("visitOrder").get("orderType")
            logging.info("下单后获取到的visitOrderID为：{}".format(visitOrderId))

        if case_name == "校验是否处方药":
            res_text = ApiFactory.get_retail().checkedPrescriptionsDrug(moudle_name=moudle_name, case_name=case_name, request_method=request_method, url=request_url, data=json.loads(req_data), visitOrderId=visitOrderId, orderType=orderType)
            logging.info("返回结果：{}".format(res_text.json()))
            assert_common(res_text, msg=exc_data)


        if case_name == "欠费":
            res_text = ApiFactory.get_retail().charge(moudle_name=moudle_name, case_name=case_name, request_method=request_method, url=request_url, data=json.loads(req_data), visitOrderId=visitOrderId, retailPrice=retailPrice)
            logging.info("返回结果：{}".format(res_text.json()))
            assert_common(res_text, msg=exc_data)

        if case_name == "查询列表":
            res_text = ApiFactory.get_retail().saleOrders(moudle_name=moudle_name, case_name=case_name, request_method=request_method, url=request_url, data=json.loads(req_data))
            logging.info("返回结果：{}".format(res_text.json()))
            assert_common(res_text, msg=exc_data)
            saleOrderId = res_text.json().get("data").get("records")[0].get("saleOrderId")

        if case_name == "补交":
            res_text = ApiFactory.get_retail().charge2(moudle_name=moudle_name, case_name=case_name,
                                                      request_method=request_method, url=request_url,
                                                      data=json.loads(req_data), visitOrderId=visitOrderId,
                                                      retailPrice=retailPrice, saleOrderId=saleOrderId)
            logging.info("返回结果：{}".format(res_text.json()))
            assert_common(res_text, msg=exc_data)


    @allure.story("药品零售菜单")
    @allure.severity("BLOCKER")
    @allure.description("003-查询药品-挂单-收费-退费")
    @pytest.mark.parametrize("moudle_name,case_name,request_method,request_url,req_data,code,exc_data", read_test_data(data_path, "挂单", None, 1, 2, 3, 4, 7, 8, 9))
    def test_entryOrders_case(self, moudle_name, case_name, request_method, request_url, req_data, code, exc_data, clinic_login):
        global registerId, visitOrderId, patientId, batchNo, total, pieceTotal, packUnit, specs, retailPrice, manufacturer, stock, id, clinicId, namePinyin, manufacturerPinyin, \
            packAmount, pieceAmount, stockId, newPrice, medicineId, expireDate, supplierId, orderType, medicineName, patientName, saleOrderId, saleDetailId

        if case_name == "药品搜索":
            res_text = ApiFactory.get_retail().selectMedicineStock(moudle_name=moudle_name,
                                                                              case_name=case_name,
                                                                              request_method=request_method,
                                                                              url=request_url,
                                                                              data=json.loads(req_data))
            logging.info("返回结果：{}".format(res_text.json()))
            assert_common(res_text, msg=exc_data)
            batchNo = res_text.json().get("data")[0].get("batchNo")
            total = res_text.json().get("data")[0].get("total")
            pieceTotal = res_text.json().get("data")[0].get("pieceTotal")
            packUnit = res_text.json().get("data")[0].get("packUnit")
            specs = res_text.json().get("data")[0].get("specs")
            retailPrice = res_text.json().get("data")[0].get("retailPrice")
            manufacturer = res_text.json().get("data")[0].get("manufacturer")
            stock = res_text.json().get("data")[0].get("stock")
            id = res_text.json().get("data")[0].get("id")
            clinicId = res_text.json().get("data")[0].get("clinicId")
            namePinyin = res_text.json().get("data")[0].get("namePinyin")
            manufacturerPinyin = res_text.json().get("data")[0].get("manufacturerPinyin")
            packAmount = res_text.json().get("data")[0].get("packAmount")
            pieceAmount = res_text.json().get("data")[0].get("pieceAmount")
            stockId = res_text.json().get("data")[0].get("stockId")
            newPrice = res_text.json().get("data")[0].get("newPrice")
            medicineId = res_text.json().get("data")[0].get("medicineId")
            expireDate = res_text.json().get("data")[0].get("expireDate")
            supplierId = res_text.json().get("data")[0].get("supplierId")
            medicineName = res_text.json().get("data")[0].get("medicineName")

        if case_name == "挂单":
            res_text = ApiFactory.get_retail().entryOrders(moudle_name=moudle_name, case_name=case_name, request_method=request_method, url=request_url, data=json.loads(req_data),
                                                           batchNo=batchNo, total=total, packUnit=packUnit, medicineName=medicineName, specs=specs, retailPrice=retailPrice, manufacturer=manufacturer, stock=stock, id=id, clinicId=clinicId, namePinyin=namePinyin, manufacturerPinyin=manufacturerPinyin, packAmount=packAmount, stockId=stockId, newPrice=newPrice, medicineId=medicineId, expireDate=expireDate, supplierId=supplierId)

            logging.info("返回结果：{}".format(res_text.json()))
            assert_common(res_text, msg=exc_data)

        if case_name == "查询挂单":
            res_text = ApiFactory.get_retail().pendingOrderList(moudle_name=moudle_name,
                                                                              case_name=case_name,
                                                                              request_method=request_method,
                                                                              url=request_url,
                                                                              data=json.loads(req_data))
            logging.info("返回结果：{}".format(res_text.json()))
            assert_common(res_text, msg=exc_data)
            saleOrderId = res_text.json().get("data")[0].get("saleOrderId")
            patientName = res_text.json().get("data")[0].get("patientName")

        if case_name == "挂单详情":
            res_text = ApiFactory.get_retail().pendingOrderDetails(moudle_name=moudle_name, case_name=case_name, request_method=request_method, url=request_url, data=json.loads(req_data), saleOrderId=saleOrderId)
            logging.info("返回结果：{}".format(res_text.json()))
            assert_common(res_text, msg=exc_data)
            saleDetailId = res_text.json().get("data").get("pendingOrderDrugInfoVOS")[0].get("saleDetailId")

        if case_name == "下单":
            res_text = ApiFactory.get_retail().retailPlaceAnOrder2(moudle_name=moudle_name, case_name=case_name, request_method=request_method, url=request_url, data=json.loads(req_data),
                                                                      batchNo=batchNo, total=total, packUnit=packUnit, specs=specs, retailPrice=retailPrice,
                                                                      manufacturer=manufacturer, stock=stock, clinicId=clinicId, namePinyin=namePinyin,
                                                                      manufacturerPinyin=manufacturerPinyin, packAmount=packAmount, stockId=stockId,
                                                                      newPrice=newPrice, medicineId=medicineId, expireDate=expireDate,
                                                                      supplierId=supplierId, medicineName=medicineName, saleDetailId=saleDetailId)
            logging.info("返回结果：{}".format(res_text.json()))
            assert_common(res_text, msg=exc_data)
            visitOrderId = res_text.json().get("data").get("visitOrder").get("id")
            orderType = res_text.json().get("data").get("visitOrder").get("orderType")
            logging.info("下单后获取到的visitOrderID为：{}".format(visitOrderId))

        if case_name == "校验是否处方药":
            res_text = ApiFactory.get_retail().checkedPrescriptionsDrug(moudle_name=moudle_name, case_name=case_name,
                                                                        request_method=request_method, url=request_url,
                                                                        data=json.loads(req_data),
                                                                        visitOrderId=visitOrderId, orderType=orderType)
            logging.info("返回结果：{}".format(res_text.json()))
            assert_common(res_text, msg=exc_data)

        if case_name == "挂单收费":
            res_text = ApiFactory.get_retail().charge2(moudle_name=moudle_name, case_name=case_name,
                                                      request_method=request_method, url=request_url,
                                                      data=json.loads(req_data), visitOrderId=visitOrderId,
                                                      retailPrice=retailPrice, saleOrderId=saleOrderId)
            logging.info("返回结果：{}".format(res_text.json()))
            assert_common(res_text, msg=exc_data)

        if case_name == "零售退费":
            res_text = ApiFactory.get_retail().orderRefund(moudle_name=moudle_name, case_name=case_name,
                                                      request_method=request_method, url=request_url,
                                                      data=json.loads(req_data), visitOrderId=visitOrderId,
                                                      retailPrice=retailPrice)
            logging.info("返回结果：{}".format(res_text.json()))
            assert_common(res_text, msg=exc_data)


    @allure.story("药品零售菜单")
    @allure.severity("BLOCKER")
    @allure.description("003-查询药品-挂单-删除挂单")
    @pytest.mark.parametrize("moudle_name,case_name,request_method,request_url,req_data,code,exc_data", read_test_data(data_path, "删除挂单", None, 1, 2, 3, 4, 7, 8, 9))
    def test_deleteSaleOrder_case(self, moudle_name, case_name, request_method, request_url, req_data, code, exc_data, clinic_login):
        global registerId, visitOrderId, patientId, batchNo, total, pieceTotal, packUnit, specs, retailPrice, manufacturer, stock, id, clinicId, namePinyin, manufacturerPinyin, \
            packAmount, pieceAmount, stockId, newPrice, medicineId, expireDate, supplierId, orderType, medicineName, patientName, saleOrderId, saleDetailId

        if case_name == "药品搜索":
            res_text = ApiFactory.get_retail().selectMedicineStock(moudle_name=moudle_name,
                                                                              case_name=case_name,
                                                                              request_method=request_method,
                                                                              url=request_url,
                                                                              data=json.loads(req_data))
            logging.info("返回结果：{}".format(res_text.json()))
            assert_common(res_text, msg=exc_data)
            batchNo = res_text.json().get("data")[0].get("batchNo")
            total = res_text.json().get("data")[0].get("total")
            pieceTotal = res_text.json().get("data")[0].get("pieceTotal")
            packUnit = res_text.json().get("data")[0].get("packUnit")
            specs = res_text.json().get("data")[0].get("specs")
            retailPrice = res_text.json().get("data")[0].get("retailPrice")
            manufacturer = res_text.json().get("data")[0].get("manufacturer")
            stock = res_text.json().get("data")[0].get("stock")
            id = res_text.json().get("data")[0].get("id")
            clinicId = res_text.json().get("data")[0].get("clinicId")
            namePinyin = res_text.json().get("data")[0].get("namePinyin")
            manufacturerPinyin = res_text.json().get("data")[0].get("manufacturerPinyin")
            packAmount = res_text.json().get("data")[0].get("packAmount")
            pieceAmount = res_text.json().get("data")[0].get("pieceAmount")
            stockId = res_text.json().get("data")[0].get("stockId")
            newPrice = res_text.json().get("data")[0].get("newPrice")
            medicineId = res_text.json().get("data")[0].get("medicineId")
            expireDate = res_text.json().get("data")[0].get("expireDate")
            supplierId = res_text.json().get("data")[0].get("supplierId")
            medicineName = res_text.json().get("data")[0].get("medicineName")

        if case_name == "挂单":
            res_text = ApiFactory.get_retail().entryOrders(moudle_name=moudle_name, case_name=case_name, request_method=request_method, url=request_url, data=json.loads(req_data),
                                                           batchNo=batchNo, total=total, packUnit=packUnit, medicineName=medicineName, specs=specs, retailPrice=retailPrice, manufacturer=manufacturer, stock=stock, id=id, clinicId=clinicId, namePinyin=namePinyin, manufacturerPinyin=manufacturerPinyin, packAmount=packAmount, stockId=stockId, newPrice=newPrice, medicineId=medicineId, expireDate=expireDate, supplierId=supplierId)

            logging.info("返回结果：{}".format(res_text.json()))
            assert_common(res_text, msg=exc_data)

        if case_name == "查询挂单":
            res_text = ApiFactory.get_retail().pendingOrderList(moudle_name=moudle_name,
                                                                              case_name=case_name,
                                                                              request_method=request_method,
                                                                              url=request_url,
                                                                              data=json.loads(req_data))
            logging.info("返回结果：{}".format(res_text.json()))
            assert_common(res_text, msg=exc_data)
            saleOrderId = res_text.json().get("data")[0].get("saleOrderId")
            patientName = res_text.json().get("data")[0].get("patientName")

        if case_name == "删除挂单":
            res_text = ApiFactory.get_retail().deleteSaleOrder(moudle_name=moudle_name,
                                                                              case_name=case_name,
                                                                              request_method=request_method,
                                                                              url=request_url,
                                                                              data=json.loads(req_data), saleOrderId=saleOrderId)
            logging.info("返回结果：{}".format(res_text.json()))
            assert_common(res_text, msg=exc_data)
