# 封装登录api接口,包含管理端登录和大屏登录
import api_config
import requests
from utils.request_common import request_common

class Login:

    def login(self, moudle_name, case_name, request_method, url, data):

        return request_common(moudle_name, case_name, request_method, url=url, data=data)

