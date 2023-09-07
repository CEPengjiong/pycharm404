"""
description: 供应商接口测试用例
time: 2022/4/13
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

@allure.feature("药房管理模块")
class TestSupplier:
    curPath = os.path.abspath(os.path.dirname(__file__))
    rootPath = os.path.split(curPath)[0]
    sys.path.append(rootPath)
    data_path = rootPath + r"\data\supplier.xls"

    '''
    @allure.severity装饰器按严重性级别来标记case　　　
    执行指定测试用例 --allure-severities blocker
    BLOCKER = 'blocker'　　阻塞缺陷
    CRITICAL = 'critical'　严重缺陷
    NORMAL = 'normal'　　  一般缺陷
    MINOR = 'minor'　　    次要缺陷
    TRIVIAL = 'trivial'　　轻微缺陷　
    '''


    @allure.story("供应商菜单")
    @allure.severity("BLOCKER")
    @allure.description("001-供应商列表-新增供应商-编辑供应商-删除供应商")
    @pytest.mark.parametrize("moudle_name,case_name,request_method,request_url,req_data,code,exc_data", read_test_data(data_path, "供应商", None, 1, 2, 3, 4, 7, 8, 9))
    def test_supplier_case(self, moudle_name, case_name, request_method, request_url, req_data, code, exc_data,clinic_login):

        global supplierId,supplierName,clinicId,createBy,createTime
        if case_name == "供应商列表":
            res_text = ApiFactory.get_supplier().supplierPage(moudle_name=moudle_name, case_name=case_name, request_method=request_method, url=request_url, data=req_data)
            logging.info("返回结果：{}".format(res_text.json()))
            assert_common(res_text, msg=exc_data)

        if case_name == "新增供应商":
            res_text = ApiFactory.get_supplier().supplierAdd(moudle_name=moudle_name, case_name=case_name, request_method=request_method, url=request_url, data=json.loads(req_data))
            logging.info("返回结果：{}".format(res_text[0].json()))
            assert_common(res_text[0], msg=exc_data)
            supplierName = res_text[1]

        if case_name == "根据姓名查询":
            res_text = ApiFactory.get_supplier().nameQuery(moudle_name=moudle_name, case_name=case_name, request_method=request_method, url=request_url, data=req_data, supplierName=supplierName)
            logging.info("返回结果：{}".format(res_text.json()))
            assert_common(res_text, msg=exc_data)
            supplierId = res_text.json().get("data").get("records")[0].get("supplierId")

        if case_name == "编辑供应商":
            res_text = ApiFactory.get_supplier().supplierEdit(moudle_name=moudle_name, case_name=case_name, request_method=request_method, url=request_url, data=req_data, supplierId=supplierId)
            logging.info("返回结果：{}".format(res_text.json()))
            assert_common(res_text, msg=exc_data)
            clinicId = res_text.json().get("data").get("clinicId")
            createBy = res_text.json().get("data").get("createBy")
            createTime = res_text.json().get("data").get("createTime")

        if case_name == "确认编辑":
            res_text = ApiFactory.get_supplier().editConfirm(moudle_name=moudle_name, case_name=case_name, request_method=request_method, url=request_url, data=json.loads(req_data), supplierId=supplierId,supplierName=supplierName,clinicId=clinicId,createBy=createBy,createTime=createTime)
            logging.info("返回结果：{}".format(res_text.json()))
            assert_common(res_text, msg=exc_data)

        if case_name == "删除供应商":
            res_text = ApiFactory.get_supplier().supplierDelete(moudle_name=moudle_name, case_name=case_name, request_method=request_method, url=request_url, data=req_data, supplierId=supplierId)
            logging.info("返回结果：{}".format(res_text.json()))
            assert_common(res_text, msg=exc_data)



