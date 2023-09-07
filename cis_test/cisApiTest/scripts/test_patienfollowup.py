"""
description: 随访管理接口测试用例
time: 2022/06/09
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
class TestPatienfollowup:
    curPath = os.path.abspath(os.path.dirname(__file__))
    rootPath = os.path.split(curPath)[0]
    sys.path.append(rootPath)
    data_path = rootPath + r"\data\patienfollowup.xls"

    '''
    @allure.severity装饰器按严重性级别来标记case　　　
    执行指定测试用例 --allure-severities blocker
    BLOCKER = 'blocker'　　阻塞缺陷
    CRITICAL = 'critical'　严重缺陷
    NORMAL = 'normal'　　  一般缺陷
    MINOR = 'minor'　　    次要缺陷
    TRIVIAL = 'trivial'　　轻微缺陷　
    '''

    @allure.story("随访管理菜单")
    @allure.severity("NORMAL")
    @allure.description("待随访列表-新增-修改-删除-随访-已随访列表-详情")
    @pytest.mark.parametrize("moudle_name,case_name,request_method,request_url,req_data,code,exc_data", read_test_data(data_path, "随访管理", None, 1, 2, 3, 4, 7, 8, 9))
    def test_patienfollowup_case(self, moudle_name, case_name, request_method, request_url, req_data, code, exc_data, clinic_login):
        # logging.info("请求的header：{}".format(api_config.request_header))
        global patientId,clinicId,age,birthday,clinicVip,followDate,name,phone,patienfollowupId,doctorId,id,sex,id2

        if case_name == "待随访列表":
            res_text = ApiFactory.get_patienfollowup().patienfollowupPage(moudle_name=moudle_name, case_name=case_name, request_method=request_method, url=request_url, data=req_data)
            logging.info("返回结果：{}".format(res_text.json()))
            assert_common(res_text, msg=exc_data)

        if case_name == "获取患者id":
            res_text = ApiFactory.get_patienfollowup().visitOrderPage(moudle_name=moudle_name, case_name=case_name, request_method=request_method, url=request_url, data=req_data)
            logging.info("返回结果：{}".format(res_text.json()))
            assert_common(res_text, msg=exc_data)
            patientId = res_text.json().get("data").get("records")[0].get("patientId")
            doctorId = res_text.json().get("data").get("records")[0].get("doctorId")

        if case_name == "新增随访":
            res_text = ApiFactory.get_patienfollowup().patienfollowup(moudle_name=moudle_name, case_name=case_name, request_method=request_method, url=request_url, data=json.loads(req_data), patientId=patientId, doctorId=doctorId)
            logging.info("返回结果：{}".format(res_text.json()))
            assert_common(res_text, msg=exc_data)

        if case_name == "新增随访后查询":
            res_text = ApiFactory.get_patienfollowup().patienfollowupPage(moudle_name=moudle_name, case_name=case_name, request_method=request_method, url=request_url, data=req_data)
            logging.info("返回结果：{}".format(res_text.json()))
            assert_common(res_text, msg=exc_data)
            id = res_text.json().get("data").get("records")[0].get("id")

        if case_name == "删除随访":
            res_text = ApiFactory.get_patienfollowup().patienfollowupDelete(moudle_name=moudle_name, case_name=case_name, request_method=request_method, url=request_url, data=req_data, id=id)
            logging.info("返回结果：{}".format(res_text.json()))
            assert_common(res_text, msg=exc_data)

        if case_name == "根据id查询":
            res_text = ApiFactory.get_patienfollowup().patienfollowupId(moudle_name=moudle_name, case_name=case_name, request_method=request_method, url=request_url, data=req_data, id=id)
            logging.info("返回结果：{}".format(res_text.json()))
            assert_common(res_text, msg=exc_data)
            age = res_text.json().get("data").get("age")[0]
            birthday = res_text.json().get("data").get("birthday")
            clinicId = res_text.json().get("data").get("clinicId")
            clinicVip = res_text.json().get("data").get("clinicVip")
            followDate = res_text.json().get("data").get("followDate")
            name = res_text.json().get("data").get("name")
            phone = res_text.json().get("data").get("phone")
            sex = res_text.json().get("data").get("sex")

        if case_name == "修改随访":
            res_text = ApiFactory.get_patienfollowup().patienfollowupUpdate(moudle_name=moudle_name, case_name=case_name, request_method=request_method, url=request_url, data=json.loads(req_data), id=id, clinicId=clinicId, clinicVip=clinicVip, doctorId=doctorId, patientId=patientId, followDate=followDate, name=name, phone=phone, birthday=birthday, age=age)
            logging.info("返回结果：{}".format(res_text.json()))
            assert_common(res_text, msg=exc_data)

        if case_name == "随访":
            res_text = ApiFactory.get_patienfollowup().patienfollowupUpdate(moudle_name=moudle_name, case_name=case_name, request_method=request_method, url=request_url, data=json.loads(req_data), id=id, clinicId=clinicId, clinicVip=clinicVip, doctorId=doctorId, patientId=patientId, followDate=followDate, name=name, phone=phone, birthday=birthday, age=age)
            logging.info("返回结果：{}".format(res_text.json()))
            assert_common(res_text, msg=exc_data)

        if case_name == "已随访列表":
            res_text = ApiFactory.get_patienfollowup().patienfollowupPage(moudle_name=moudle_name, case_name=case_name, request_method=request_method, url=request_url, data=req_data)
            logging.info("返回结果：{}".format(res_text.json()))
            assert_common(res_text, msg=exc_data)
            id2 = res_text.json().get("data").get("records")[0].get("id")

        if case_name == "查看详情":
            res_text = ApiFactory.get_patienfollowup().patienfollowupDetail(moudle_name=moudle_name, case_name=case_name, request_method=request_method, url=request_url, data=req_data, id2=id2)
            logging.info("返回结果：{}".format(res_text.json()))
            assert_common(res_text, msg=exc_data)




