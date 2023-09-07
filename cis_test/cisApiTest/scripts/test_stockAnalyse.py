"""
description: 库存分析接口测试用例
time: 2022/4/13
author: chenling
"""
import logging
import allure
import pytest
import os
import sys
from utils.assert_common import assert_common
from utils.ReadTabDataUtils import read_test_data
from api.api_factory import ApiFactory
import api_config

@allure.feature("药房管理模块")
class TestStockAnalyse:
    curPath = os.path.abspath(os.path.dirname(__file__))
    rootPath = os.path.split(curPath)[0]
    sys.path.append(rootPath)
    data_path = rootPath + r"\data\stockAnalyse.xls"

    '''
    @allure.severity装饰器按严重性级别来标记case　　　
    执行指定测试用例 --allure-severities blocker
    BLOCKER = 'blocker'　　阻塞缺陷
    CRITICAL = 'critical'　严重缺陷
    NORMAL = 'normal'　　  一般缺陷
    MINOR = 'minor'　　    次要缺陷
    TRIVIAL = 'trivial'　　轻微缺陷　
    '''


    @allure.story("库存分析菜单")
    @allure.severity("BLOCKER")
    @allure.description("001近效期预警药品查询-库存预警药品查询-过期药品查询")
    @pytest.mark.parametrize("moudle_name,case_name,request_method,request_url,req_data,code,exc_data", read_test_data(data_path, "库存分析", None, 1, 2, 3, 4, 7, 8, 9))
    def test_stockAnalyse_case(self, moudle_name, case_name, request_method, request_url, req_data, code, exc_data,clinic_login):

        res_text = ApiFactory.get_stockAnalyse().page(moudle_name=moudle_name, case_name=case_name, request_method=request_method, url=request_url, data=req_data)
        logging.info("返回结果：{}".format(res_text.json()))
        assert_common(res_text, msg=exc_data)

