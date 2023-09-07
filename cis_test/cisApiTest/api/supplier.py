"""
description: 封装供应商菜单接口
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

class supplier:

    # 供应商列表
    def supplierPage(self, moudle_name, case_name, request_method, url, data):
        url = url + str(_t) + "&total=1&pageNum=1&pageSize=10"
        return request_common(moudle_name, case_name, request_method, url=url, data=data)

    # 新增供应商
    def supplierAdd(self, moudle_name, case_name, request_method, url, data):
        url = url + str(_t)
        data["supplierName"] = "接口测试新增供应商" + str(_t)
        return (request_common(moudle_name, case_name, request_method, url=url, data=data), data["supplierName"])

    # 根据姓名查询
    def nameQuery(self, moudle_name, case_name, request_method, url, data, supplierName):

        url = url + str(_t) + "&total=6&pageNum=1&pageSize=10&supplierName=" + supplierName
        return request_common(moudle_name, case_name, request_method, url=url, data=data)

    # 编辑供应商
    def supplierEdit(self, moudle_name, case_name, request_method, url, data, supplierId):
        url = url + str(supplierId) + "?_t=" + str(_t)
        return request_common(moudle_name, case_name, request_method, url=url, data=data)

    # 确认编辑
    def editConfirm(self, moudle_name, case_name, request_method, url, data, supplierId, supplierName, clinicId, createBy, createTime):
        data["supplierId"] = supplierId
        data["supplierName"] = supplierName
        data["clinicId"] = clinicId
        data["createBy"] = createBy
        data["createTime"] =createTime
        data["updateTime"] = visitTime
        return request_common(moudle_name, case_name, request_method, url=url, data=data)

    # 删除供应商
    def supplierDelete(self, moudle_name, case_name, request_method, url, data, supplierId):
        url = url + str(supplierId)
        return request_common(moudle_name, case_name, request_method, url=url, data=data)
