"""
description: 在编写测试脚本时,每个可能需要导入多个类,因此会出现大量重复导入类,所以建一个统一入口类,返回所有接口的类
time:
author: chenling
"""
from api.login import Login
from api.clinicalReception import clinicalReception
from api.patientRegister import patientRegister
from api.selRegisterInfoList import selRegisterInfoList
from api.chargeManagement import chargeManagement
from api.templateManagement import templateManagement
from api.speedPlaceAnOrder import speedPlaceAnOrder
from api.retail import retail
from api.homePage import homePage
from api.medicineManagement import medicineManagement
from api.purchase import purchase
from api.medicineCheck import medicineCheck
from api.stockAnalyse import stockAnalyse
from api.texpiredDrugs import texpiredDrugs
from api.medicineStock import medicineStock
from api.supplier import supplier
from api.patientManagement import patientManagement
from api.patienfollowup import patienfollowup
from api.clinicDaily import clinicDaily
from api.chargeStatistics import chargeStatistics
from api.clinicLog import clinicLog
from api.supplierStatistics import supplierStatistics
from api.Integral import Integral
from api.vip import vip
from api.medicinebreakage import medicinebreakage
from api.insurance import insurance
from api.clinicconfig import clinicconfig
from api.clinicExtra import clinicExtra

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

    @classmethod
    def get_retail(cls):
        """返回药品零售接口对象"""
        return retail()

    @classmethod
    def get_homePage(cls):
        """返回首页接口对象"""
        return homePage()

    @classmethod
    def get_medicineManagement(cls):
        """返回药品管理接口对象"""
        return medicineManagement()

    @classmethod
    def get_purchase(cls):
        """返回采购入库接口对象"""
        return purchase()

    @classmethod
    def get_medicineCheck(cls):
        """返回库存盘点接口对象"""
        return medicineCheck()

    @classmethod
    def get_stockAnalyse(cls):
        """返回库存分析接口对象"""
        return stockAnalyse()

    @classmethod
    def get_texpiredDrugs(cls):
        """返回销毁记录接口对象"""
        return texpiredDrugs()

    @classmethod
    def get_medicineStock(cls):
        """返回库存汇总接口对象"""
        return medicineStock()

    @classmethod
    def get_supplier(cls):
        """返回供应商菜单接口对象"""
        return supplier()

    @classmethod
    def get_patientManagement(cls):
        """返回患者管理菜单接口对象"""
        return patientManagement()

    @classmethod
    def get_patienfollowup(cls):
        """返回随访管理菜单接口对象"""
        return patienfollowup()

    @classmethod
    def get_clinicDaily(cls):
        """返回今日日报菜单接口对象"""
        return clinicDaily()

    @classmethod
    def get_chargeStatistics(cls):
        """返回收费统计菜单接口对象"""
        return chargeStatistics()

    @classmethod
    def get_vip(cls):
        """返回会员管理菜单接口对象"""
        return vip()

    @classmethod
    def get_clinicLog(cls):
        """返回门诊日志菜单接口对象"""
        return clinicLog()

    @classmethod
    def get_supplierStatistics(cls):
        """返回供应商统计接口对象"""
        return supplierStatistics()

    @classmethod
    def get_Integral(cls):
        """返回积分管理统计接口对象"""
        return Integral()

    @classmethod
    def get_medicinebreakage(cls):
        """返回损毁管理统计接口对象"""
        return medicinebreakage()

    @classmethod
    def get_insurance(cls):
        """返回医保管理接口对象"""
        return insurance()

    @classmethod
    def get_clinicconfig(cls):
        """返回诊所配置接口对象"""
        return clinicconfig()

    @classmethod
    def get_clinicExtra(cls):
        """返回附加费用接口对象"""
        return clinicExtra()