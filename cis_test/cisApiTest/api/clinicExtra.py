# -*- coding: utf-8 -*-
# @Time    : 2022/11/4 14:08
# @Author  : PengJiong
# @Email   : 18390050274@qq.com
# @File    : clinicExtra.py.py
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

# 格式化成2021-09-13 11:45:39形式
visitTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

class clinicExtra:
    # 功能配置
    def info(self, moudle_name, case_name, request_method, url, data):
        url = url + str(_t)
        return request_common(moudle_name, case_name, request_method, url=url, data=data)

    # 附加费用配置列表
    def clinicExtrapage(self, moudle_name, case_name, request_method, url, data):
        url = url + str(_t) + "&pageNum=1&pageSize=10&isExtra=1&isCheck=0"
        return request_common(moudle_name, case_name, request_method, url=url, data=data)

    # 新增附加费用项目
    def addclinicExtra(self, moudle_name, case_name, request_method, url, data):
        url = url + str(_t)
        return request_common(moudle_name, case_name, request_method, url=url, data=data)

    # 附加费用配置列表1
    def clinicExtrapage1(self, moudle_name, case_name, request_method, url, data):
        url = url + str(_t) + "&pageNum=1&pageSize=10&isExtra=1&isCheck=0"
        return request_common(moudle_name, case_name, request_method, url=url, data=data)

    # 新增附加费用详细信息
    def chlinicclinicExtra(self, moudle_name, case_name, request_method, url, data, extraId):
        url = url + str(extraId) + "?_t=" + str(_t)
        return request_common(moudle_name, case_name, request_method, url=url, data=data)

#  sssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssss

    # 新增检验治疗
    def addclinicExtra(self, moudle_name, case_name, request_method, url, data):
        url = url + str(_t)
        return request_common(moudle_name, case_name, request_method, url=url, data=data)

    # 检验治疗列表
    def extralist(self, moudle_name, case_name, request_method, url, data):
        url = url + str(_t) + "&pageNum=1&pageSize=10&isExtra=0&isCheck=1"
        return request_common(moudle_name, case_name, request_method, url=url, data=data)

    # 查看新增检验治疗详细
    def addExtraXiangxi(self, moudle_name, case_name, request_method, url, data):
        url = url + str(_t)
        return request_common(moudle_name, case_name, request_method, url=url, data=data)

    # 检验治疗列表1
    def extralist1(self, moudle_name, case_name, request_method, url, data):
        url = url + str(_t) + "&pageNum=1&pageSize=10&isExtra=0&isCheck=1"
        return request_common(moudle_name, case_name, request_method, url=url, data=data)

    # 挂号费设置
    def doctorregistrationpage(self, moudle_name, case_name, request_method, url, data):
        url = url + str(_t) + "&pageNum=1&pageSize=10"
        return request_common(moudle_name, case_name, request_method, url=url, data=data)

    # 科室列表显示
    def clinicdeptlist(self, moudle_name, case_name, request_method, url, data):
        url = url + str(_t)
        return request_common(moudle_name, case_name, request_method, url=url, data=data)

    # 用户列表
    def clinicuserlist(self, moudle_name, case_name, request_method, url, data):
        url = url + str(_t)
        return request_common(moudle_name, case_name, request_method, url=url, data=data)

    # 湖北各类挂号费
    def hubeiservicepage(self, moudle_name, case_name, request_method, url, data):
        url = url + str(_t) + "&pageNum=1&pageSize=10&name="
        return request_common(moudle_name, case_name, request_method, url=url, data=data)

    # 医生挂号费默认设置
    def doctorregistration(self, moudle_name, case_name, request_method, url, data):
        url = url + str(_t)
        return request_common(moudle_name, case_name, request_method, url=url, data=data)

    # 挂号费设置1
    def doctorregistrationpage1(self, moudle_name, case_name, request_method, url, data):
        url = url + str(_t) + "&pageNum=1&pageSize=10"
        return request_common(moudle_name, case_name, request_method, url=url, data=data)

    # 挂号费临时费用显示
    def getClinicRegisterFree(self, moudle_name, case_name, request_method, url, data):
        url = url + str(_t)
        return request_common(moudle_name, case_name, request_method, url=url, data=data)

    # 医生注册显示
    def doctorregistration(self, moudle_name, case_name, request_method, url, data):
        url = url
        return request_common(moudle_name, case_name, request_method, url=url, data=data)

# SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS

    # 患者标签设置
    def patientTagpage(self, moudle_name, case_name, request_method, url, data):
        url = url + str(_t) + "&pageNum=1&pageSize=10"
        return request_common(moudle_name, case_name, request_method, url=url, data=data)

    # 新增患者标签
    def addpatientTag(self, moudle_name, case_name, request_method, url, data):
        url = url + str(_t)
        return request_common(moudle_name, case_name, request_method, url=url, data=data)

    # 患者标签设置1
    def patientTagpage1(self, moudle_name, case_name, request_method, url, data):
        url = url + str(_t) + "&pageNum=1&pageSize=10"
        return request_common(moudle_name, case_name, request_method, url=url, data=data)

    # 查看患者详情
    def patientTagxq(self, moudle_name, case_name, request_method, url, data, tagId):
        url = url + str(tagId) + "?_t=" + str(_t)
        return request_common(moudle_name, case_name, request_method, url=url, data=data)

    # 修改患者标签
    def clinicpatientTag(self, moudle_name, case_name, request_method, url, data, tagId, clinicId, createBy, updateBy):
        url = url
        data["clinicId"] = clinicId
        data["createBy"] = createBy
        data["tagId"] = tagId
        data["updateBy"] = updateBy
        return request_common(moudle_name, case_name, request_method, url=url, data=data)

    # 删除患者详情
    def delpatientTag(self, moudle_name, case_name, request_method, url, data, tagId):
        url = url + str(tagId)
        return request_common(moudle_name, case_name, request_method, url=url, data=data)

# ssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssss

    # 查看用户信息
    def getUser(self, moudle_name, case_name, request_method, url, data):
        url = url + str(_t)
        return request_common(moudle_name, case_name, request_method, url=url, data=data)
