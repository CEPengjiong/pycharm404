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
from utils.random_phone import random_name
import api_config

@allure.feature("诊所设置模块")
class TestSupplier:
    curPath = os.path.abspath(os.path.dirname(__file__))
    rootPath = os.path.split(curPath)[0]
    sys.path.append(rootPath)
    data_path = rootPath + r"\data\clinicconfig.xls"

    '''
    @allure.severity装饰器按严重性级别来标记case　　　
    执行指定测试用例 --allure-severities blocker
    BLOCKER = 'blocker'　　阻塞缺陷
    CRITICAL = 'critical'　严重缺陷
    NORMAL = 'normal'　　  一般缺陷
    MINOR = 'minor'　　    次要缺陷
    TRIVIAL = 'trivial'　　轻微缺陷　
    '''


    @allure.story("机构设置")
    @allure.severity("BLOCKER")
    @allure.description("001-机构设置-中西成药-注射处方-中药处方-敷贴")
    @pytest.mark.parametrize("moudle_name,case_name,request_method,request_url,req_data,code,exc_data", read_test_data(data_path, "诊所设置", None, 1, 2, 3, 4, 7, 8, 9))
    def test_clinicconfig_case(self, moudle_name, case_name, request_method, request_url, req_data, code, exc_data, clinic_login):

        global supplierId,supplierName,clinicId,createBy,createTime,medicineId,\
            medicineName,manufacturer,specs,batchNo,medicineType,pieceNumber,packUnit,\
            pieceUnit,newPrice,id,packAmount,typeStr,medicineTypeStr,medicineNamePy,packAmount, \
            pieceAmount,total,type,reason,delFlag,updateBy,updateTime,version,_X_ROW_KEY,typeId,typeName,source

        if case_name == "功能配置":
            res_text = ApiFactory.get_clinicconfig().info(moudle_name=moudle_name, case_name=case_name, request_method=request_method, url=request_url, data=req_data)
            logging.info("返回结果：{}".format(res_text.json()))
            assert_common(res_text, msg=exc_data)

        if case_name == "中西成药模板配置":
            res_text = ApiFactory.get_clinicconfig().synthetic(moudle_name=moudle_name, case_name=case_name, request_method=request_method, url=request_url, data=req_data)
            logging.info("返回结果：{}".format(res_text.json()))
            assert_common(res_text, msg=exc_data)

        if case_name == "注射模板配置":
            res_text = ApiFactory.get_clinicconfig().infusion(moudle_name=moudle_name, case_name=case_name, request_method=request_method, url=request_url, data=req_data)
            logging.info("返回结果：{}".format(res_text.json()))
            assert_common(res_text, msg=exc_data)

        if case_name == "中药模板配置":
            res_text = ApiFactory.get_clinicconfig().chinese(moudle_name=moudle_name, case_name=case_name, request_method=request_method, url=request_url, data=req_data)
            logging.info("返回结果：{}".format(res_text.json()))
            assert_common(res_text, msg=exc_data)

        if case_name == "敷贴模板配置":
            res_text = ApiFactory.get_clinicconfig().applicator(moudle_name=moudle_name, case_name=case_name, request_method=request_method, url=request_url, data=req_data)
            logging.info("返回结果：{}".format(res_text.json()))
            assert_common(res_text, msg=exc_data)

    @allure.story("疾病症状设置")
    @allure.severity("BLOCKER")
    @allure.description("001-疾病症状设置-查看疾病类型-新增疾病类型-修改疾病类型-删除疾病类型")
    @pytest.mark.parametrize("moudle_name,case_name,request_method,request_url,req_data,code,exc_data",read_test_data(data_path, "疾病症状设置", None, 1, 2, 3, 4, 7, 8, 9))
    def test_tdiseasetype_case(self, moudle_name, case_name, request_method, request_url, req_data, code, exc_data, clinic_login):

        global supplierId, supplierName, clinicId, createBy, createTime, medicineId, \
                medicineName, manufacturer, specs, batchNo, medicineType, pieceNumber, packUnit, \
                pieceUnit, newPrice, id, packAmount, typeStr, medicineTypeStr, medicineNamePy, packAmount, \
                pieceAmount, total, type, reason, delFlag, updateBy, updateTime, version, _X_ROW_KEY, typeId, typeName,\
                source,diseaseId,diseaseTypeId,createTime1,updateTime1,diseaseName

        if case_name == "机构信息获取":
            res_text = ApiFactory.get_clinicconfig().getinfo(moudle_name=moudle_name, case_name=case_name, request_method=request_method, url=request_url, data=req_data)
            logging.info("返回结果：{}".format(res_text.json()))
            assert_common(res_text, msg=exc_data)

        if case_name == "疾病类型":
            res_text = ApiFactory.get_clinicconfig().tdiseasetype(moudle_name=moudle_name, case_name=case_name, request_method=request_method, url=request_url, data=req_data)
            logging.info("返回结果：{}".format(res_text.json()))
            assert_common(res_text, msg=exc_data)

        if case_name == "新增疾病类型":
            res_text = ApiFactory.get_clinicconfig().xinzengjibing(moudle_name=moudle_name, case_name=case_name, request_method=request_method, url=request_url, data=json.loads(req_data))
            logging.info("返回结果：{}".format(res_text.json()))
            assert_common(res_text, msg=exc_data)

        if case_name == "疾病类型2":
            res_text = ApiFactory.get_clinicconfig().tdiseasetype2(moudle_name=moudle_name, case_name=case_name, request_method=request_method, url=request_url, data=req_data)
            logging.info("返回结果：{}".format(res_text.json()))
            assert_common(res_text, msg=exc_data)
            typeId = res_text.json().get("data").get("records")[1].get("typeId")
            clinicId = res_text.json().get("data").get("records")[1].get("clinicId")
            source = res_text.json().get("data").get("records")[1].get("source")
            updateBy = res_text.json().get("data").get("records")[1].get("updateBy")
            createTime = res_text.json().get("data").get("records")[1].get("createTime")
            updateTime = res_text.json().get("data").get("records")[1].get("updateTime")

        if case_name == "修改疾病类型":
            res_text = ApiFactory.get_clinicconfig().updatajibing(moudle_name=moudle_name, case_name=case_name, request_method=request_method, url=request_url, data=json.loads(req_data), typeId=typeId,
                                                                  clinicId=clinicId, source=source, createTime=createTime, updateTime=updateTime, updateBy=updateBy)
            logging.info("返回结果：{}".format(res_text.json()))
            assert_common(res_text, msg=exc_data)

        if case_name == "删除疾病类型":
            res_text = ApiFactory.get_clinicconfig().deletetype(moudle_name=moudle_name, case_name=case_name, request_method=request_method, url=request_url, data=req_data, typeId=typeId)
            logging.info("返回结果：{}".format(res_text.json()))
            assert_common(res_text, msg=exc_data)

        if case_name == "疾病名称":
            res_text = ApiFactory.get_clinicconfig().tclinicdisease(moudle_name=moudle_name, case_name=case_name, request_method=request_method, url=request_url, data=req_data)
            logging.info("返回结果：{}".format(res_text.json()))
            assert_common(res_text, msg=exc_data)
            diseaseId = res_text.json().get("data").get("records")[0].get("diseaseId")
            diseaseTypeId = res_text.json().get("data").get("records")[0].get("diseaseTypeId")
            createBy = res_text.json().get("data").get("records")[0].get("createBy")
            createTime1 = res_text.json().get("data").get("records")[0].get("createTime")
            updateTime1 = res_text.json().get("data").get("records")[0].get("updateTime")

        if case_name == "疾病名称列表":
            res_text = ApiFactory.get_clinicconfig().tclinicdiseaselist(moudle_name=moudle_name, case_name=case_name, request_method=request_method, url=request_url, data=req_data)
            logging.info("返回结果：{}".format(res_text.json()))
            assert_common(res_text, msg=exc_data)

        if case_name == "新增疾病名称":
            res_text = ApiFactory.get_clinicconfig().xinzengtclinicdisease(moudle_name=moudle_name, case_name=case_name, request_method=request_method, url=request_url, data=json.loads(req_data), diseaseId=diseaseId,
                                                                           diseaseTypeId=diseaseTypeId, createBy=createBy, createTime1=createTime1, updateTime1=updateTime1)
            logging.info("返回结果：{}".format(res_text.json()))
            assert_common(res_text, msg=exc_data)

        if case_name == "疾病名称2":
            res_text = ApiFactory.get_clinicconfig().tclinicdisease2(moudle_name=moudle_name, case_name=case_name, request_method=request_method, url=request_url, data=req_data)
            logging.info("返回结果：{}".format(res_text.json()))
            assert_common(res_text, msg=exc_data)

        if case_name == "修改疾病名称":
            res_text = ApiFactory.get_clinicconfig().updatatclinicdisease(moudle_name=moudle_name, case_name=case_name, request_method=request_method, url=request_url, data=json.loads(req_data), diseaseId=diseaseId, clinicId=clinicId,
                                                                          diseaseTypeId=diseaseTypeId, createBy=createBy, createTime=createTime, updateTime=updateTime)
            logging.info("返回结果：{}".format(res_text.json()))
            assert_common(res_text, msg=exc_data)

        if case_name == "删除疾病名称":
            res_text = ApiFactory.get_clinicconfig().tclinicdiseaseDle(moudle_name=moudle_name, case_name=case_name, request_method=request_method, url=request_url, data=req_data, diseaseId=diseaseId)
            logging.info("返回结果：{}".format(res_text.json()))
            assert_common(res_text, msg=exc_data)

    @allure.story("账号权限设置-科室管理")
    @allure.severity("BLOCKER")
    @allure.description("001-刷新-新增疾病类型-修改疾病类型-删除")
    @pytest.mark.parametrize("moudle_name,case_name,request_method,request_url,req_data,code,exc_data",read_test_data(data_path, "账号权限设置", None, 1, 2, 3, 4, 7, 8, 9))
    def test_clinicdept_case(self, moudle_name, case_name, request_method, request_url, req_data, code, exc_data, clinic_login):

        global deptName,hospDeptName,status,medicalDeptId,deptId,clinicId,caty,createBy,medicalDeptName,medicalDeptCode

        if case_name == "科室列表刷新":
            res_text = ApiFactory.get_clinicconfig().clinicdeptpage(moudle_name=moudle_name, case_name=case_name, request_method=request_method, url=request_url, data=req_data)
            logging.info("返回结果：{}".format(res_text.json()))
            assert_common(res_text, msg=exc_data)
            deptName = res_text.json().get("data").get("records")[0].get("deptName")
            hospDeptName = res_text.json().get("data").get("records")[0].get("hospDeptName")
            status = res_text.json().get("data").get("records")[0].get("status")
            medicalDeptId = res_text.json().get("data").get("records")[0].get("medicalDeptId")

        if case_name == "新增科室":
            res_text = ApiFactory.get_clinicconfig().clinicdept(moudle_name=moudle_name, case_name=case_name, request_method=request_method, url=request_url, data=req_data)
            logging.info("返回结果：{}".format(res_text.json()))
            assert_common(res_text, msg=exc_data)

        if case_name == "科室列表刷新1":
            res_text = ApiFactory.get_clinicconfig().clinicdeptpage1(moudle_name=moudle_name, case_name=case_name, request_method=request_method, url=request_url, data=req_data)
            logging.info("返回结果：{}".format(res_text.json()))
            assert_common(res_text, msg=exc_data)
            deptId = res_text.json().get("data").get("records")[3].get("deptId")
            clinicId = res_text.json().get("data").get("records")[3].get("clinicId")
            caty = res_text.json().get("data").get("records")[3].get("caty")
            createBy = res_text.json().get("data").get("records")[3].get("createBy")
            medicalDeptName = res_text.json().get("data").get("records")[3].get("medicalDeptName")
            medicalDeptCode = res_text.json().get("data").get("records")[3].get("medicalDeptCode")

        if case_name == "查看科室详细信息":
            res_text = ApiFactory.get_clinicconfig().Seedept(moudle_name=moudle_name, case_name=case_name, request_method=request_method, url=request_url, data=req_data)
            logging.info("返回结果：{}".format(res_text.json()))
            assert_common(res_text, msg=exc_data)

        if case_name == "修改科室":
            res_text = ApiFactory.get_clinicconfig().Modifydept(moudle_name=moudle_name, case_name=case_name, request_method=request_method, url=request_url, data=req_data)
            logging.info("返回结果：{}".format(res_text.json()))
            assert_common(res_text, msg=exc_data)

        if case_name == "删除科室":
            res_text = ApiFactory.get_clinicconfig().Deldept(moudle_name=moudle_name, case_name=case_name, request_method=request_method, url=request_url, data=req_data, deptId=deptId)
            logging.info("返回结果：{}".format(res_text.json()))
            assert_common(res_text, msg=exc_data)

    @allure.story("账号权限设置-角色管理")
    @allure.severity("BLOCKER")
    @allure.description("新增角色-修改角色-删除角色")
    @pytest.mark.parametrize("moudle_name,case_name,request_method,request_url,req_data,code,exc_data",
                             read_test_data(data_path, "账号权限设置", None, 1, 2, 3, 4, 7, 8, 9))
    def test_clinicdept_case(self, moudle_name, case_name, request_method, request_url, req_data, code, exc_data,
                             clinic_login):

        global deptName, hospDeptName, status, medicalDeptId, deptId, clinicId, caty, createBy, medicalDeptName, medicalDeptCode\
            , roleId

        if case_name == "新增角色":
            res_text = ApiFactory.get_clinicconfig().addrole(moudle_name=moudle_name, case_name=case_name,
                                                                request_method=request_method, url=request_url,
                                                                data=req_data)
            logging.info("返回结果：{}".format(res_text.json()))
            assert_common(res_text, msg=exc_data)

        if case_name == "角色列表刷新":
            res_text = ApiFactory.get_clinicconfig().rolelist(moudle_name=moudle_name, case_name=case_name,
                                                                request_method=request_method, url=request_url,
                                                                data=req_data)
            logging.info("返回结果：{}".format(res_text.json()))
            assert_common(res_text, msg=exc_data)
            roleId = res_text.json().get("data").get("records")[0].get("roleId")

        if case_name == "角色删除":
            res_text = ApiFactory.get_clinicconfig().delrole(moudle_name=moudle_name, case_name=case_name,
                                                                request_method=request_method, url=request_url,
                                                                data=req_data, roleID=roleId)
            logging.info("返回结果：{}".format(res_text.json()))
            assert_common(res_text, msg=exc_data)

    @allure.story("账号权限设置-员工管理")
    @allure.severity("BLOCKER")
    @allure.description("员工列表刷新-修改角色")
    @pytest.mark.parametrize("moudle_name,case_name,request_method,request_url,req_data,code,exc_data",
                             read_test_data(data_path, "账号权限设置", None, 1, 2, 3, 4, 7, 8, 9))
    def test_clinicdept_case(self, moudle_name, case_name, request_method, request_url, req_data, code, exc_data,
                             clinic_login):

        global deptName, hospDeptName, status, medicalDeptId, deptId, clinicId, caty, createBy, medicalDeptName, medicalDeptCode\
            , roleId, userId

        if case_name == "员工列表刷新":
            res_text = ApiFactory.get_clinicconfig().userqueryPage(moudle_name=moudle_name, case_name=case_name,
                                                                request_method=request_method, url=request_url,
                                                                data=req_data)
            logging.info("返回结果：{}".format(res_text.json()))
            assert_common(res_text, msg=exc_data)
            userId = res_text.json().get("data").get("records")[0].get("userId")

        if case_name == "查看员工详细信息":
            res_text = ApiFactory.get_clinicconfig().userid(moudle_name=moudle_name, case_name=case_name,
                                                             request_method=request_method, url=request_url,
                                                             data=req_data, userId=userId)
            logging.info("返回结果：{}".format(res_text.json()))
            assert_common(res_text, msg=exc_data)

        if case_name == "职业列表信息":
            res_text = ApiFactory.get_clinicconfig().userid(moudle_name=moudle_name, case_name=case_name,
                                                            request_method=request_method, url=request_url,
                                                            data=req_data, userId=userId)
            logging.info("返回结果：{}".format(res_text.json()))
            assert_common(res_text, msg=exc_data)

