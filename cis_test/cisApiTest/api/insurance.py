# -*- coding: utf-8 -*-
# @Time    : 2022/9/13 10:28
# @Author  : PengJiong
# @Email   : 18390050274@qq.com
# @File    : insurance.py
import time
from utils.request_common import request_common
import datetime as DT
import api_config

# 转换成13位时间戳
endTime = DT.date.today()
beginTime = endTime - DT.timedelta(days=10)
t = time.time()
_t = int(t)

# 格式化成2021-09-13 11:45:39形式
visitTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

class insurance:

    # 机构信息获取
    def getinfo(self, moudle_name, case_name, request_method, url, data):
        url = url + str(_t)
        return request_common(moudle_name,case_name, request_method, url=url, data=data)

    # 医保结算单据
    def insurance(self, moudle_name, case_name, request_method, url, data, clinicId):
        url = url + str(_t) + "&clinicId=" + str(clinicId) + "&pageNum=1&pageSize=10&beginTime=" + str(api_config.today) + "&endTime=" + str(api_config.today)
        return request_common(moudle_name,case_name, request_method, url=url, data=data)

    # 医保三目匹配数据统计
    def countMedicare(self, moudle_name, case_name, request_method, url, data):
        url = url + str(_t)
        return request_common(moudle_name,case_name, request_method, url=url, data=data)

    # 医保三目匹配数据
    def listByMedicalCare(self, moudle_name, case_name, request_method, url, data):
        url = url + str(_t) + "&pageNum=1&pageSize=10&enable=1"
        return request_common(moudle_name,case_name, request_method, url=url, data=data)

    # 医保服务匹配数据
    def clinicExtra(self, moudle_name, case_name, request_method, url, data):
        url = url + str(_t) + "&pageNum=1&pageSize=10&isCheck=1&delFlag=0"
        return request_common(moudle_name,case_name, request_method, url=url, data=data)

    # 医保服务匹配数据目录外
    def medicare(self, moudle_name, case_name, request_method, url, data):
        url = url + str(_t) + "&pageNum=1&pageSize=10&name="
        return request_common(moudle_name,case_name, request_method, url=url, data=data)

    # 医保对账
    def drugSettleBill(self, moudle_name, case_name, request_method, url, data, clinicId):
        url = url + str(_t) + "&pageNum=1&pageSize=10&clinicId=" + str(clinicId) + "&startbillDate=2022-08-14&endbillDate=2022-09-13&billFlag=1&billStatus="
        return request_common(moudle_name,case_name, request_method, url=url, data=data)

    # 对账记录
    def drugSettleBillpage(self, moudle_name, case_name, request_method, url, data, clinicId):
        url = url + str(_t) + "&pageNum=1&pageSize=10&clinicId=" + str(clinicId) + "&startbillDate=2022-09-07&endbillDate=2022-09-13"
        return request_common(moudle_name,case_name, request_method, url=url, data=data)

    # 清算申请与撤销
    def clrPage(self, moudle_name, case_name, request_method, url, data, clinicId):
        url = url + str(_t) + "&pageNum=1&pageSize=10&clinicId=" + str(clinicId)
        return request_common(moudle_name,case_name, request_method, url=url, data=data)

    # 医保字典查询1
    def dictionary1(self, moudle_name, case_name, request_method, url, data):
        url = url + str(_t) + "&type=insutype"
        return request_common(moudle_name,case_name, request_method, url=url, data=data)

    # 医保字典查询2
    def dictionary2(self, moudle_name, case_name, request_method, url, data):
        url = url + str(_t) + "&type=agnter_rlts"
        return request_common(moudle_name,case_name, request_method, url=url, data=data)

    # 医保字典查询3
    def dictionary3(self, moudle_name, case_name, request_method, url, data):
        url = url + str(_t) + "&type=psn_cert_type"
        return request_common(moudle_name,case_name, request_method, url=url, data=data)

    # 进销存管理列表
    def queryUploadPage(self, moudle_name, case_name, request_method, url, data, clinicId):
        url = url + str(_t) + "&pageNum=1&pageSize=10&uploadType=1&clinicId=" + str(clinicId) + "&beginTime=2022-09-01&endTime=2022-09-13"
        return request_common(moudle_name,case_name, request_method, url=url, data=data)