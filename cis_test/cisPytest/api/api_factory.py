# -*- coding: utf-8 -*-
# @Time    : 2022/8/30 13:56
# @Author  : PengJiong
# @Email   : 18390050274@qq.com
# @File    : api.factory.py.py
# 在编写测试脚本时,每个可能需要导入多个类,因此会出现大量重复导入类,所以建一个统一入口类,返回所有接口的类
from api.clinicalReception import clinicalReception
from api.login import Login

class ApiFactory:
    """返回所有接口的统一入口类"""

    @classmethod
    def get_login(cls):
        """返回登录接口对象"""
        return Login()

    @classmethod
    def get_clinicalReception(cls):
        """返回医生接诊接口对象"""
        return clinicalReception()