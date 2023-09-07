"""
description: 模板管理接口测试用例
time: 2022/01/22
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

@allure.feature("门诊管理模块")
class TestTemplateManagement:
    curPath = os.path.abspath(os.path.dirname(__file__))
    rootPath = os.path.split(curPath)[0]
    sys.path.append(rootPath)
    data_path = rootPath + r"\data\templateManagement.xls"

    '''
    @allure.severity装饰器按严重性级别来标记case　　　
    执行指定测试用例 --allure-severities blocker
    BLOCKER = 'blocker'　　阻塞缺陷
    CRITICAL = 'critical'　严重缺陷
    NORMAL = 'normal'　　  一般缺陷
    MINOR = 'minor'　　    次要缺陷
    TRIVIAL = 'trivial'　　轻微缺陷　
    '''

    @allure.story("模板管理菜单")
    @allure.severity("BLOCKER")
    @allure.description("001模板管理查询-按类型查询")
    @pytest.mark.parametrize("moudle_name,case_name,request_method,request_url,req_data,code,exc_data", read_test_data(data_path, "查询", None, 1, 2, 3, 4, 7, 8, 9))
    def test_templateList_case(self, moudle_name, case_name, request_method, request_url, req_data, code, exc_data, clinic_login):

        res_text = ApiFactory.get_templateManagement().templatePage(moudle_name=moudle_name, case_name=case_name, request_method=request_method, url=request_url, data=req_data)
        logging.info("返回结果：{}".format(res_text.json()))
        assert_common(res_text, msg=exc_data)

    @allure.story("模板管理菜单")
    @allure.severity("BLOCKER")
    @allure.description("002模板管理-新增-编辑-删除")
    @pytest.mark.parametrize("moudle_name,case_name,request_method,request_url,req_data,code,exc_data", read_test_data(data_path, "新增", None, 1, 2, 3, 4, 7, 8, 9))
    def test_templateAdd_case(self, moudle_name, case_name, request_method, request_url, req_data, code, exc_data, clinic_login):
        global total, batchNo, clinicId, expireDate, id, manufacturer, manufacturerPinyin, medicineId, medicineName, namePinyin, newPrice, packAmount, packUnit, pieceAmount, pieceTotal, \
            specs, stock, stockId, supplierId, retailPrice, title, templateId, titlePy, doctorId, id2, createBy, createTime

        if case_name == "药品搜索":
            res_text = ApiFactory.get_clinicalReception().selectMedicineStock(moudle_name=moudle_name, case_name=case_name, request_method=request_method, url=request_url, data=json.loads(req_data))
            logging.info("返回结果：{}".format(res_text.json()))
            assert_common(res_text, msg=exc_data)
            batchNo = res_text.json().get("data")[0].get("batchNo")
            total = res_text.json().get("data")[0].get("total")
            pieceTotal = res_text.json().get("data")[0].get("pieceTotal")
            packUnit = res_text.json().get("data")[0].get("packUnit")
            specs = res_text.json().get("data")[0].get("specs")
            retailPrice = res_text.json().get("data")[0].get("retailPrice")
            manufacturer = res_text.json().get("data")[0].get("manufacturer")
            stock = res_text.json().get("data")[0].get("stock")
            id = res_text.json().get("data")[0].get("id")
            clinicId = res_text.json().get("data")[0].get("clinicId")
            namePinyin = res_text.json().get("data")[0].get("namePinyin")
            manufacturerPinyin = res_text.json().get("data")[0].get("manufacturerPinyin")
            packAmount = res_text.json().get("data")[0].get("packAmount")
            pieceAmount = res_text.json().get("data")[0].get("pieceAmount")
            stockId = res_text.json().get("data")[0].get("stockId")
            newPrice = res_text.json().get("data")[0].get("newPrice")
            medicineId = res_text.json().get("data")[0].get("medicineId")
            expireDate = res_text.json().get("data")[0].get("expireDate")
            supplierId = res_text.json().get("data")[0].get("supplierId")
            medicineName = res_text.json().get("data")[0].get("medicineName")

        if case_name == "新增模板":
            res_text = ApiFactory.get_templateManagement().templateAdd(moudle_name=moudle_name, case_name=case_name, request_method=request_method, url=request_url, data=json.loads(req_data),
                                                                           batchNo=batchNo, total=total, pieceTotal=pieceTotal, packUnit=packUnit, specs=specs, retailPrice=retailPrice, manufacturer=manufacturer,
                                                                           stock=stock, id=id, clinicId=clinicId, namePinyin=namePinyin, manufacturerPinyin=manufacturerPinyin, packAmount=packAmount, pieceAmount=pieceAmount,
                                                                           stockId=stockId, newPrice=newPrice, medicineId=medicineId, expireDate=expireDate, supplierId=supplierId, medicineName=medicineName)
            logging.info("返回结果：{}".format(res_text[0].json()))
            assert_common(res_text[0], msg=exc_data)
            title = res_text[1]


        if case_name == "查询新增模板":
            res_text = ApiFactory.get_templateManagement().templatePage_name(moudle_name=moudle_name, case_name=case_name, request_method=request_method, url=request_url, data=req_data, title=title)
            logging.info("返回结果：{}".format(res_text.json()))
            assert_common(res_text, msg=exc_data)
            templateId = res_text.json().get("data").get("records")[0].get("templateId")
            titlePy = res_text.json().get("data").get("records")[0].get("titlePy")
            doctorId = res_text.json().get("data").get("records")[0].get("doctorId")

        if case_name == "模板详情":
            res_text = ApiFactory.get_templateManagement().templatedetails(moudle_name=moudle_name, case_name=case_name, request_method=request_method, url=request_url, data=req_data, templateId=templateId)
            logging.info("返回结果：{}".format(res_text.json()))
            assert_common(res_text, msg=exc_data)
            id2 = res_text.json().get("data").get("syntheticMedicineVOS")[0].get("id")
            createBy = res_text.json().get("data").get("createBy")
            createTime = res_text.json().get("data").get("createTime")

        if case_name == "编辑模板":
            res_text = ApiFactory.get_templateManagement().templateEdit(moudle_name=moudle_name, case_name=case_name, request_method=request_method, url=request_url, data=json.loads(req_data), packUnit=packUnit, specs=specs, retailPrice=retailPrice, manufacturer=manufacturer, clinicId=clinicId, medicineId=medicineId, medicineName=medicineName, templateId=templateId, titlePy=titlePy, doctorId=doctorId, id2=id2, createBy=createBy, createTime=createTime, title=title)
            logging.info("返回结果：{}".format(res_text.json()))
            assert_common(res_text, msg=exc_data)

        if case_name == "删除模板":
            res_text = ApiFactory.get_templateManagement().templateDelete(moudle_name=moudle_name, case_name=case_name, request_method=request_method, url=request_url, data=req_data, templateId=templateId)
            logging.info("返回结果：{}".format(res_text.json()))
            assert_common(res_text, msg=exc_data)


