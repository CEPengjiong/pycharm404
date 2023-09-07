"""
description: 药品管理接口测试用例
time: 2022/3/14
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


@allure.feature("药房管理-药品管理")
class TestMedicineManagement:
    curPath = os.path.abspath(os.path.dirname(__file__))
    rootPath = os.path.split(curPath)[0]
    sys.path.append(rootPath)
    data_path = rootPath + r"\data\medicineManagement.xls"

    '''
    @allure.severity装饰器按严重性级别来标记case　　　
    执行指定测试用例 --allure-severities blocker
    BLOCKER = 'blocker'　　阻塞缺陷
    CRITICAL = 'critical'　严重缺陷
    NORMAL = 'normal'　　  一般缺陷
    MINOR = 'minor'　　    次要缺陷
    TRIVIAL = 'trivial'　　轻微缺陷　
    '''


    @allure.story("药品管理")
    @allure.severity("BLOCKER")
    @allure.description("001-药品列表查询-新增药品-中心药品库搜索-编辑药品-删除")
    @pytest.mark.parametrize("moudle_name,case_name,request_method,request_url,req_data,code,exc_data", read_test_data(data_path, "新增药品", None, 1, 2, 3, 4, 7, 8, 9))
    def test_medicineManagement_case(self, moudle_name, case_name, request_method, request_url, req_data, code, exc_data, clinic_login):

        global medicineId,clinicId,createBy,createTime,effectiveTime



        if case_name == "获取药品信息":
            res_text = ApiFactory.get_medicineManagement().getMedicineInfo(moudle_name=moudle_name,
                                                                              case_name=case_name,
                                                                              request_method=request_method,
                                                                              url=request_url,
                                                                              data=json.loads(req_data),medicineId=medicineId)
            logging.info("返回结果：{}".format(res_text.json()))
            assert_common(res_text, msg=exc_data)
            clinicId = res_text.json().get("data").get("clinicId")
            createBy = res_text.json().get("data").get("createBy")
            createTime = res_text.json().get("data").get("createTime")
            effectiveTime = res_text.json().get("data").get("effectiveTime")
        elif case_name == "编辑药品":
            res_text = ApiFactory.get_medicineManagement().medicineInfo(moudle_name=moudle_name,
                                                                              case_name=case_name,
                                                                              request_method=request_method,
                                                                              url=request_url,
                                                                              data=json.loads(req_data), medicineId=medicineId, clinicId=clinicId, createBy=createBy, createTime=createTime, effectiveTime=effectiveTime)
            logging.info("返回结果：{}".format(res_text.json()))
            assert_common(res_text, msg=exc_data)
        elif case_name == "删除药品":
            res_text = ApiFactory.get_medicineManagement().medicineDelete(moudle_name=moudle_name,
                                                                              case_name=case_name,
                                                                              request_method=request_method,
                                                                              url=request_url,
                                                                              data=json.loads(req_data),medicineId=medicineId)
            logging.info("返回结果：{}".format(res_text.json()))
            assert_common(res_text, msg=exc_data)
        else:
            res_text = ApiFactory.get_medicineManagement().medicineManagement(moudle_name=moudle_name,
                                                                              case_name=case_name,
                                                                              request_method=request_method,
                                                                              url=request_url,
                                                                              data=json.loads(req_data))
            logging.info("返回结果：{}".format(res_text.json()))
            assert_common(res_text, msg=exc_data)
            if case_name == "根据药品名称查询":
                medicineId = res_text.json().get("data").get("records")[0].get("medicineId")

    @allure.story("药品管理")
    @allure.severity("BLOCKER")
    @allure.description("002-云药房查询-新增药品-拆零-删除")
    @pytest.mark.parametrize("moudle_name,case_name,request_method,request_url,req_data,code,exc_data", read_test_data(data_path, "云药房", None, 1, 2, 3, 4, 7, 8, 9))
    def test_cloudMedicineManagement_case(self, moudle_name, case_name, request_method, request_url, req_data, code, exc_data, clinic_login):

        global approvalNumber,barCode,code2,formulation,insuranceCode,manufacturer,medicareFlag,medicineMinimumNumber,medicineMinimumUnit,medicinePreparationUnit,name,packUnit,province,specs,retailPrice,medicineId



        if case_name == "导入":
            res_text = ApiFactory.get_medicineManagement().saveBatch(moudle_name=moudle_name, case_name=case_name, request_method=request_method, url=request_url, data=json.loads(req_data),
                                                                     approvalNumber=approvalNumber, barCode=barCode, code2=code2, formulation=formulation, insuranceCode=insuranceCode, manufacturer=manufacturer,
                                                                     medicareFlag=medicareFlag, medicineMinimumNumber=medicineMinimumNumber, medicineMinimumUnit=medicineMinimumUnit, medicinePreparationUnit=medicinePreparationUnit,
                                                                     name=name, packUnit=packUnit, province=province, specs=specs, retailPrice=retailPrice)
            logging.info("返回结果：{}".format(res_text.json()))
            assert_common(res_text, msg=exc_data)

        if case_name == "根据药品名称查询":
            res_text = ApiFactory.get_medicineManagement().drugNameQuery(moudle_name=moudle_name,
                                                                              case_name=case_name,
                                                                              request_method=request_method,
                                                                              url=request_url,
                                                                              data=json.loads(req_data), name=name)
            logging.info("返回结果：{}".format(res_text.json()))
            assert_common(res_text, msg=exc_data)
            medicineId = res_text.json().get("data").get("records")[0].get("medicineId")

        if case_name == "删除药品":
            res_text = ApiFactory.get_medicineManagement().medicineDelete(moudle_name=moudle_name,
                                                                              case_name=case_name,
                                                                              request_method=request_method,
                                                                              url=request_url,
                                                                              data=json.loads(req_data),medicineId=medicineId)
            logging.info("返回结果：{}".format(res_text.json()))
            assert_common(res_text, msg=exc_data)

        if case_name == "拆零":
            res_text = ApiFactory.get_medicineManagement().updateZero(moudle_name=moudle_name,
                                                                              case_name=case_name,
                                                                              request_method=request_method,
                                                                              url=request_url,
                                                                              data=json.loads(req_data), medicineId=medicineId)
            logging.info("返回结果：{}".format(res_text.json()))

        if case_name == "云药房查询":
            res_text = ApiFactory.get_medicineManagement().medicineManagement(moudle_name=moudle_name,
                                                                              case_name=case_name,
                                                                              request_method=request_method,
                                                                              url=request_url,
                                                                              data=json.loads(req_data))
            logging.info("返回结果：{}".format(res_text.json()))
            assert_common(res_text, msg=exc_data)
            approvalNumber = res_text.json().get("data").get("records")[0].get("approvalNumber")
            barCode = res_text.json().get("data").get("records")[0].get("barCode")
            code2 = res_text.json().get("data").get("records")[0].get("code")
            formulation = res_text.json().get("data").get("records")[0].get("formulation")
            insuranceCode = res_text.json().get("data").get("records")[0].get("insuranceCode")
            manufacturer = res_text.json().get("data").get("records")[0].get("manufacturer")
            medicareFlag = res_text.json().get("data").get("records")[0].get("medicareFlag")
            medicineMinimumNumber = res_text.json().get("data").get("records")[0].get("medicineMinimumNumber")
            medicineMinimumUnit = res_text.json().get("data").get("records")[0].get("medicineMinimumUnit")
            medicinePreparationUnit = res_text.json().get("data").get("records")[0].get("medicinePreparationUnit")
            name = res_text.json().get("data").get("records")[0].get("name")
            packUnit = res_text.json().get("data").get("records")[0].get("packUnit")
            province = res_text.json().get("data").get("records")[0].get("province")
            retailPrice = res_text.json().get("data").get("records")[0].get("retailPrice")
            specs = res_text.json().get("data").get("records")[0].get("specs")

