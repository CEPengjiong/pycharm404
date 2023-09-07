"""
description: 库存盘点接口测试用例
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


@allure.feature("药房管理-库存盘点")
class TestMedicineCheck:
    curPath = os.path.abspath(os.path.dirname(__file__))
    rootPath = os.path.split(curPath)[0]
    sys.path.append(rootPath)
    data_path = rootPath + r"\data\medicineCheck.xls"

    '''
    @allure.severity装饰器按严重性级别来标记case　　　
    执行指定测试用例 --allure-severities blocker
    BLOCKER = 'blocker'　　阻塞缺陷
    CRITICAL = 'critical'　严重缺陷
    NORMAL = 'normal'　　  一般缺陷
    MINOR = 'minor'　　    次要缺陷
    TRIVIAL = 'trivial'　　轻微缺陷　
    '''


    @allure.story("库存盘点")
    @allure.severity("BLOCKER")
    @allure.description("001-药品搜索-库存查询-盘点-列表查询-查看详情")
    @pytest.mark.parametrize("moudle_name,case_name,request_method,request_url,req_data,code,exc_data", read_test_data(data_path, "盘点", None, 1, 2, 3, 4, 7, 8, 9))
    def test_MedicineCheck_case(self, moudle_name, case_name, request_method, request_url, req_data, code, exc_data, clinic_login):

        global medicineId, batchNo, supplierId, bookPackAmount, expireDate, inboundDate, medicineName, newCostPrice, packUnit, retailPrice, specs, stockId, supplierName, totalAmount, id



        if case_name == "获取药品信息":
            res_text = ApiFactory.get_medicineCheck().selectMedicineStock(moudle_name=moudle_name,
                                                                              case_name=case_name,
                                                                              request_method=request_method,
                                                                              url=request_url,
                                                                              data=json.loads(req_data))
            logging.info("返回结果：{}".format(res_text.json()))
            assert_common(res_text, msg=exc_data)
            medicineId = res_text.json().get("data")[0].get("medicineId")
            batchNo = res_text.json().get("data")[0].get("batchNo")
            supplierId = res_text.json().get("data")[0].get("supplierId")
        if case_name == "搜索药品库存":
            res_text = ApiFactory.get_medicineCheck().selDrugStock(moudle_name=moudle_name,
                                                                              case_name=case_name,
                                                                              request_method=request_method,
                                                                              url=request_url,
                                                                              data=json.loads(req_data), medicineId=medicineId, batchNo=batchNo, supplierId=supplierId)
            logging.info("返回结果：{}".format(res_text.json()))
            assert_common(res_text, msg=exc_data)
            bookPackAmount = res_text.json().get("data")[0].get("bookPackAmount")
            expireDate = res_text.json().get("data")[0].get("expireDate")
            inboundDate = res_text.json().get("data")[0].get("inboundDate")
            medicineName = res_text.json().get("data")[0].get("medicineName")
            newCostPrice = res_text.json().get("data")[0].get("newCostPrice")
            packUnit = res_text.json().get("data")[0].get("packUnit")
            retailPrice = res_text.json().get("data")[0].get("retailPrice")
            specs = res_text.json().get("data")[0].get("specs")
            stockId = res_text.json().get("data")[0].get("stockId")
            supplierName = res_text.json().get("data")[0].get("supplierName")
            totalAmount = res_text.json().get("data")[0].get("totalAmount")

        if case_name == "变更":
            res_text = ApiFactory.get_medicineCheck().medicineCheck(moudle_name=moudle_name, case_name=case_name, request_method=request_method, url=request_url, data=json.loads(req_data),
                                                                   medicineId=medicineId, batchNo=batchNo, supplierId=supplierId, bookPackAmount=bookPackAmount, expireDate=expireDate,
                                                                   inboundDate=inboundDate, medicineName=medicineName, newCostPrice=newCostPrice, packUnit=packUnit,
                                                                   retailPrice=retailPrice, specs=specs, stockId=stockId, supplierName=supplierName, totalAmount=totalAmount)
            logging.info("返回结果：{}".format(res_text.json()))
            assert_common(res_text, msg=exc_data)

        if case_name == "总成本盈亏":
            res_text = ApiFactory.get_medicineCheck().costTotal(moudle_name=moudle_name,
                                                                              case_name=case_name,
                                                                              request_method=request_method,
                                                                              url=request_url,
                                                                              data=json.loads(req_data))
            logging.info("返回结果：{}".format(res_text.json()))
            assert_common(res_text, msg=exc_data)

        if case_name == "盘点列表":
            res_text = ApiFactory.get_medicineCheck().medicineCheckList(moudle_name=moudle_name,
                                                                              case_name=case_name,
                                                                              request_method=request_method,
                                                                              url=request_url,
                                                                              data=json.loads(req_data))
            logging.info("返回结果：{}".format(res_text.json()))
            assert_common(res_text, msg=exc_data)
            id = res_text.json().get("data").get("records")[0].get("id")

        if case_name == "查看详情":
            res_text = ApiFactory.get_medicineCheck().medicineCheckDetails(moudle_name=moudle_name,
                                                                              case_name=case_name,
                                                                              request_method=request_method,
                                                                              url=request_url,
                                                                              data=json.loads(req_data), id=id)
            logging.info("返回结果：{}".format(res_text.json()))
            assert_common(res_text, msg=exc_data)

    @allure.story("库存盘点")
    @allure.severity("BLOCKER")
    @allure.description("002-药品搜索-库存查询-暂存-删除")
    @pytest.mark.parametrize("moudle_name,case_name,request_method,request_url,req_data,code,exc_data", read_test_data(data_path, "暂存", None, 1, 2, 3, 4, 7, 8, 9))
    def test_MedicineCheckTS_case(self, moudle_name, case_name, request_method, request_url, req_data, code, exc_data, clinic_login):

        global medicineId, batchNo, supplierId, bookPackAmount, expireDate, inboundDate, medicineName, newCostPrice, packUnit, retailPrice, specs, stockId, supplierName, totalAmount, id



        if case_name == "获取药品信息":
            res_text = ApiFactory.get_medicineCheck().selectMedicineStock(moudle_name=moudle_name,
                                                                              case_name=case_name,
                                                                              request_method=request_method,
                                                                              url=request_url,
                                                                              data=json.loads(req_data))
            logging.info("返回结果：{}".format(res_text.json()))
            assert_common(res_text, msg=exc_data)
            medicineId = res_text.json().get("data")[0].get("medicineId")
            batchNo = res_text.json().get("data")[0].get("batchNo")
            supplierId = res_text.json().get("data")[0].get("supplierId")
        if case_name == "搜索药品库存":
            res_text = ApiFactory.get_medicineCheck().selDrugStock(moudle_name=moudle_name,
                                                                              case_name=case_name,
                                                                              request_method=request_method,
                                                                              url=request_url,
                                                                              data=json.loads(req_data), medicineId=medicineId, batchNo=batchNo, supplierId=supplierId)
            logging.info("返回结果：{}".format(res_text.json()))
            assert_common(res_text, msg=exc_data)
            bookPackAmount = res_text.json().get("data")[0].get("bookPackAmount")
            expireDate = res_text.json().get("data")[0].get("expireDate")
            inboundDate = res_text.json().get("data")[0].get("inboundDate")
            medicineName = res_text.json().get("data")[0].get("medicineName")
            newCostPrice = res_text.json().get("data")[0].get("newCostPrice")
            packUnit = res_text.json().get("data")[0].get("packUnit")
            retailPrice = res_text.json().get("data")[0].get("retailPrice")
            specs = res_text.json().get("data")[0].get("specs")
            stockId = res_text.json().get("data")[0].get("stockId")
            supplierName = res_text.json().get("data")[0].get("supplierName")
            totalAmount = res_text.json().get("data")[0].get("totalAmount")

        if case_name == "暂存":
            res_text = ApiFactory.get_medicineCheck().medicineCheck(moudle_name=moudle_name, case_name=case_name, request_method=request_method, url=request_url, data=json.loads(req_data),
                                                                   medicineId=medicineId, batchNo=batchNo, supplierId=supplierId, bookPackAmount=bookPackAmount, expireDate=expireDate,
                                                                   inboundDate=inboundDate, medicineName=medicineName, newCostPrice=newCostPrice, packUnit=packUnit,
                                                                   retailPrice=retailPrice, specs=specs, stockId=stockId, supplierName=supplierName, totalAmount=totalAmount)
            logging.info("返回结果：{}".format(res_text.json()))
            assert_common(res_text, msg=exc_data)

        if case_name == "总成本盈亏":
            res_text = ApiFactory.get_medicineCheck().costTotal(moudle_name=moudle_name,
                                                                              case_name=case_name,
                                                                              request_method=request_method,
                                                                              url=request_url,
                                                                              data=json.loads(req_data))
            logging.info("返回结果：{}".format(res_text.json()))
            assert_common(res_text, msg=exc_data)

        if case_name == "盘点列表":
            res_text = ApiFactory.get_medicineCheck().medicineCheckList(moudle_name=moudle_name,
                                                                              case_name=case_name,
                                                                              request_method=request_method,
                                                                              url=request_url,
                                                                              data=json.loads(req_data))
            logging.info("返回结果：{}".format(res_text.json()))
            assert_common(res_text, msg=exc_data)
            id = res_text.json().get("data").get("records")[0].get("id")

        if case_name == "删除":
            res_text = ApiFactory.get_medicineCheck().medicineCheckDelete(moudle_name=moudle_name,
                                                                              case_name=case_name,
                                                                              request_method=request_method,
                                                                              url=request_url,
                                                                              data=json.loads(req_data), id=id)
            logging.info("返回结果：{}".format(res_text.json()))
            assert_common(res_text, msg=exc_data)
