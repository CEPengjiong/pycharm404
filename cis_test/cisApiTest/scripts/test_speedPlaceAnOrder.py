"""
description: 快速接诊接口测试用例
time: 2022/3/01
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

@allure.feature("门诊管理模块")
class TestSpeedPlaceAnOrder:
    curPath = os.path.abspath(os.path.dirname(__file__))
    rootPath = os.path.split(curPath)[0]
    sys.path.append(rootPath)
    data_path = rootPath + r"\data\speedPlaceAnOrder.xls"

    '''
    @allure.severity装饰器按严重性级别来标记case　　　
    执行指定测试用例 --allure-severities blocker
    BLOCKER = 'blocker'　　阻塞缺陷
    CRITICAL = 'critical'　严重缺陷
    NORMAL = 'normal'　　  一般缺陷
    MINOR = 'minor'　　    次要缺陷
    TRIVIAL = 'trivial'　　轻微缺陷　
    '''


    @allure.story("快速接诊菜单")
    @allure.severity("BLOCKER")
    @allure.description("001快速接诊-收费")
    @pytest.mark.parametrize("moudle_name,case_name,request_method,request_url,req_data,code,exc_data", read_test_data(data_path, "收费", None, 1, 2, 3, 4, 7, 8, 9))
    def test_speedPlaceAnOrder_case(self, moudle_name, case_name, request_method, request_url, req_data, code, exc_data,clinic_login):
        # logging.info("请求的header：{}".format(api_config.request_header))
        global deptId, jobId, doctorId, registerId, visitOrderId, patientId, batchNo, total, pieceTotal, packUnit, specs, retailPrice, manufacturer, stock, id, clinicId, namePinyin, manufacturerPinyin,\
            packAmount, pieceAmount, stockId, newPrice, medicineId, expireDate, supplierId, orderType, medicineName


        if case_name == "getInfo":
            res_text = ApiFactory.get_speedPlaceAnOrder().getInfo(moudle_name=moudle_name, case_name=case_name, request_method=request_method, url=request_url, data=req_data)
            logging.info("返回结果：{}".format(res_text.json()))
            assert_common(res_text, msg=exc_data)
            deptId = res_text.json().get("user").get("deptId")
            jobId = res_text.json().get("user").get("jobId")
            doctorId = res_text.json().get("user").get("userId")

        if case_name == "药品搜索":
            res_text = ApiFactory.get_speedPlaceAnOrder().selectMedicineStock(moudle_name=moudle_name, case_name=case_name, request_method=request_method, url=request_url, data=json.loads(req_data))
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

        if case_name == "快速下单":
            res_text = ApiFactory.get_speedPlaceAnOrder().speedPlaceAnOrder(moudle_name=moudle_name, case_name=case_name, request_method=request_method, url=request_url, data=json.loads(req_data), batchNo=batchNo, total=total, packUnit=packUnit, specs=specs, retailPrice=retailPrice, jobId=jobId, deptId=deptId,
                                                                            doctorId=doctorId, manufacturer=manufacturer, stock=stock, clinicId=clinicId, namePinyin=namePinyin, manufacturerPinyin=manufacturerPinyin, packAmount=packAmount, stockId=stockId, newPrice=newPrice, medicineId=medicineId, expireDate=expireDate, supplierId=supplierId, medicineName=medicineName)
            logging.info("返回结果：{}".format(res_text.json()))
            assert_common(res_text, msg=exc_data)
            visitOrderId = res_text.json().get("data").get("visitOrder").get("id")
            orderType = res_text.json().get("data").get("visitOrder").get("orderType")
            logging.info("下单后获取到的visitOrderID为：{}".format(visitOrderId))

        if case_name == "校验是否处方药":
            res_text = ApiFactory.get_speedPlaceAnOrder().checkedPrescriptionsDrug(moudle_name=moudle_name, case_name=case_name, request_method=request_method, url=request_url, data=json.loads(req_data), visitOrderId=visitOrderId, orderType=orderType)
            logging.info("返回结果：{}".format(res_text.json()))
            assert_common(res_text, msg=exc_data)

        if moudle_name == "收费发药":
            res_text = ApiFactory.get_speedPlaceAnOrder().charge(moudle_name=moudle_name, case_name=case_name, request_method=request_method, url=request_url, data=json.loads(req_data), visitOrderId=visitOrderId, retailPrice=retailPrice)
            logging.info("返回结果：{}".format(res_text.json()))
            assert_common(res_text, msg=exc_data)
