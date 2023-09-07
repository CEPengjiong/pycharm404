# -*- coding: utf-8 -*-
# @Time    : 2022/3/24 16:46
# @Author  : PengJiong
# @Email   : 18390050274@qq.com
# @File    : clinicDailyInfo.py.py

import time
from utils.request_common import request_common
import datetime as DT
import api_config

endtime = DT.date.today()
beginTime = endtime - DT.timedelta(days=10)
t = time.time()
_t = int(t)

# 格式化成2021-09-13 11:45:39形式
visitTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

class clinicDailInfo:
    # 机构信息获取
    def getinfo(self, moudle_name, case_name, request_method, url, data):
        url = url + str(_t)
        return request_common(moudle_name,case_name, request_method, url=url, data=data)

    #今日日报
    def clinicDailInfo(self, moudle_name, case_name, request_method, url, data):
        url = url + str(_t) + "&createTime=2022-03-25"
        return request_common(moudle_name, case_name, request_method, url=url, data=data)

    #时间筛选查询
    def tClinicDailyShare(self, moudle_name, case_name, request_method, url, data):
        url = url + str(_t) + "&createTime=2022-03-25"
        return request_common(moudle_name, case_name, request_method, url=url, data=data)

    #查看趋势图
    def tClinicDailyPage(self, moudle_name, case_name, request_method, url, data):
        url = url + str(_t) + "&beginTime=2022-03-24&endTime=2022-03-31"
        return request_common(moudle_name, case_name, request_method, url=url, data=data)

    #收费明细表
    def clinicdeptlist(self, moudle_name, case_name, request_method, url, data):
        url = url + str(_t)
        return request_common(moudle_name, case_name, request_method, url=url, data=data)

    # 费用统计
    def chargeStatistics(self, moudle_name, case_name, request_method, url, data):
        url = url + str(_t) + "&beginTime=2022-04-01&endTime=2022-04-01"
        return request_common(moudle_name, case_name, request_method, url=url, data=data)

    # 收费详情
    def chargeDetails(self, moudle_name, case_name, request_method, url, data):
        url = url + str(_t) + "&pageNum=1&pageSize=10&beginTime=2022-03-01&endTime=2022-03-31"
        return request_common(moudle_name, case_name, request_method, url=url, data=data)

    # 销售明细
    def getTVisitOrderDetailPage(self, moudle_name, case_name, request_method, url, data):
        url = url + str(_t) + "&pageNum=1&pageSize=10&beginTime=2022-03-01&endTime=2022-03-31"
        return request_common(moudle_name, case_name, request_method, url=url, data=data)

    # 科室统计
    def departmentStatistics(self, moudle_name, case_name, request_method, url, data):
        url = url + str(_t) + "&beginTime=2022-04-01&endTime=2022-04-01"
        return request_common(moudle_name, case_name, request_method, url=url, data=data)

    # 医生业绩统计
    def performanceStatistics(self, moudle_name, case_name, request_method, url, data, clinicId):
        data["clinicId"] = clinicId
        url = url + str(_t)
        return request_common(moudle_name, case_name, request_method, url=url, data=data)

    # ----------------------------------------------------------------

    # 用户信息获取
    def getuserlist(self, moudle_name, case_name, request_method, url, data):
        url = url +str(_t)
        return request_common(moudle_name, case_name, request_method, url=url, data=data)

    # 门诊日志
    def page(self, moudle_name, case_name, request_method, url, data):
        url = url + str(_t)
        return request_common(moudle_name, case_name, request_method, url=url, data=data)

    # 进销存统计
    def invoicingStatistics(self, moudle_name, case_name, request_method, url, data, clinicId):
        data["clinicId"] = clinicId
        url = url + str(_t)
        return request_common(moudle_name, case_name, request_method, url=url, data=data)

    # 出入库统计
    def stockStatistics(self, moudle_name, case_name, request_method, url, data, clinicId):
        data["clinicId"] = clinicId
        url = url + str(_t)
        return request_common(moudle_name, case_name, request_method, url=url, data=data)

    # 供应商统计
    def supplierStatistics(self, moudle_name, case_name, request_method, url, data):
        url = url + str(_t)
        return request_common(moudle_name, case_name, request_method, url=url, data=data)