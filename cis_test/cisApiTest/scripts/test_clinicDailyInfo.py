# -*- coding: utf-8 -*-
# @Time    : 2022/3/24 16:46
# @Author  : PengJiong
# @Email   : 18390050274@qq.com
# @File    : test_clinicDailyInfo.py.py

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

@allure.feature("经营分析")
class TestClinicDailyInfo:
    curPath = os.path.abspath(os.path.dirname(__file__))
    rootPath = os.path.split(curPath)[0]
    sys.path.append(rootPath)
    data_path = rootPath + r"\data\clinicDailyInfo.xls"

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
    @allure.description("001经营分析-报表查询")
    @pytest.mark.parametrize("moudle_name,case_name,request_method,request_url,req_data,code,exc_data", read_test_data(data_path, "今日日报", None, 1, 2, 3, 4, 7, 8, 9))
    def test_clinicDailyInfo_case(self, moudle_name, case_name, request_method, request_url, req_data, code, exc_data, clinic_login):
        global deptId, jobId, doctorId, registerId, visitOrderId, patientId, batchNo, total, pieceTotal, clinicId

        if case_name == "机构信息获取":
            res_text = ApiFactory.get_clinicDailyInfo().getinfo(moudle_name=moudle_name, case_name=case_name,
                                                                request_method=request_method, url=request_url,
                                                                data=req_data)
            logging.info("返回结果：{}".format(res_text.json()))
            assert_common(res_text, msg=exc_data)
            clinicId = res_text.json().get("data").get("clinicId")

        if case_name == "今日日报":
            res_text = ApiFactory.get_clinicDailyInfo().clinicDailInfo(moudle_name=moudle_name, case_name=case_name,
                                                                    request_method=request_method, url=request_url,
                                                                    data=req_data)
            logging.info("返回结果：{}".format(res_text.json()))
            assert_common(res_text, msg=exc_data)

        if case_name == "时间筛选查询":
            res_text = ApiFactory.get_clinicDailyInfo().tClinicDailyShare(moudle_name=moudle_name, case_name=case_name,
                                                                    request_method=request_method, url=request_url,
                                                                    data=req_data)
            logging.info("返回结果：{}".format(res_text.json()))
            assert_common(res_text, msg=exc_data)

        if case_name == "查看趋势图":
            res_text = ApiFactory.get_clinicDailyInfo().tClinicDailyPage(moudle_name=moudle_name, case_name=case_name,
                                                                    request_method=request_method, url=request_url,
                                                                    data=req_data)
            logging.info("返回结果：{}".format(res_text.json()))
            assert_common(res_text, msg=exc_data)

        if case_name == "收费明细表":
            res_text = ApiFactory.get_clinicDailyInfo().clinicdeptlist(moudle_name=moudle_name, case_name=case_name,
                                                                    request_method=request_method, url=request_url,
                                                                    data=req_data)
            logging.info("返回结果：{}".format(res_text.json()))
            assert_common(res_text, msg=exc_data)

        if case_name == "费用统计":
            res_text = ApiFactory.get_clinicDailyInfo().chargeStatistics(moudle_name=moudle_name, case_name=case_name,
                                                                    request_method=request_method, url=request_url,
                                                                    data=req_data)
            logging.info("返回结果：{}".format(res_text.json()))
            assert_common(res_text, msg=exc_data)

        if case_name == "收费详情":
            res_text = ApiFactory.get_clinicDailyInfo().chargeDetails(moudle_name=moudle_name, case_name=case_name,
                                                                         request_method=request_method, url=request_url,
                                                                         data=req_data)
            logging.info("返回结果：{}".format(res_text.json()))
            assert_common(res_text, msg=exc_data)

        if case_name == "销售明细":
            res_text = ApiFactory.get_clinicDailyInfo().getTVisitOrderDetailPage(moudle_name=moudle_name, case_name=case_name,
                                                                         request_method=request_method, url=request_url,
                                                                         data=req_data)
            logging.info("返回结果：{}".format(res_text.json()))
            assert_common(res_text, msg=exc_data)

        if case_name == "科室统计":
            res_text = ApiFactory.get_clinicDailyInfo().departmentStatistics(moudle_name=moudle_name, case_name=case_name,
                                                                         request_method=request_method, url=request_url,
                                                                         data=req_data)
            logging.info("返回结果：{}".format(res_text.json()))
            assert_common(res_text, msg=exc_data)

        if case_name == "医生业绩统计":
            res_text = ApiFactory.get_clinicDailyInfo().performanceStatistics(moudle_name=moudle_name, case_name=case_name,
                                                                         request_method=request_method, url=request_url,
                                                                         data=json.loads(req_data), clinicId=clinicId)
            logging.info("返回结果：{}".format(res_text.json()))
            assert_common(res_text, msg=exc_data)

    @allure.story("门诊日志")
    @allure.severity("BLOCKER")
    @allure.description("001经营分析-门诊日志，库存统计，供应商统计")
    @pytest.mark.parametrize("moudle_name,case_name,request_method,request_url,req_data,code,exc_data",read_test_data(data_path, "今日日报", None, 1, 2, 3, 4, 7, 8, 9))
    def test_clinicDailyInfo1_case(self, moudle_name, case_name, request_method, request_url, req_data, code, exc_data, clinic_login):
        global deptId, jobId, doctorId, registerId, visitOrderId, patientId, batchNo, total, pieceTotal, clinicId

        # if case_name == "用户信息获取":
        #     res_text = ApiFactory.get_clinicDailyInfo().getuserlist(moudle_name=moudle_name, case_name=case_name,
        #                                                         request_method=request_method, url=request_url,
        #                                                         data=req_data)
        #     logging.info("返回结果：{}".format(res_text.json()))
        #     assert_common(res_text, msg=exc_data)

        if case_name == "机构信息获取":
            res_text = ApiFactory.get_clinicDailyInfo().getinfo(moudle_name=moudle_name, case_name=case_name,
                                                                request_method=request_method, url=request_url,
                                                                data=req_data)
            logging.info("返回结果：{}".format(res_text.json()))
            assert_common(res_text, msg=exc_data)
            clinicId = res_text.json().get("data").get("clinicId")

        if case_name == "门诊日志":
            res_text = ApiFactory.get_clinicDailyInfo().page(moudle_name=moudle_name, case_name=case_name,
                                                                request_method=request_method, url=request_url,
                                                                data=req_data)
            logging.info("返回结果：{}".format(res_text.json()))
            assert_common(res_text, msg=exc_data)

        if case_name == "进销存统计":
            res_text = ApiFactory.get_clinicDailyInfo().invoicingStatistics(moudle_name=moudle_name, case_name=case_name,
                                                                request_method=request_method, url=request_url,
                                                                data=json.loads(req_data), clinicId=clinicId)
            logging.info("返回结果：{}".format(res_text.json()))
            assert_common(res_text, msg=exc_data)

        if case_name == "出入库统计":
            res_text = ApiFactory.get_clinicDailyInfo().stockStatistics(moudle_name=moudle_name, case_name=case_name,
                                                                request_method=request_method, url=request_url,
                                                                data=json.loads(req_data), clinicId=clinicId)
            logging.info("返回结果：{}".format(res_text.json()))
            assert_common(res_text, msg=exc_data)

        if case_name == "供应商统计":
            res_text = ApiFactory.get_clinicDailyInfo().supplierStatistics(moudle_name=moudle_name, case_name=case_name,
                                                                request_method=request_method, url=request_url,
                                                                data=req_data)
            logging.info("返回结果：{}".format(res_text.json()))
            assert_common(res_text, msg=exc_data)
