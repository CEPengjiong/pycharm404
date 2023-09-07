"""
description: 接诊列表接口测试用例
time: 2021/11/24
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
class TestSelRegisterInfoList:
    curPath = os.path.abspath(os.path.dirname(__file__))
    rootPath = os.path.split(curPath)[0]
    sys.path.append(rootPath)
    data_path = rootPath + r"\data\selRegisterInfoList.xls"

    '''
    @allure.severity装饰器按严重性级别来标记case　　　
    执行指定测试用例 --allure-severities blocker
    BLOCKER = 'blocker'　　阻塞缺陷
    CRITICAL = 'critical'　严重缺陷
    NORMAL = 'normal'　　  一般缺陷
    MINOR = 'minor'　　    次要缺陷
    TRIVIAL = 'trivial'　　轻微缺陷　
    '''

    @allure.story("接诊列表菜单")
    @allure.severity("BLOCKER")
    @allure.description("接诊列表查询-新增随访-查看详情")
    @pytest.mark.parametrize("moudle_name,case_name,request_method,request_url,req_data,code,exc_data", read_test_data(data_path, "Sheet1", None, 1, 2, 3, 4, 7, 8, 9))
    def test_selRegisterInfoList_case(self, moudle_name, case_name, request_method, request_url, req_data, code, exc_data, clinic_login):
        # logging.info("请求的header：{}".format(api_config.request_header))
        global doctorId, visitOrderId, patientId

        if case_name == "接诊列表查询":
            res_text = ApiFactory.get_selRegisterInfoList().listQuery(moudle_name=moudle_name, case_name=case_name, request_method=request_method, url=request_url, data=req_data)
            logging.info("返回结果：{}".format(res_text.json()))
            assert_common(res_text, msg=exc_data)
            patientId = res_text.json().get("data").get("records")[0].get("patientId")
            doctorId = res_text.json().get("data").get("records")[0].get("doctorId")
            visitOrderId = res_text.json().get("data").get("records")[0].get("visitOrderId")

        if case_name == "新增随访":
            res_text = ApiFactory.get_selRegisterInfoList().patienfollowup(moudle_name=moudle_name, case_name=case_name, request_method=request_method, url=request_url, data=json.loads(req_data), patientId=patientId, doctorId=doctorId)
            logging.info("返回结果：{}".format(res_text.json()))
            assert_common(res_text, msg=exc_data)

        if case_name == "查看详情":
            res_text = ApiFactory.get_selRegisterInfoList().particulars(moudle_name=moudle_name, case_name=case_name, request_method=request_method, url=request_url, data=req_data, visitOrderId=visitOrderId)
            logging.info("返回结果：{}".format(res_text.json()))
            assert_common(res_text, msg=exc_data)