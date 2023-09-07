"""
description: 供应商统计接口测试用例
time: 2022/06/13
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

@allure.feature("经营分析模块")
class TestSupplierStatistics:
    curPath = os.path.abspath(os.path.dirname(__file__))
    rootPath = os.path.split(curPath)[0]
    sys.path.append(rootPath)
    data_path = rootPath + r"\data\supplierStatistics.xls"

    '''
    @allure.severity装饰器按严重性级别来标记case　　　
    执行指定测试用例 --allure-severities blocker
    BLOCKER = 'blocker'　　阻塞缺陷
    CRITICAL = 'critical'　严重缺陷
    NORMAL = 'normal'　　  一般缺陷
    MINOR = 'minor'　　    次要缺陷
    TRIVIAL = 'trivial'　　轻微缺陷　
    '''

    @allure.story("库存统计菜单")
    @allure.severity("NORMAL")
    @allure.description("供应商列表-详情")
    @pytest.mark.parametrize("moudle_name,case_name,request_method,request_url,req_data,code,exc_data", read_test_data(data_path, "供应商统计", None, 1, 2, 3, 4, 7, 8, 9))
    def test_supplierStatistics_case(self, moudle_name, case_name, request_method, request_url, req_data, code, exc_data, clinic_login):
        # logging.info("请求的header：{}".format(api_config.request_header))
        global supplierId
        if case_name == "供应商统计列表":
            res_text = ApiFactory.get_supplierStatistics().supplierStatistics(moudle_name=moudle_name, case_name=case_name, request_method=request_method, url=request_url, data=req_data)
            logging.info("返回结果：{}".format(res_text.json()))
            assert_common(res_text, msg=exc_data)
            supplierId = res_text.json().get("data").get("records")[0].get("supplierId")
        if case_name == "详情":
            res_text = ApiFactory.get_supplierStatistics().supplierInfo(moudle_name=moudle_name, case_name=case_name, request_method=request_method, url=request_url, data=req_data, supplierId=supplierId)
            logging.info("返回结果：{}".format(res_text.json()))
            assert_common(res_text, msg=exc_data)