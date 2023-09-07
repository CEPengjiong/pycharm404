#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 用pip3命令安装
import requests
from ruamel import PyYAML
import json


def test_loginToGetToken():
    host = 'http://xx.xx.xx.xx:xx/'#接口地址ip与port
    url = host + "login"
    #登录的参数数据
    data = {
        'userName': '159592055xx',
        'loginType': 2,
        'password': '123123'
    }
    #登录请求头部信息
    headers = {'Content-Type': 'application/json'}
    # 初始化url请求对象
    response = requests.post(url=url, data=json.dumps(data), headers=headers)

    # print(response.text)
    # print(response.status_code)
    # print(response.json()["data"]["token"])
    # return response.json()["token"]

    # 把token值写入配置文件中
    yamlpath = r'D:\autotest\api\628x\Token.yaml'#保存文件路径
    #提取token字段
    tokenValue = {
        'token': response.json()["data"]["token"]
    }
    with open(yamlpath, "w", encoding="utf-8") as f:
        PyYAML.dump(tokenValue, f, Dumper=yaml.RoundTripDumper)


if __name__ == "__main__":
    test_loginToGetToken()
