# -*- coding: utf-8 -*-
# @Time    : 2022/9/14 9:48
# @Author  : PengJiong
# @Email   : 18390050274@qq.com
# @File    : clinicconfig.py
import time
from utils.request_common import request_common
import datetime as DT
from utils.random_phone import random_name
import api_config

# 转换成13位时间戳
endTime = DT.date.today()
beginTime = endTime - DT.timedelta(days=10)
t = time.time()
_t = int(t)

A = str("萨德主义")
# 格式化成2021-09-13 11:45:39形式
visitTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

class clinicconfig:

    # 功能配置
    def info(self, moudle_name, case_name, request_method, url, data):
        url = url + str(_t)
        return request_common(moudle_name, case_name, request_method, url=url, data=data)

    # 中西成药模板配置
    def synthetic(self, moudle_name, case_name, request_method, url, data):
        url = url + str(_t)
        return request_common(moudle_name, case_name, request_method, url=url, data=data)

    # 注射模板配置
    def infusion(self, moudle_name, case_name, request_method, url, data):
        url = url + str(_t)
        return request_common(moudle_name, case_name, request_method, url=url, data=data)

    # 中药模板配置
    def chinese(self, moudle_name, case_name, request_method, url, data):
        url = url + str(_t)
        return request_common(moudle_name, case_name, request_method, url=url, data=data)

    # 敷贴模板配置
    def applicator(self, moudle_name, case_name, request_method, url, data):
        url = url + str(_t)
        return request_common(moudle_name, case_name, request_method, url=url, data=data)

    # 机构信息获取
    def getinfo(self, moudle_name, case_name, request_method, url, data):
        url = url + str(_t)
        return request_common(moudle_name, case_name, request_method, url=url, data=data)

    # 疾病类型
    def tdiseasetype(self, moudle_name, case_name, request_method, url, data):
        url = url + str(_t) + "&pageNum=1&pageSize=10"
        return request_common(moudle_name, case_name, request_method, url=url, data=data)

    # 新增疾病类型
    def xinzengjibing(self, moudle_name, case_name, request_method, url, data):
        url = url + str(_t)
        return request_common(moudle_name, case_name, request_method, url=url, data=data)

    # 疾病类型2
    def tdiseasetype2(self, moudle_name, case_name, request_method, url, data):
        url = url + str(_t) + "&pageNum=1&pageSize=10"
        return request_common(moudle_name, case_name, request_method, url=url, data=data)

    # 修改疾病类型
    def updatajibing(self, moudle_name, case_name, request_method, url, data, typeId,
                     clinicId, source, createTime, updateTime, updateBy):
        url = url
        data["typeId"] = typeId
        data["clinicId"] = clinicId
        data["source"] = source
        data["updateBy"] = updateBy
        data["createTime"] = createTime
        data["updateTime"] = updateTime

        return request_common(moudle_name, case_name, request_method, url=url, data=data)

    # 删除疾病类型
    def deletetype(self, moudle_name, case_name, request_method, url, data, typeId):
        url = url + str(typeId)
        return request_common(moudle_name, case_name, request_method, url=url, data=data)

    # 疾病名称
    def tclinicdisease(self, moudle_name, case_name, request_method, url, data):
        url = url + str(_t) + "&pageNum=1&pageSize=10&medType=11"
        return request_common(moudle_name, case_name, request_method, url=url, data=data)

    # 疾病名称列表
    def tclinicdiseaselist(self, moudle_name, case_name, request_method, url, data):
        url = url + str(_t)
        return request_common(moudle_name, case_name, request_method, url=url, data=data)

    # 新增疾病名称
    def xinzengtclinicdisease(self, moudle_name, case_name, request_method, url, data, diseaseId, diseaseTypeId, createBy, createTime1, updateTime1):
        url = url + str(_t)
        data["diseaseId"] = diseaseId
        data["diseaseTypeId"] = diseaseTypeId
        data["createBy"] = createBy
        data["createTime1"] = createTime1
        data["updateTime1"] = updateTime1
        return request_common(moudle_name, case_name, request_method, url=url, data=data)

    # 疾病名称2
    def tclinicdisease2(self, moudle_name, case_name, request_method, url, data):
        url = url + str(_t) + "&pageNum=1&pageSize=10&medType=11"
        return request_common(moudle_name, case_name, request_method, url=url, data=data)

    # 修改疾病名称
    def updatatclinicdisease(self, moudle_name, case_name, request_method, url, data, diseaseId, clinicId, diseaseTypeId, createBy, createTime, updateTime):
        url = url
        data["diseaseId"] = diseaseId
        data["clinicId"] = clinicId
        data["diseaseTypeId"] = diseaseTypeId
        data["createBy"] = createBy
        data["createTime"] = createTime
        data["updateTime"] = updateTime
        return request_common(moudle_name, case_name, request_method, url=url, data=data)

    # 删除疾病名称
    def tclinicdiseaseDle(self, moudle_name, case_name, request_method, url, data, diseaseId):
        url = url + str(diseaseId)
        return request_common(moudle_name, case_name, request_method, url=url, data=data)

# ssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssss

    # 科室列表刷新
    def clinicdeptpage(self, moudle_name, case_name, request_method, url, data):
        url = url + str(_t) + "&pageNum=1&pageSize=20"
        return request_common(moudle_name, case_name, request_method, url=url, data=data)

    # 新增科室
    def clinicdept(self, moudle_name, case_name, request_method, url, data, deptName, hospDeptName, status, medicalDeptId):
        url = url + str(_t)
        data["deptName"] = deptName
        data["hospDeptName"] = hospDeptName
        data["status"] = status
        data["medicalDeptId"] = medicalDeptId
        return request_common(moudle_name, case_name, request_method, url=url, data=data)

    # 科室列表刷新1
    def clinicdeptpage1(self, moudle_name, case_name, request_method, url, data):
        url = url + str(_t) + "&pageNum=1&pageSize=20"
        return request_common(moudle_name, case_name, request_method, url=url, data=data)

    # 查看科室详细信息
    def Seedept(self, moudle_name, case_name, request_method, url, data):
        url = url + str(_t)
        return request_common(moudle_name, case_name, request_method, url=url, data=data)

    # 修改科室
    def Modifydept(self, moudle_name, case_name, request_method, url, data, deptId, clinicId, medicalDeptId, caty, hospDeptName, status, createBy, medicalDeptName, medicalDeptCode):
        url = url + str(_t)
        data["deptId"] = deptId
        data["clinicId"] = clinicId
        data["medicalDeptId"] = medicalDeptId
        data["caty"] = caty
        data["hospDeptName"] = hospDeptName
        data["status"] = status
        data["createBy"] = createBy
        data["medicalDeptName"] = medicalDeptName
        data["medicalDeptCode"] = medicalDeptCode
        return request_common(moudle_name, case_name, request_method, url=url, data=data)

    # 删除科室
    def Deldept(self, moudle_name, case_name, request_method, url, data, deptId):
        url = url + str(deptId)
        return request_common(moudle_name, case_name, request_method, url=url, data=data)

    # ssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssss

    # 新增角色
    def addrole(self, moudle_name, case_name, request_method, url, data):
        url = url + str(_t)
        return request_common(moudle_name, case_name, request_method, url=url, data=data)

    # 角色列表刷新
    def rolelist(self, moudle_name, case_name, request_method, url, data):
        url = url + str(_t) + "&pageNum=1&pageSize=10"
        return request_common(moudle_name, case_name, request_method, url=url, data=data)

    # 角色删除
    def delrole(self, moudle_name, case_name, request_method, url, data, roleId):
        url = url + str(roleId)
        return request_common(moudle_name, case_name, request_method, url=url, data=data)

    # sssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssss

    # 员工刷新列表
    def userqueryPage(self, moudle_name, case_name, request_method, url, data):
        url = url + str(_t) + "&pageNum=1&pageSize=10"
        return request_common(moudle_name, case_name, request_method, url=url, data=data)

    # 查看员工详细信息
    def userid(self, moudle_name, case_name, request_method, url, data, userId):
        url = url + str(userId) + "?_t=" + str(_t)
        return request_common(moudle_name, case_name, request_method, url=url, data=data)

    # 职业列表信息
    def clinicjoblist(self, moudle_name, case_name, request_method, url, data, userId):
        url = url + str(_t)
        return request_common(moudle_name, case_name, request_method, url=url, data=data)
