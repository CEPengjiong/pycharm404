"""
description: 封装库存统计-供应商统计菜单接口
time: 2022/6/13
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

class supplierStatistics:

    # 供应商列表
    def supplierStatistics(self, moudle_name, case_name, request_method, url, data):
        url = url + str(_t) + "&pageNum=1&pageSize=10&beginTime=" + str(api_config.week_ago) + "&endTime=" + str(api_config.today)
        return request_common(moudle_name, case_name, request_method, url=url, data=data)

    # 详情
    def supplierInfo(self, moudle_name, case_name, request_method, url, data, supplierId):
        url = url + str(supplierId) + "?_t=" + str(_t) + "&pageNum=1&pageSize=10&beginTime=" + str(api_config.week_ago) + "&endTime=" + str(api_config.today)
        return request_common(moudle_name, case_name, request_method, url=url, data=data)