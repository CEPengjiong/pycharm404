"""
description: 断言的通用方法,断言status和message
time:
author: chenling
"""
def assert_common(res, code=200, msg=None):
    """
    通用断言状态码和message的方法
    :param res: 响应对象
    :param code: 响应状态码
    :param msg: 响应的message
    :return:
    """
    assert res.json().get("code") == code
    assert res.json().get("msg") == msg

