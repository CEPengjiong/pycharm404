"""
description: 封装收费统计接口
time: 2022/06/13
author: chenling
"""
from utils.request_common import request_common
import api_config

_t = str(api_config._t)


class chargeStatistics:

    # 收费统计查询
    def chargeStatistics(self, moudle_name, case_name, request_method, url, data):

        url = url + _t + "&beginTime=" + str(api_config.today) + "&endTime=" + str(api_config.today)

        return request_common(moudle_name, case_name, request_method, url=url, data=data)

    # 收费明细查询
    def chargeDetails(self, moudle_name, case_name, request_method, url, data):

        url = url + _t + "&pageNum=1&pageSize=10&beginTime=" + str(api_config.today) + "&endTime=" + str(api_config.today)

        return request_common(moudle_name, case_name, request_method, url=url, data=data)

    # 科室统计查询
    def departmentStatistics(self, moudle_name, case_name, request_method, url, data):

        url = url + _t + "&beginTime=" + str(api_config.today) + "&endTime=" + str(api_config.today)

        return request_common(moudle_name, case_name, request_method, url=url, data=data)