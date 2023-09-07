# -*- coding: utf-8 -*-
# @Time    : 2022/4/15 15:57
# @Author  : PengJiong
# @Email   : 18390050274@qq.com
# @File    : test_HuanzheGuanli.py

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

@allure.feature("患者管理")
class TestClinicDailyInfo:
    curPath = os.path.abspath(os.path.dirname(__file__))
    rootPath = os.path.split(curPath)[0]
    sys.path.append(rootPath)
    data_path = rootPath + r"\data\HuanzheGuanli.xls"

    '''
    @allure.severity装饰器按严重性级别来标记case　　　
    执行指定测试用例 --allure-severities blocker
    BLOCKER = 'blocker'　　阻塞缺陷
    CRITICAL = 'critical'　严重缺陷
    NORMAL = 'normal'　　  一般缺陷
    MINOR = 'minor'　　    次要缺陷
    TRIVIAL = 'trivial'　　轻微缺陷　
    '''


    @allure.story("患者管理")
    @allure.severity("BLOCKER")
    @allure.description("001患者管理-查询")
    @pytest.mark.parametrize("moudle_name,case_name,request_method,request_url,req_data,code,exc_data", read_test_data(data_path, "今日日报", None, 1, 2, 3, 4, 7, 8, 9))
    def test_HuanzheGuanli_case(self, moudle_name, case_name, request_method, request_url, req_data, code, exc_data, clinic_login):
        global deptId, jobId, doctorId, registerId, visitOrderId, patientId, batchNo, total, pieceTotal, clinicId, clinicErpCode, doctorId


        if case_name == "诊所信息获取":
            res_text = ApiFactory.get_HuanzheGuanli().getinfo(moudle_name=moudle_name, case_name=case_name,
                                                                request_method=request_method, url=request_url,
                                                                data=req_data)
            logging.info("返回结果：{}".format(res_text.json()))
            assert_common(res_text, msg=exc_data)
            # clinicId = res_text.json().get("data").get("clinicId")
            clinicErpCode = res_text.json().get("clinicErpCode")

        if case_name == "病人":
            res_text = ApiFactory.get_HuanzheGuanli().isExist(moudle_name=moudle_name, case_name=case_name,
                                                                    request_method=request_method, url=request_url,
                                                                    data=req_data)
            logging.info("返回结果：{}".format(res_text.json()))
            assert_common(res_text, msg=exc_data)

        if case_name == "访问者页面":
            res_text = ApiFactory.get_HuanzheGuanli().visitOrderPage(moudle_name=moudle_name, case_name=case_name,
                                                                    request_method=request_method, url=request_url,
                                                                    data=req_data)
            logging.info("返回结果：{}".format(res_text.json()))
            assert_common(res_text, msg=exc_data)
            patientId = res_text.json().get("data").get("records")[0].get("patientId")
            doctorId = res_text.json().get("data").get("records")[0].get("doctorId")

        if case_name == "用户列表":
            res_text = ApiFactory.get_HuanzheGuanli().userlist(moudle_name=moudle_name, case_name=case_name,
                                                                    request_method=request_method, url=request_url,
                                                                    data=req_data)
            logging.info("返回结果：{}".format(res_text.json()))
            assert_common(res_text, msg=exc_data)

        if case_name == "文件详细信息":
            res_text = ApiFactory.get_HuanzheGuanli().fileDetails(moudle_name=moudle_name, case_name=case_name,
                                                                    request_method=request_method, url=request_url,
                                                                    data=req_data, patientId=patientId)
            logging.info("返回结果：{}".format(res_text.json()))
            assert_common(res_text, msg=exc_data)

        # if case_name == "门诊病例":
        #     res_text = ApiFactory.get_HuanzheGuanli().outpatientRecordsPage(moudle_name=moudle_name, case_name=case_name,
        #                                                             request_method=request_method, url=request_url,
        #                                                             data=req_data, patientId=patientId)
        #     logging.info("返回结果：{}".format(res_text.json()))
        #     assert_common(res_text, msg=exc_data)

        if case_name == "患者轨迹页面":
            res_text = ApiFactory.get_HuanzheGuanli().patientTrajectoryPage(moudle_name=moudle_name, case_name=case_name,
                                                                                request_method=request_method, url=request_url,
                                                                                data=req_data, patientId=patientId)
            logging.info("返回结果：{}".format(res_text.json()))
            assert_common(res_text, msg=exc_data)

        if case_name == "零售记录":
            res_text = ApiFactory.get_HuanzheGuanli().saleOrders(moudle_name=moudle_name, case_name=case_name,
                                                                    request_method=request_method, url=request_url,
                                                                    data=req_data, patientId=patientId)
            logging.info("返回结果：{}".format(res_text.json()))
            assert_common(res_text, msg=exc_data)

        if case_name == "随访记录":
            res_text = ApiFactory.get_HuanzheGuanli().page(moudle_name=moudle_name, case_name=case_name,
                                                            request_method=request_method, url=request_url,
                                                            data=req_data, patientId=patientId)
            logging.info("返回结果：{}".format(res_text.json()))
            assert_common(res_text, msg=exc_data)

        if case_name == "随访管理":
            res_text = ApiFactory.get_HuanzheGuanli().patienfollowuppage(moudle_name=moudle_name, case_name=case_name,
                                                                            request_method=request_method, url=request_url,
                                                                            data=req_data)
            logging.info("返回结果：{}".format(res_text.json()))
            assert_common(res_text, msg=exc_data)

        if case_name == "新增随访":
            res_text = ApiFactory.get_HuanzheGuanli().patienfollowup(moudle_name=moudle_name, case_name=case_name,
                                                                        request_method=request_method, url=request_url,
                                                                        data=json.loads(req_data), patientId=patientId, doctorId=doctorId)
            logging.info("返回结果：{}".format(res_text.json()))
            assert_common(res_text, msg=exc_data)