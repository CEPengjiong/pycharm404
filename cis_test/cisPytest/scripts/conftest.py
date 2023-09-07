import api_config
import logging
import pytest
import requests
from utils.assert_common import assert_common
# 诊所端登录通用方法

@pytest.fixture(scope = "session" )
def clinic_login():
    """诊所端登录"""

    data = {
        # "phone": "18111111111",
        # "password": "9aa63df3f30a64b0a469974bcfab3202",
        # "timestamp": 1651218884987,
        "phone": "18390050274",
        "password": "8c5d6f0eac443ecdbc863b55c95485e3",
        "timestamp": 1652349864714,
    }
    host_url = api_config.get_env()
    url = host_url + '/prod-api/auth/switchLogin/clinicList'
    res_login = requests.post(url=url, headers=api_config.request_header, json=data, verify=False)

    logging.info("登录的响应数据:{}".format(res_login.json()))
    # 断言响应状态码和message
    assert_common(res_login, 200, '操作成功')
    # 保存token, Bearer+空格+token
    token = "Bearer " + res_login.json().get("data").get("access_token")
    api_config.request_header["token"] = token
    logging.info("获取到的token:{}".format(token))
    return token
