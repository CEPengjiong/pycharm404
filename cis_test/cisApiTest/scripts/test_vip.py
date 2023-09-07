import json
import logging
import allure
import pytest
import os
import sys
from utils.assert_common import assert_common
from utils.ReadTabDataUtils import read_test_data
from api.api_factory import ApiFactory
from utils.random_phone import random_name,random_phone
import api_config

phone = random_phone()
name = random_name()

@allure.feature("会员管理")
class TestClinicDailyInfo:
    curPath = os.path.abspath(os.path.dirname(__file__))
    rootPath = os.path.split(curPath)[0]
    sys.path.append(rootPath)
    data_path = rootPath + r"\data\vip.xls"

    '''
    @allure.severity装饰器按严重性级别来标记case　　　
    执行指定测试用例 --allure-severities blocker
    BLOCKER = 'blocker'　　阻塞缺陷
    CRITICAL = 'critical'　严重缺陷
    NORMAL = 'normal'　　  一般缺陷
    MINOR = 'minor'　　    次要缺陷
    TRIVIAL = 'trivial'　　轻微缺陷　
    '''


    @allure.story("会员管理")
    @allure.severity("BLOCKER")
    @allure.description("001会员管理-会员列表")
    @pytest.mark.parametrize("moudle_name,case_name,request_method,request_url,req_data,code,exc_data", read_test_data(data_path, "会员数据", None, 1, 2, 3, 4, 7, 8, 9))
    def test_vip_case(self, moudle_name, case_name, request_method, request_url, req_data, code, exc_data, clinic_login):
        global deptId, jobId, doctorId, registerId, visitOrderId, patientId, batchNo, total, pieceTotal, clinicId, clinicErpCode, doctorId, phone, name, vipId


        # if case_name == "诊所信息获取":
        #     res_text = ApiFactory.get_HuanzheGuanli().getinfo(moudle_name=moudle_name, case_name=case_name,
        #                                                         request_method=request_method, url=request_url,
        #                                                         data=req_data)
        #     logging.info("返回结果：{}".format(res_text.json()))
        #     assert_common(res_text, msg=exc_data)
        #     # clinicId = res_text.json().get("data").get("clinicId")
        #     clinicErpCode = res_text.json().get("clinicErpCode")

        if case_name == "会员列表":
            res_text = ApiFactory.get_vip().vippage(moudle_name=moudle_name, case_name=case_name,
                                                                    request_method=request_method, url=request_url,
                                                                    data=req_data)
            logging.info("返回结果：{}".format(res_text.json()))
            assert_common(res_text, msg=exc_data)

        if case_name == "新增会员":
            res_text = ApiFactory.get_vip().vipvip(moudle_name=moudle_name, case_name=case_name,
                                                                    request_method=request_method, url=request_url,
                                                                    data=json.loads(req_data), phone=phone, name=name)
            logging.info("返回结果：{}".format(res_text.json()))
            # print(phone)
            # print(name)
            assert_common(res_text, msg=exc_data)

        if case_name == "取得新增会员Id":
            res_text = ApiFactory.get_vip().vippage(moudle_name=moudle_name, case_name=case_name,
                                                                    request_method=request_method, url=request_url,
                                                                    data=req_data)
            logging.info("返回结果：{}".format(res_text.json()))
            assert_common(res_text, msg=exc_data)
            vipId = res_text.json().get("data").get("records")[0].get("vipId")

        if case_name == "会员详情":
            res_text = ApiFactory.get_vip().logpage(moudle_name=moudle_name, case_name=case_name,
                                                                    request_method=request_method, url=request_url,
                                                                    data=req_data, vipId=vipId)
            logging.info("返回结果：{}".format(res_text.json()))
            assert_common(res_text, msg=exc_data)

        if case_name == "会员设置":
            res_text = ApiFactory.get_vip().setUpInfo(moudle_name=moudle_name, case_name=case_name,
                                                                    request_method=request_method, url=request_url,
                                                                    data=req_data)
            logging.info("返回结果：{}".format(res_text.json()))
            assert_common(res_text, msg=exc_data)

        # if case_name == "会员设置保存":
        #     res_text = ApiFactory.get_vip().setUp(moudle_name=moudle_name, case_name=case_name,
        #                                                             request_method=request_method, url=request_url,
        #                                                             data=req_data)
        #     logging.info("返回结果：{}".format(res_text.json()))
        #     assert_common(res_text, msg=exc_data)
