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
        "phone": "13127851205",
        "password": "63a2338451d491061a719bab16e40c2e",
        "timestamp": 1644374253481,

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
