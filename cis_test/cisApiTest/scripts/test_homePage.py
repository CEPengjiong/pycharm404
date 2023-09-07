"""
description: 首页接口测试用例
time: 2022/3/11
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


@allure.feature("首页")
class TestHomePage:
    curPath = os.path.abspath(os.path.dirname(__file__))
    rootPath = os.path.split(curPath)[0]
    sys.path.append(rootPath)
    data_path = rootPath + r"\data\homePage.xls"

    '''
    @allure.severity装饰器按严重性级别来标记case　　　
    执行指定测试用例 --allure-severities blocker
    BLOCKER = 'blocker'　　阻塞缺陷
    CRITICAL = 'critical'　严重缺陷
    NORMAL = 'normal'　　  一般缺陷
    MINOR = 'minor'　　    次要缺陷
    TRIVIAL = 'trivial'　　轻微缺陷　
    '''


    @allure.story("首页")
    @allure.severity("BLOCKER")
    @allure.description("001首页")
    @pytest.mark.parametrize("moudle_name,case_name,request_method,request_url,req_data,code,exc_data", read_test_data(data_path, "Sheet1", None, 1, 2, 3, 4, 7, 8, 9))
    def test_homePage_case(self, moudle_name, case_name, request_method, request_url, req_data, code, exc_data,clinic_login):

        res_text = ApiFactory.get_homePage().homePage(moudle_name=moudle_name, case_name=case_name,
                                                              request_method=request_method, url=request_url,
                                                              data=json.loads(req_data))
        logging.info("返回结果：{}".format(res_text.json()))
        assert_common(res_text, msg=exc_data)

