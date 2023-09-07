"""
description: 封装库存汇总接口
time: 2022/4/13
author: chenling
"""
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

class medicineStock:
    # 库存汇总列表
    def medicineStockpage(self, moudle_name, case_name, request_method, url, data):
        url = url + str(_t) + "&pageNum=1&pageSize=10&beginTime=&endTime="
        return request_common(moudle_name, case_name, request_method, url=url, data=data)

    # 库存总金额
    def profit(self, moudle_name, case_name, request_method, url, data):
        url = url + str(_t)
        return request_common(moudle_name, case_name, request_method, url=url, data=data)

    # 库存详情
    def medicineStockDetail(self, moudle_name, case_name, request_method, url, data, medicineId):
        if case_name == "销售明细":
            url = url + str(_t) + "&medicineId=" + str(medicineId) + "&pageNum=1&pageSize=20&orderType=&beginTime=&endTime="
        if case_name == "库存流水":
            url = url + str(_t) + "&pageNum=1&pageSize=10&type=0&medicineId=" + str(medicineId) + "&beginTime=&endTime="
        if case_name == "批次":
            url = url + str(_t) + "&pageNum=1&pageSize=10&type=3&medicineId=" + str(medicineId) + "&beginTime=&endTime="
        return request_common(moudle_name, case_name, request_method, url=url, data=data)