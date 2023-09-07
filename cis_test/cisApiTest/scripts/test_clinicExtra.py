# -*- coding: utf-8 -*-
# @Time    : 2022/11/4 14:08
# @Author  : PengJiong
# @Email   : 18390050274@qq.com
# @File    : clinicExtra.py.py
import json
import logging
import allure
import pytest
import os
import sys
from utils.assert_common import assert_common
from utils.ReadTabDataUtils import read_test_data
from api.api_factory import ApiFactory
from utils.random_phone import random_name
import api_config

@allure.feature("诊所设置模块")
class TestSupplier:
    curPath = os.path.abspath(os.path.dirname(__file__))
    rootPath = os.path.split(curPath)[0]
    sys.path.append(rootPath)
    data_path = rootPath + r"\data\clinicExtra.xls"

    '''
    @allure.severity装饰器按严重性级别来标记case　　　
    执行指定测试用例 --allure-severities blocker
    BLOCKER = 'blocker'　　阻塞缺陷
    CRITICAL = 'critical'　严重缺陷
    NORMAL = 'normal'　　  一般缺陷
    MINOR = 'minor'　　    次要缺陷
    TRIVIAL = 'trivial'　　轻微缺陷　
    '''


    @allure.story("账号费用设置")
    @allure.severity("BLOCKER")
    @allure.description("001-账号费用设置-新增附加费用-修改附加费用-删除附加费用")
    @pytest.mark.parametrize("moudle_name,case_name,request_method,request_url,req_data,code,exc_data", read_test_data(data_path, "账号费用设置", None, 1, 2, 3, 4, 7, 8, 9))
    def test_clinicconfig_case(self, moudle_name, case_name, request_method, request_url, req_data, code, exc_data, clinic_login):

        global supplierId,supplierName,clinicId,createBy,createTime,medicineId,\
            medicineName,manufacturer,specs,batchNo,medicineType,pieceNumber,packUnit,\
            pieceUnit,newPrice,id,packAmount,typeStr,medicineTypeStr,medicineNamePy,packAmount, \
            pieceAmount,total,type,reason,delFlag,updateBy,updateTime,version,_X_ROW_KEY,typeId,typeName,source,extraId

        if case_name == "功能配置":
            res_text = ApiFactory.get_clinicExtra().info(moudle_name=moudle_name, case_name=case_name, request_method=request_method, url=request_url, data=req_data)
            logging.info("返回结果：{}".format(res_text.json()))
            assert_common(res_text, msg=exc_data)

        if case_name == "附加费用配置列表":
            res_text = ApiFactory.get_clinicconfig().clinicExtrapage(moudle_name=moudle_name, case_name=case_name, request_method=request_method, url=request_url, data=req_data)
            logging.info("返回结果：{}".format(res_text.json()))
            assert_common(res_text, msg=exc_data)

        if case_name == "新增附加费用项目":
            res_text = ApiFactory.get_clinicconfig().addclinicExtra(moudle_name=moudle_name, case_name=case_name, request_method=request_method, url=request_url, data=req_data)
            logging.info("返回结果：{}".format(res_text.json()))
            assert_common(res_text, msg=exc_data)

        if case_name == "附加费用配置列表1":
            res_text = ApiFactory.get_clinicconfig().clinicExtrapage1(moudle_name=moudle_name, case_name=case_name, request_method=request_method, url=request_url, data=req_data)
            logging.info("返回结果：{}".format(res_text.json()))
            assert_common(res_text, msg=exc_data)
            extraId = res_text.json.get("data").get("records")[0].get("extraId")

        if case_name == "新增附加费用详细信息":
            res_text = ApiFactory.get_clinicconfig().chlinicclinicExtra(moudle_name=moudle_name, case_name=case_name, request_method=request_method, url=request_url, data=req_data, extraId=extraId)
            logging.info("返回结果：{}".format(res_text.json()))
            assert_common(res_text, msg=exc_data)

    @allure.story("检验治疗设置")
    @allure.severity("BLOCKER")
    @allure.description("001-检验治疗设置-新增检验治疗-修改检验治疗-删除检验治疗")
    @pytest.mark.parametrize("moudle_name,case_name,request_method,request_url,req_data,code,exc_data",
                             read_test_data(data_path, "检验治疗设置", None, 1, 2, 3, 4, 7, 8, 9))
    def test_clinicconfig_case(self, moudle_name, case_name, request_method, request_url, req_data, code, exc_data,
                               clinic_login):

        global supplierId, supplierName, clinicId, createBy, createTime, medicineId, \
            medicineName, manufacturer, specs, batchNo, medicineType, pieceNumber, packUnit, \
            pieceUnit, newPrice, id, packAmount, typeStr, medicineTypeStr, medicineNamePy, packAmount, \
            pieceAmount, total, type, reason, delFlag, updateBy, updateTime, version, _X_ROW_KEY, typeId, typeName, source, extraId

        if case_name == "新增检验治疗":
            res_text = ApiFactory.get_clinicExtra().addclinicExtra(moudle_name=moudle_name, case_name=case_name, request_method=request_method, url=request_url, data=req_data)
            logging.info("返回结果：{}".format(res_text.json()))
            assert_common(res_text, msg=exc_data)

        if case_name == "检验治疗列表":
            res_text = ApiFactory.get_clinicExtra().extralist(moudle_name=moudle_name, case_name=case_name, request_method=request_method, url=request_url, data=req_data)
            logging.info("返回结果：{}".format(res_text.json()))
            assert assert_common(res_text, msg=exc_data)

        if case_name == "查看新增检验治疗详细":
            res_text = ApiFactory.get_clinicExtra().addExtraXiangxi(moudle_name=moudle_name, case_name=case_name, request_method=request_method, url=request_url, data=req_data)
            logging.info("返回结果：{}".format(res_text.json()))
            assert assert_common(res_text, msg=exc_data)

        if case_name == "检验治疗列表1":
            res_text = ApiFactory.get_clinicExtra().extralist1(moudle_name=moudle_name, case_name=case_name, request_method=request_method, url=request_url, data=req_data)
            logging.info("返回结果：{}".format(res_text.json()))
            assert assert_common(res_text, msg=exc_data)

    @allure.story("挂号费设置")
    @allure.severity("BLOCKER")
    @allure.description("001-设置默认挂号费-设置单个挂号费-挂号费列表")
    @pytest.mark.parametrize("moudle_name,case_name,request_method,request_url,req_data,code,exc_data",
                             read_test_data(data_path, "挂号费设置", None, 1, 2, 3, 4, 7, 8, 9))
    def test_clinicconfig_case(self, moudle_name, case_name, request_method, request_url, req_data, code, exc_data,
                               clinic_login):

        global supplierId, supplierName, clinicId, createBy, createTime, medicineId, \
            medicineName, manufacturer, specs, batchNo, medicineType, pieceNumber, packUnit, \
            pieceUnit, newPrice, id, packAmount, typeStr, medicineTypeStr, medicineNamePy, packAmount

        if case_name == "挂号费设置":
            res_text = ApiFactory.get_clinicExtra().doctorregistrationpage(moudle_name=moudle_name, case_name=case_name, request_method=request_method, url=request_url, data=req_data)
            logging.info("返回结果：{}".format(res_text.json()))
            assert assert_common(res_text, msg=exc_data)

        if case_name == "科室列表显示":
            res_text = ApiFactory.get_clinicExtra().clinicdeptlist(moudle_name=moudle_name, case_name=case_name, request_method=request_method, url=request_url, data=req_data)
            logging.info("返回结果：{}".format(res_text.json()))
            assert assert_common(res_text, msg=exc_data)

        if case_name == "用户列表":
            res_text = ApiFactory.get_clinicExtra().clinicuserlist(moudle_name=moudle_name, case_name=case_name, request_method=request_method, url=request_url, data=req_data)
            logging.info("返回结果：{}".format(res_text.json()))
            assert assert_common(res_text, msg=exc_data)

        if case_name == "湖北各类挂号费":
            res_text = ApiFactory.get_clinicExtra().hubeiservicepage(moudle_name=moudle_name, case_name=case_name, request_method=request_method, url=request_url, data=req_data)
            logging.info("返回结果：{}".format(res_text.json()))
            assert assert_common(res_text, msg=exc_data)

        if case_name == "医生挂号费默认设置":
            res_text = ApiFactory.get_clinicExtra().doctorregistration(moudle_name=moudle_name, case_name=case_name, request_method=request_method, url=request_url, data=req_data)
            logging.info("返回结果：{}".format(res_text.json()))
            assert assert_common(res_text, msg=exc_data)

        if case_name == "挂号费设置1":
            res_text = ApiFactory.get_clinicExtra().doctorregistrationpage1(moudle_name=moudle_name, case_name=case_name, request_method=request_method, url=request_url, data=req_data)
            logging.info("返回结果：{}".format(res_text.json()))
            assert assert_common(res_text, msg=exc_data)

        if case_name == "挂号费临时费用显示":
            res_text = ApiFactory.get_clinicExtra().getClinicRegisterFree(moudle_name=moudle_name, case_name=case_name, request_method=request_method, url=request_url, data=req_data)
            logging.info("返回结果：{}".format(res_text.json()))
            assert assert_common(res_text, msg=exc_data)

        if case_name == "医生注册显示":
            res_text = ApiFactory.get_clinicExtra().doctorregistration(moudle_name=moudle_name, case_name=case_name, request_method=request_method, url=request_url, data=req_data)
            logging.info("返回结果：{}".format(res_text.json()))
            assert assert_common(res_text, msg=exc_data)

    @allure.story("患者标签设置")
    @allure.severity("BLOCKER")
    @allure.description("001-新增患者标签-编辑患者标签-删除患者标签")
    @pytest.mark.parametrize("moudle_name,case_name,request_method,request_url,req_data,code,exc_data",
                             read_test_data(data_path, "患者标签设置", None, 1, 2, 3, 4, 7, 8, 9))
    def test_clinicconfig_case(self, moudle_name, case_name, request_method, request_url, req_data, code, exc_data,
                               clinic_login):

        global supplierId, supplierName, clinicId, createBy, createTime, medicineId, \
            medicineName, manufacturer, specs, batchNo, medicineType, pieceNumber, packUnit, \
            pieceUnit, newPrice, id, packAmount, typeStr, medicineTypeStr, medicineNamePy, packAmount, tagId,\
        tagName, updateBy

        if case_name == "患者标签设置":
            res_text = ApiFactory.get_clinicExtra().patientTagpage(moudle_name=moudle_name, case_name=case_name, request_method=request_method, url=request_url, data=req_data)
            logging.info("返回结果：{}".format(res_text.json()))
            assert assert_common(res_text, msg=exc_data)

        if case_name == "新增患者标签":
            res_text = ApiFactory.get_clinicExtra().addpatientTag(moudle_name=moudle_name, case_name=case_name, request_method=request_method, url=request_url, data=req_data)
            logging.info("返回结果：{}".format(res_text.json()))
            assert assert_common(res_text, msg=exc_data)

        if case_name == "患者标签设置1":
            res_text = ApiFactory.get_clinicExtra().patientTagpage1(moudle_name=moudle_name, case_name=case_name, request_method=request_method, url=request_url, data=req_data)
            logging.info("返回结果：{}".format(res_text.json()))
            assert assert_common(res_text, msg=exc_data)
            clinicId = res_text.json.get("data").get("records")[0].get("clinicId")
            createBy = res_text.json.get("data").get("records")[0].get("createBy")
            tagId = res_text.json.get("data").get("records")[0].get("tagId")
            tagName = res_text.json.get("data").get("records")[0].get("tagName")
            updateBy = res_text.json.get("data").get("records")[0].get("updateBy")

        if case_name == "查看患者详情":
            res_text = ApiFactory.get_clinicExtra().patientTagxq(moudle_name=moudle_name, case_name=case_name, request_method=request_method, url=request_url, data=req_data, tagId=tagId)
            logging.info("返回结果：{}".format(res_text.json()))
            assert assert_common(res_text, msg=exc_data)

        if case_name == "修改患者标签":
            res_text = ApiFactory.get_clinicExtra().clinicpatientTag(moudle_name=moudle_name, case_name=case_name, request_method=request_method, url=request_url, data=req_data, tagId=tagId, clinicId=clinicId, createBy=createBy, updateBy=updateBy)
            logging.info("返回结果：{}".format(res_text.json()))
            assert assert_common(res_text, msg=exc_data)

        if case_name == "删除患者标签":
            res_text = ApiFactory.get_clinicExtra().delpatientTag(moudle_name=moudle_name, case_name=case_name, request_method=request_method, url=request_url, data=req_data, tagId=tagId)
            logging.info("返回结果：{}".format(res_text.json()))
            assert assert_common(res_text, msg=exc_data)

    @allure.story("交接班记录")
    @allure.severity("BLOCKER")
    @allure.description("001-查看交接班记录列表-")
    @pytest.mark.parametrize("moudle_name,case_name,request_method,request_url,req_data,code,exc_data",
                             read_test_data(data_path, "患者标签设置", None, 1, 2, 3, 4, 7, 8, 9))
    def test_clinicconfig_case(self, moudle_name, case_name, request_method, request_url, req_data, code, exc_data,
                               clinic_login):

        global supplierId, supplierName, clinicId, createBy, createTime, medicineId, \
            medicineName, manufacturer, specs, batchNo, medicineType, pieceNumber, packUnit

        if case_name == "查看用户信息":
            res_text = ApiFactory.get_clinicExtra().getUser(moudle_name=moudle_name, case_name=case_name, request_method=request_method, url=request_url, data=req_data)
            logging.info("返回结果：{}".format(res_text.json()))
            assert assert_common(res_text, msg=exc_data)