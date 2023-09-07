"""
description: 封装通用request请求
time:
author: chenling
"""

import requests
import api_config
import logging
import urllib3
urllib3.disable_warnings()

def request_common( moudle_name, case_name, request_method, url, data):
    host_url = api_config.get_env()
    url = host_url + url
    logging.info("模块：{}    用例名称：{}\n请求方式：{}\n请求地址的url：{}；\n请求的body:{}".format(moudle_name, case_name, request_method, url, data))
    try:
        if request_method == 'get':
            return requests.get(url=url, headers=api_config.request_header, json=data, verify=False)
        elif request_method == 'post':
            return requests.post(url=url, headers=api_config.request_header, json=data, verify=False)
        elif request_method == 'put':
            return requests.put(url=url, headers=api_config.request_header, json=data, verify=False)
        elif request_method == 'DELETE':
            return requests.delete(url=url, headers=api_config.request_header, json=data, verify=False)
        else:
            print("未定义的接口请求方式!", request_method)
    except Exception as w:
        raise ValueError("接口请求失败！", w)
