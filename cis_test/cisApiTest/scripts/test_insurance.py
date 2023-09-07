# -*- coding: utf-8 -*-
# @Time    : 2022/9/13 10:28
# @Author  : PengJiong
# @Email   : 18390050274@qq.com
# @File    : test_insurance.py
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

@allure.feature("医保管理")
class TestClinicDailyInfo:
    curPath = os.path.abspath(os.path.dirname(__file__))
    rootPath = os.path.split(curPath)[0]
    sys.path.append(rootPath)
    data_path = rootPath + r"\data\insurance.xls"

    '''
    @allure.severity装饰器按严重性级别来标记case　　　
    执行指定测试用例 --allure-severities blocker
    BLOCKER = 'blocker'　　阻塞缺陷
    CRITICAL = 'critical'　严重缺陷
    NORMAL = 'normal'　　  一般缺陷
    MINOR = 'minor'　　    次要缺陷
    TRIVIAL = 'trivial'　　轻微缺陷　
    '''


    @allure.story("今日日报")
    @allure.severity("BLOCKER")
    @allure.description("001医保管理-医保结算单据")
    @pytest.mark.parametrize("moudle_name,case_name,request_method,request_url,req_data,code,exc_data", read_test_data(data_path, "医保管理", None, 1, 2, 3, 4, 7, 8, 9))
    def test_clinicDailyInfo_case(self, moudle_name, case_name, request_method, request_url, req_data, code, exc_data, clinic_login):
        global deptId, jobId, doctorId, registerId, visitOrderId, patientId, batchNo, total, pieceTotal, clinicId

        if case_name == "机构信息获取":
            res_text = ApiFactory.get_insurance().getinfo(moudle_name=moudle_name, case_name=case_name,
                                                                request_method=request_method, url=request_url,
                                                                data=req_data)
            logging.info("返回结果：{}".format(res_text.json()))
            assert_common(res_text, msg=exc_data)
            clinicId = res_text.json().get("data").get("clinicId")

        if case_name == "医保结算单据":
            res_text = ApiFactory.get_insurance().insurance(moudle_name=moudle_name, case_name=case_name,
                                                                request_method=request_method, url=request_url,
                                                                data=req_data, clinicId=clinicId)
            logging.info("返回结果:{}".format(res_text.json()))
            assert_common(res_text, msg=exc_data)

        if case_name == "医保三目匹配数据统计":
            res_text = ApiFactory.get_insurance().countMedicare(moudle_name=moudle_name, case_name=case_name,
                                                            request_method=request_method, url=request_url,
                                                            data=req_data)
            logging.info("返回结果:{}".format(res_text.json()))
            assert_common(res_text, msg=exc_data)

        if case_name == "医保三目匹配数据":
            res_text = ApiFactory.get_insurance().listByMedicalCare(moudle_name=moudle_name, case_name=case_name,
                                                            request_method=request_method, url=request_url,
                                                            data=req_data)
            logging.info("返回结果:{}".format(res_text.json()))
            assert_common(res_text, msg=exc_data)

        if case_name == "医保服务匹配数据":
            res_text = ApiFactory.get_insurance().clinicExtra(moudle_name=moudle_name, case_name=case_name,
                                                            request_method=request_method, url=request_url,
                                                            data=req_data)
            logging.info("返回结果:{}".format(res_text.json()))
            assert_common(res_text, msg=exc_data)

        if case_name == "医保服务匹配数据目录外":
            res_text = ApiFactory.get_insurance().medicare(moudle_name=moudle_name, case_name=case_name,
                                                            request_method=request_method, url=request_url,
                                                            data=req_data)
            logging.info("返回结果:{}".format(res_text.json()))
            assert_common(res_text, msg=exc_data)

        if case_name == "医保对账":
            res_text = ApiFactory.get_insurance().drugSettleBill(moudle_name=moudle_name, case_name=case_name,
                                                            request_method=request_method, url=request_url,
                                                            data=req_data, clinicId=clinicId)
            logging.info("返回结果:{}".format(res_text.json()))
            assert_common(res_text, msg=exc_data)

        if case_name == "对账记录":
            res_text = ApiFactory.get_insurance().drugSettleBillpage(moudle_name=moudle_name, case_name=case_name,
                                                            request_method=request_method, url=request_url,
                                                            data=req_data, clinicId=clinicId)
            logging.info("返回结果:{}".format(res_text.json()))
            assert_common(res_text, msg=exc_data)

        if case_name == "清算申请与撤销":
            res_text = ApiFactory.get_insurance().clrPage(moudle_name=moudle_name, case_name=case_name,
                                                            request_method=request_method, url=request_url,
                                                            data=req_data, clinicId=clinicId)
            logging.info("返回结果:{}".format(res_text.json()))
            assert_common(res_text, msg=exc_data)

        if case_name == "医保字典查询1":
            res_text = ApiFactory.get_insurance().dictionary1(moudle_name=moudle_name, case_name=case_name,
                                                            request_method=request_method, url=request_url,
                                                            data=req_data)
            logging.info("返回结果:{}".format(res_text.json()))
            assert_common(res_text, msg=exc_data)

        if case_name == "医保字典查询2":
            res_text = ApiFactory.get_insurance().dictionary2(moudle_name=moudle_name, case_name=case_name,
                                                            request_method=request_method, url=request_url,
                                                            data=req_data)
            logging.info("返回结果:{}".format(res_text.json()))
            assert_common(res_text, msg=exc_data)

        if case_name == "医保字典查询3":
            res_text = ApiFactory.get_insurance().dictionary3(moudle_name=moudle_name, case_name=case_name,
                                                            request_method=request_method, url=request_url,
                                                            data=req_data)
            logging.info("返回结果:{}".format(res_text.json()))
            assert_common(res_text, msg=exc_data)

        if case_name == "进销存管理列表":
            res_text = ApiFactory.get_insurance().queryUploadPage(moudle_name=moudle_name, case_name=case_name,
                                                            request_method=request_method, url=request_url,
                                                            data=req_data, clinicId=clinicId)
            logging.info("返回结果:{}".format(res_text.json()))
            assert_common(res_text, msg=exc_data)