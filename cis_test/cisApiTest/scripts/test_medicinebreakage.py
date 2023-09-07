# -*- coding: utf-8 -*-
# @Time    : 2022/9/2 11:51
# @Author  : PengJiong
# @Email   : 18390050274@qq.com
# @File    : test_medicinebreakage.py.py
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
    data_path = rootPath + r"\data\medicinebreakage.xls"

    '''
    @allure.severity装饰器按严重性级别来标记case　　　
    执行指定测试用例 --allure-severities blocker
    BLOCKER = 'blocker'　　阻塞缺陷
    CRITICAL = 'critical'　严重缺陷
    NORMAL = 'normal'　　  一般缺陷
    MINOR = 'minor'　　    次要缺陷
    TRIVIAL = 'trivial'　　轻微缺陷　
    '''


    @allure.story("损毁管理")
    @allure.severity("BLOCKER")
    @allure.description("001-损毁列表-药品搜索-选择首个药品-保存报损药品信息")
    @pytest.mark.parametrize("moudle_name,case_name,request_method,request_url,req_data,code,exc_data", read_test_data(data_path, "损毁管理", None, 1, 2, 3, 4, 7, 8, 9))
    def test_medicinebreakage_case(self, moudle_name, case_name, request_method, request_url, req_data, code, exc_data, clinic_login):

        global supplierId,supplierName,clinicId,createBy,createTime,medicineId,\
            medicineName,manufacturer,specs,batchNo,medicineType,pieceNumber,packUnit,\
            pieceUnit,newPrice,id,packAmount,typeStr,medicineTypeStr,medicineNamePy,packAmount, \
            pieceAmount,total,type,reason,delFlag,updateBy,updateTime,version,_X_ROW_KEY

        if case_name == "损毁列表":
            res_text = ApiFactory.get_medicinebreakage().medicinebreakage(moudle_name=moudle_name, case_name=case_name, request_method=request_method, url=request_url, data=req_data)
            logging.info("返回结果：{}".format(res_text.json()))
            assert_common(res_text, msg=exc_data)

        if case_name == "药品搜索":
            res_text = ApiFactory.get_medicinebreakage().selectBreakageMedicineStock(moudle_name=moudle_name, case_name=case_name, request_method=request_method, url=request_url, data=json.loads(req_data))
            logging.info("返回结果:{}".format(res_text.json()))
            assert_common(res_text, msg=exc_data)
            medicineId = res_text.json().get("data")[0].get("medicineId")
            medicineName = res_text.json().get("data")[0].get("medicineName")
            manufacturer = res_text.json().get("data")[0].get("manufacturer")
            specs = res_text.json().get("data")[0].get("specs")
            batchNo = res_text.json().get("data")[0].get("batchNo")
            medicineType = res_text.json().get("data")[0].get("medicineType")
            pieceNumber = res_text.json().get("data")[0].get("pieceNumber")
            packUnit = res_text.json().get("data")[0].get("packUnit")
            newPrice = res_text.json().get("data")[0].get("newPrice")
            clinicId = res_text.json().get("data")[0].get("clinicId")

        if case_name == "选择首个药品":
            res_text = ApiFactory.get_medicinebreakage().selDrugStock(moudle_name=moudle_name, case_name=case_name, request_method=request_method, url=request_url, data=req_data, medicineId=medicineId)
            logging.info("返回结果:{}".format(res_text.json()))
            assert_common(res_text, msg=exc_data)

        if case_name == "保存报损药品信息":
            res_text = ApiFactory.get_medicinebreakage().saveAndDrugStock(moudle_name=moudle_name, case_name=case_name, request_method=request_method, url=request_url, data=json.loads(req_data), medicineId=medicineId,
            medicineName=medicineName, manufacturer=manufacturer, specs=specs, pieceNumber=pieceNumber, packUnit=packUnit, newPrice=newPrice)
            logging.info("返回结果:{}".format(res_text.json()))
            assert_common(res_text, msg=exc_data)

        if case_name == "损毁列表1":
            res_text = ApiFactory.get_medicinebreakage().medicinebreakage1(moudle_name=moudle_name, case_name=case_name, request_method=request_method, url=request_url, data=req_data)
            logging.info("返回结果：{}".format(res_text.json()))
            id = res_text.json().get("data").get("records")[0].get("id")
            medicineTypeStr = res_text.json().get("data").get("records")[0].get("medicineTypeStr")
            typeStr = res_text.json().get("data").get("records")[0].get("typeStr")
            createBy = res_text.json().get("data").get("records")[0].get("createBy")
            createTime = res_text.json().get("data").get("records")[0].get("createTime")
            assert_common(res_text, msg=exc_data)

        if case_name == "撤销报损药品":
            res_text = ApiFactory.get_medicinebreakage().cancelAndAddStock(moudle_name=moudle_name, case_name=case_name, request_method=request_method, url=request_url, data=json.loads(req_data), medicineId=medicineId,
            medicineName=medicineName, manufacturer=manufacturer, specs=specs, batchNo=batchNo, medicineType=medicineType, pieceNumber=pieceNumber, packUnit=packUnit, newPrice=newPrice, id=id, medicineTypeStr=medicineTypeStr,
                                                                           typeStr=typeStr, createBy=createBy, createTime=createTime, clinicId=clinicId)
            logging.info("返回结果:{}".format(res_text.json()))
            assert_common(res_text, msg=exc_data)