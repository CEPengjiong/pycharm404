# 在编写测试脚本时,每个可能需要导入多个类,因此会出现大量重复导入类,所以建一个统一入口类,返回所有接口的类
from api.login import Login
from api.clinicalReception import clinicalReception
from api.patientRegister import patientRegister
from api.selRegisterInfoList import selRegisterInfoList
from api.chargeManagement import chargeManagement
from api.templateManagement import templateManagement
from api.speedPlaceAnOrder import speedPlaceAnOrder

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

    @classmethod
    def get_patientRegister(cls):
        """返回预约列表接口对象"""
        return patientRegister()

    @classmethod
    def get_selRegisterInfoList(cls):
        """返回接诊列表接口对象"""
        return selRegisterInfoList()

    @classmethod
    def get_chargeManagement(cls):
        """返回收费管理接口对象"""
        return chargeManagement()

    @classmethod
    def get_templateManagement(cls):
        """返回模板管理接口对象"""
        return templateManagement()

    @classmethod
    def get_speedPlaceAnOrder(cls):
        """返回快速接诊接口对象"""
        return speedPlaceAnOrder()