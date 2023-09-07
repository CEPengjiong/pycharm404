# -*- coding: utf-8 -*-
# @Time    : 2022/3/1 11:43
# @Author  : PengJiong
# @Email   : 18390050274@qq.com
# @File    : pendingOrderList.py.py

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

@allure.feature("药品零售模块")
class TestpendingOrderList:
    curPath = os.path.abspath(os.path.dirname(__file__))
    rootPath = os.path.split(curPath)[0]
    sys.path.append(rootPath)
    data_path = rootPath + r"\data\pendingOrderList.xls"

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
    @allure.severity("阻塞")
    @allure.description("001搜索药品-下单-支付-收费")
    @pytest.mark.parametrize("moudle_name,case_name,request_method,request_url,req_data,code,exc_data", read_test_data(data_path, "药品零售", None, 1, 2, 3, 4, 7, 8, 9))
    def test_charge_case(self, moudle_name, case_name, request_method, request_url, req_data, code, exc_data,clinic_login):
        # logging.info("请求的header：{}".format(api_config.request_header))
        global deptId, jobId, doctorId, registerId, visitOrderId, patientId, batchNo, total, pieceTotal, unit, specs, manufacturer, stock, id, clinicId, namePinyin, manufacturerPinyin,\
            packAmount, pieceAmount, stockId, newPrice, medicineId, expireDate, supplierId, orderType, medicineName , unit, retailPrice


        if case_name == "getInfo":
            res_text = ApiFactory.get_pendingOrderList().getInfo(moudle_name=moudle_name, case_name=case_name, request_method=request_method, url=request_url, data=req_data)
            logging.info("返回结果：{}".format(res_text.json()))
            assert_common(res_text, msg=exc_data)
            deptId = res_text.json().get("user").get("deptId")
            jobId = res_text.json().get("user").get("jobId")
            doctorId = res_text.json().get("user").get("userId")

        # if case_name == "药品零售列表":
        #     res_text = ApiFactory.get_pendingOrderList().pendingOrderList(moudle_name=moudle_name, case_name=case_name, request_method=request_method, url=request_url, data=req_data)
        #     logging.info("返回结果：{}".format(res_text.json()))
        #     assert_common(res_text, msg=exc_data)
        #     registerId = res_text.json().get("data").get("registerId")
        #     patientId = res_text.json().get("data").get("patientId")

        if case_name == "搜索(无)药品":
            res_text = ApiFactory.get_pendingOrderList().selectMedicineStock(moudle_name=moudle_name, case_name=case_name, request_method=request_method, url=request_url, data=json.loads(req_data))
            logging.info("返回结果：{}".format(res_text.json()))
            assert_common(res_text, msg=exc_data)
            batchNo = res_text.json().get("data")[0].get("batchNo")
            total = res_text.json().get("data")[0].get("total")
            pieceTotal = res_text.json().get("data")[0].get("pieceTotal")
            unit = res_text.json().get("data")[0].get("packUnit")
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

        if case_name == "收费发药":
            res_text = ApiFactory.get_pendingOrderList().retailPlaceAnOrder(moudle_name=moudle_name, case_name=case_name, request_method=request_method, url=request_url, data=json.loads(req_data), unit=unit, specs=specs, retailPrice=retailPrice,
                                                                            manufacturer= manufacturer, stock=stock, clinicId=clinicId, namePinyin=namePinyin, manufacturerPinyin=manufacturerPinyin, medicineId=medicineId, medicineName=medicineName)
            logging.info("返回结果：{}".format(res_text.json()))
            assert_common(res_text, msg=exc_data)
            visitOrderId = res_text.json().get("data").get("visitOrder").get("id")
            orderType = res_text.json().get("data").get("visitOrder").get("orderType")
            logging.info("下单后获取到的visitOrderID为：{}".format(visitOrderId))

        if case_name == "确定现金支付":
            res_text = ApiFactory.get_pendingOrderList().checkedPrescriptionsDrug(moudle_name=moudle_name, case_name=case_name, request_method=request_method, url=request_url, data=json.loads(req_data), visitOrderId=visitOrderId, orderType=orderType)
            logging.info("返回结果：{}".format(res_text.json()))
            assert_common(res_text, msg=exc_data)

        if case_name == "确定支付":
            res_text = ApiFactory.get_pendingOrderList().charge(moudle_name=moudle_name, case_name=case_name, request_method=request_method, url=request_url, data=json.loads(req_data), visitOrderId=visitOrderId, retailPrice=retailPrice)
            logging.info("返回结果：{}".format(res_text.json()))
            assert_common(res_text, msg=exc_data)

        if case_name == "支付完成列表校验":
            res_text = ApiFactory.get_pendingOrderList().pendingOrderList(moudle_name=moudle_name, case_name=case_name, request_method=request_method, url=request_url, data=json.loads(req_data))
            logging.info("返回结果：{}".format(res_text.json()))
            assert_common(res_text, msg=exc_data)