"""
description: 预约列表接口测试用例
time: 2021/12/10
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

@allure.feature("预约管理模块")
class TestPatientRegister:
    curPath = os.path.abspath(os.path.dirname(__file__))
    rootPath = os.path.split(curPath)[0]
    sys.path.append(rootPath)
    data_path = rootPath + r"\data\patientRegister.xls"

    '''
    @allure.severity装饰器按严重性级别来标记case　　　
    执行指定测试用例 --allure-severities blocker
    BLOCKER = 'blocker'　　阻塞缺陷
    CRITICAL = 'critical'　严重缺陷
    NORMAL = 'normal'　　  一般缺陷
    MINOR = 'minor'　　    次要缺陷
    TRIVIAL = 'trivial'　　轻微缺陷　
    '''

    @allure.story("预约列表菜单")
    @allure.severity("NORMAL")
    @allure.description("预约列表查询-挂号-取消挂号")
    @pytest.mark.parametrize("moudle_name,case_name,request_method,request_url,req_data,code,exc_data", read_test_data(data_path, "Sheet1", None, 1, 2, 3, 4, 7, 8, 9))
    def test_patientRegister_case(self, moudle_name, case_name, request_method, request_url, req_data, code, exc_data, clinic_login):
        # logging.info("请求的header：{}".format(api_config.request_header))
        global deptId, jobId, doctorId, registerId, visitOrderId, patientId

        if case_name == "getInfo":
            res_text = ApiFactory.get_patientRegister().getInfo(moudle_name=moudle_name, case_name=case_name, request_method=request_method, url=request_url, data=req_data)
            logging.info("返回结果：{}".format(res_text.json()))
            assert_common(res_text, msg=exc_data)
            deptId = res_text.json().get("user").get("deptId")
            jobId = res_text.json().get("user").get("jobId")
            doctorId = res_text.json().get("user").get("userId")

        elif case_name == "预约列表查询":
            res_text = ApiFactory.get_patientRegister().patientRegisterList(moudle_name=moudle_name, case_name=case_name, request_method=request_method, url=request_url, data=req_data, doctorId=doctorId)
            logging.info("返回结果：{}".format(res_text.json()))
            assert_common(res_text, msg=exc_data)

        elif case_name == "新增预约挂号":
            res_text = ApiFactory.get_patientRegister().registration(moudle_name=moudle_name, case_name=case_name, request_method=request_method, url=request_url, data=json.loads(req_data), deptId=deptId, jobId=jobId, doctorId=doctorId)
            logging.info("返回结果：{}".format(res_text.json()))
            assert_common(res_text, msg=exc_data)
            registerId = res_text.json().get("data").get("registerId")

        elif case_name == "取消挂号":
            res_text = ApiFactory.get_patientRegister().cancelCheck(moudle_name=moudle_name, case_name=case_name, request_method=request_method, url=request_url, data=req_data, registerId=registerId)
            logging.info("返回结果：{}".format(res_text.json()))
            assert_common(res_text, msg=exc_data)