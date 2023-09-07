# -*- coding: utf-8 -*-
# @Time    : 2022/3/10 11:29
# @Author  : PengJiong
# @Email   : 18390050274@qq.com
# @File    : test_saleOrders.py.py

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

@allure.feature("药房管理")
class TestSaleOrders:
    curPath = os.path.abspath(os.path.dirname(__file__))
    rootPath = os.path.split(curPath)[0]
    sys.path.append(rootPath)
    data_path = rootPath + r"\data\saleOrders.xls"

    '''
    @allure.severity装饰器按严重性级别来标记case　　　
    执行指定测试用例 --allure-severities blocker
    BLOCKER = 'blocker'　　阻塞缺陷
    CRITICAL = 'critical'　严重缺陷
    NORMAL = 'normal'　　  一般缺陷
    MINOR = 'minor'　　    次要缺陷
    TRIVIAL = 'trivial'　　轻微缺陷　
    '''


    @allure.story("零售记录模块")
    @allure.severity("BLOCKER")
    @allure.description("001药品零售-退费")
    @pytest.mark.parametrize("moudle_name,case_name,request_method,request_url,req_data,code,exc_data", read_test_data(data_path, "退费", None, 1, 2, 3, 4, 7, 8, 9))
    def test_saleOrders_case(self, moudle_name, case_name, request_method, request_url, req_data, code, exc_data, clinic_login):
        global deptId, jobId, doctorId, registerId, visitOrderId, patientId, batchNo, total, pieceTotal, packUnit, specs, retailPrice, manufacturer, stock, id, clinicId, namePinyin, manufacturerPinyin,\
            packAmount, pieceAmount, stockId, newPrice, medicineId, expireDate, supplierId, orderType, medicineName, hospital, checkedType, doctor, cash


        if case_name == "getInfo":
            res_text = ApiFactory.get_saleOrders().getInfo(moudle_name=moudle_name, case_name=case_name,
                                                        request_method=request_method, url=request_url,
                                                        data=req_data)
            logging.info("返回结果：{}".format(res_text.json()))
            assert_common(res_text, msg=exc_data)
            deptId = res_text.json().get("user").get("deptId")
            jobId = res_text.json().get("user").get("jobId")
            doctorId = res_text.json().get("user").get("userId")

        if case_name == "药品零售菜单":
            res_text = ApiFactory.get_saleOrders().pendingOrderList(moudle_name=moudle_name, case_name=case_name,
                                                                 request_method=request_method, url=request_url,
                                                                 data=req_data)
            logging.info("返回结果：{}".format(res_text.json()))
            assert_common(res_text, msg=exc_data)

        if case_name == "药品搜索":
            res_text = ApiFactory.get_saleOrders().selectMedicineStock(moudle_name=moudle_name, case_name=case_name,
                                                                 request_method=request_method, url=request_url,
                                                                 data=json.loads(req_data))
            logging.info("返回结果：{}".format(res_text.json()))
            assert_common(res_text, msg=exc_data)
            total = res_text.json().get("data")[0].get("total")
            pieceTotal = res_text.json().get("data")[0].get("pieceTotal")
            batchNo = res_text.json().get("data")[0].get("batchNo")
            packUnit = res_text.json().get("data")[0].get("packUnit")
            medicineName = res_text.json().get("data")[0].get("medicineName")
            specs = res_text.json().get("data")[0].get("specs")
            retailPrice = res_text.json().get("data")[0].get("retailPrice")
            stock = res_text.json().get("data")[0].get("stock")
            id = res_text.json().get("data")[0].get("id")
            clinicId = res_text.json().get("data")[0].get("clinicId")
            namePinyin = res_text.json().get("data")[0].get("namePinyin")
            manufacturerPinyin = res_text.json().get("data")[0].get("manufacturerPinyin")
            packAmount = res_text.json().get("data")[0].get("packAmount")
            stockId = res_text.json().get("data")[0].get("stockId")
            newPrice = res_text.json().get("data")[0].get("newPrice")
            medicineId = res_text.json().get("data")[0].get("medicineId")
            expireDate = res_text.json().get("data")[0].get("expirDate")
            supplierId = res_text.json().get("data")[0].get("supplierId")

        if case_name == "下单收费":
            res_text = ApiFactory.get_saleOrders().speedPlaceAnOrder(moudle_name=moudle_name,case_name=case_name,request_method=request_method,url=request_url,
                                                                            data=json.loads(req_data),retailPrice=retailPrice, medicineId=medicineId,batchNo=batchNo, total=total,
                                                                            packUnit=packUnit, medicineName=medicineName, specs=specs, stock=stock, clinicId=clinicId,namePinyin=namePinyin,
                                                                            manufacturerPinyin=manufacturerPinyin, packAmount=packAmount, stockId=stockId, newPrice=newPrice, expireDate=expireDate, supplierId=supplierId)
            logging.info("返回结果：{}".format(res_text.json()))
            assert_common(res_text, msg=exc_data)
            visitOrderId = res_text.json().get("data").get("visitOrder").get("id")
            orderType = res_text.json().get("data").get("visitOrder").get("orderType")
            logging.info("下单后获取到的visitOrderID为：{}".format(visitOrderId))

        if case_name == "检查药物处方":
            res_text = ApiFactory.get_saleOrders().checkedPrescriptionsDrug(moudle_name=moudle_name, case_name=case_name,
                                                                     request_method=request_method, url=request_url,
                                                                     data=json.loads(req_data), visitOrderId=visitOrderId, orderType=orderType)
            logging.info("返回结果：{}".format(res_text.json()))
            assert_common(res_text, msg=exc_data)
            # checkedType = res_text.json().get("data")[0].get("checkedType")
            # hospital = res_text.json().get("data")[0].get("hospital")
            # doctor = res_text.json().get("data")[0].get("doctor")

        if case_name == "确定支付":
            res_text = ApiFactory.get_saleOrders().charge(moudle_name=moudle_name, case_name=case_name,
                                                                        request_method=request_method, url=request_url,
                                                                        data=json.loads(req_data),visitOrderId=visitOrderId,retailPrice=retailPrice)

            logging.info("返回结果：{}".format(res_text.json()))
            assert_common(res_text, msg=exc_data)

        if case_name == "零售记录菜单":
            res_text = ApiFactory.get_saleOrders().saleOrders1(moudle_name=moudle_name, case_name=case_name,
                                                                    request_method=request_method, url=request_url,
                                                                    data=json.loads(req_data))
            logging.info("返回结果：{}".format(res_text.json()))
            assert_common(res_text, msg=exc_data)

        if case_name == "订单退款核实":
            res_text = ApiFactory.get_saleOrders().orderRefundVerify(moudle_name=moudle_name, case_name=case_name,
                                                              request_method=request_method, url=request_url,
                                                              data=json.loads(req_data), visitOrderId=visitOrderId)
            logging.info("返回结果：{}".format(res_text.json()))
            assert_common(res_text, msg=exc_data)
            if case_name == "退费校验":
                status = res_text.json().get("data").get("status")
                assert status == 3, "退费失败，退费后，订单号%s 返回的status!=3，实际status=%s" % (visitOrderId, status)

        if case_name == "订单退款":
            res_text = ApiFactory.get_saleOrders().orderRefund(moudle_name=moudle_name, case_name=case_name,
                                                                     request_method=request_method, url=request_url,
                                                                     data=json.loads(req_data), visitOrderId=visitOrderId, retailPrice=retailPrice)
            logging.info("返回结果：{}".format(res_text.json()))
            assert_common(res_text, msg=exc_data)
