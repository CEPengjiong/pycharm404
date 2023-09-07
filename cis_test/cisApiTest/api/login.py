"""
description: 封装登录接口
time: 2021/12/02
author: chenling
"""
import api_config
import requests
from utils.request_common import request_common

class Login:

    def login(self, moudle_name, case_name, request_method, url, data):

        return request_common(moudle_name, case_name, request_method, url=url, data=data)

