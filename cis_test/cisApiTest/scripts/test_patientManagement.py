"""
description: 患者管理接口测试用例
time: 2022/05/11
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

@allure.feature("患者管理模块")
class TestPatientManagement:
    curPath = os.path.abspath(os.path.dirname(__file__))
    rootPath = os.path.split(curPath)[0]
    sys.path.append(rootPath)
    data_path = rootPath + r"\data\patientManagement.xls"

    '''
    @allure.severity装饰器按严重性级别来标记case　　　
    执行指定测试用例 --allure-severities blocker
    BLOCKER = 'blocker'　　阻塞缺陷
    CRITICAL = 'critical'　严重缺陷
    NORMAL = 'normal'　　  一般缺陷
    MINOR = 'minor'　　    次要缺陷
    TRIVIAL = 'trivial'　　轻微缺陷　
    '''

    @allure.story("患者管理菜单")
    @allure.severity("NORMAL")
    @allure.description("患者管理列表-档案详情-修改患者信息-门诊记录-详情-零售纪录-详情-随访记录-详情-患者轨迹")
    @pytest.mark.parametrize("moudle_name,case_name,request_method,request_url,req_data,code,exc_data", read_test_data(data_path, "患者管理", None, 1, 2, 3, 4, 7, 8, 9))
    def test_patientManagement_case(self, moudle_name, case_name, request_method, request_url, req_data, code, exc_data, clinic_login):
        # logging.info("请求的header：{}".format(api_config.request_header))
        global patientId,clinicId,clinicName,createBy,createTime,visitOrderId,medicalRecordId,orderId,patienfollowupId

        if case_name == "患者管理列表":
            res_text = ApiFactory.get_patientManagement().visitOrderPage(moudle_name=moudle_name, case_name=case_name, request_method=request_method, url=request_url, data=req_data)
            logging.info("返回结果：{}".format(res_text.json()))
            assert_common(res_text, msg=exc_data)
            patientId = res_text.json().get("data").get("records")[0].get("patientId")

        if case_name == "档案详情":
            res_text = ApiFactory.get_patientManagement().fileDetails(moudle_name=moudle_name, case_name=case_name, request_method=request_method, url=request_url, data=req_data, patientId=patientId)
            logging.info("返回结果：{}".format(res_text.json()))
            assert_common(res_text, msg=exc_data)
            clinicId = res_text.json().get("data").get("patientInfo").get("clinicId")
            clinicName = res_text.json().get("data").get("patientInfo").get("clinicName")
            createBy = res_text.json().get("data").get("patientInfo").get("createBy")
            createTime = res_text.json().get("data").get("patientInfo").get("createTime")

        if case_name == "修改患者信息":
            res_text = ApiFactory.get_patientManagement().patientinfo(moudle_name=moudle_name, case_name=case_name, request_method=request_method, url=request_url, data=json.loads(req_data), patientId=patientId, clinicId=clinicId, clinicName=clinicName, createBy=createBy, createTime=createTime)
            logging.info("返回结果：{}".format(res_text.json()))
            assert_common(res_text, msg=exc_data)

        if case_name == "门诊记录":
            res_text = ApiFactory.get_patientManagement().outpatientRecordsPage(moudle_name=moudle_name, case_name=case_name, request_method=request_method, url=request_url, data=req_data, patientId=patientId)
            logging.info("返回结果：{}".format(res_text.json()))
            assert_common(res_text, msg=exc_data)
            visitOrderId = res_text.json().get("data").get("records")[0].get("id")
            medicalRecordId = res_text.json().get("data").get("records")[0].get("medicalRecordId")

        if case_name == "门诊记录-详情":
            res_text = ApiFactory.get_patientManagement().outpatientRecordsDetail(moudle_name=moudle_name, case_name=case_name, request_method=request_method, url=request_url, data=req_data, medicalRecordId=medicalRecordId, visitOrderId=visitOrderId)
            logging.info("返回结果：{}".format(res_text.json()))
            assert_common(res_text, msg=exc_data)

        if case_name == "患者轨迹":
            res_text = ApiFactory.get_patientManagement().patientTrajectoryPage(moudle_name=moudle_name, case_name=case_name, request_method=request_method, url=request_url, data=req_data, patientId=patientId)
            logging.info("返回结果：{}".format(res_text.json()))
            assert_common(res_text, msg=exc_data)

        if case_name == "零售纪录":
            res_text = ApiFactory.get_patientManagement().saleOrders(moudle_name=moudle_name, case_name=case_name, request_method=request_method, url=request_url, data=req_data, patientId=patientId)
            logging.info("返回结果：{}".format(res_text.json()))
            assert_common(res_text, msg=exc_data)
            orderId = res_text.json().get("data").get("records")[0].get("orderId")

        if case_name == "零售纪录-详情":
            res_text = ApiFactory.get_patientManagement().retailRecordDetailInfo(moudle_name=moudle_name, case_name=case_name, request_method=request_method, url=request_url, data=req_data, orderId=orderId)
            logging.info("返回结果：{}".format(res_text.json()))
            assert_common(res_text, msg=exc_data)

        if case_name == "随访记录":
            res_text = ApiFactory.get_patientManagement().patienfollowup(moudle_name=moudle_name, case_name=case_name, request_method=request_method, url=request_url, data=req_data, patientId=patientId)
            logging.info("返回结果：{}".format(res_text.json()))
            assert_common(res_text, msg=exc_data)
            patienfollowupId = res_text.json().get("data").get("records")[0].get("id")

        if case_name == "随访记录-详情":
            res_text = ApiFactory.get_patientManagement().patienfollowupDetail(moudle_name=moudle_name, case_name=case_name, request_method=request_method, url=request_url, data=req_data, patienfollowupId=patienfollowupId)
            logging.info("返回结果：{}".format(res_text.json()))
            assert_common(res_text, msg=exc_data)
