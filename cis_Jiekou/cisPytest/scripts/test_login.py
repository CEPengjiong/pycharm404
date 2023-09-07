import logging, allure, pytest
from utils.assert_common import assert_common
import os, sys
from utils.ReadTabDataUtils import read_test_data
from api.api_factory import ApiFactory
import api_config


@allure.feature("登录")
class TestLogin:
    curPath = os.path.abspath(os.path.dirname(__file__))
    rootPath = os.path.split(curPath)[0]
    sys.path.append(rootPath)
    data_path = rootPath + r"\data\login.xls"

    ''' 
    @allure.severity装饰器按严重性级别来标记case　　　
    执行指定测试用例 --allure-severities blocker
    BLOCKER = 'blocker'　　阻塞缺陷
    CRITICAL = 'critical'　严重缺陷
    NORMAL = 'normal'　　  一般缺陷
    MINOR = 'minor'　　    次要缺陷
    TRIVIAL = 'trivial'　　轻微缺陷　
    '''


    @allure.story("登录接口测试")
    @allure.severity("normal")
    @allure.description("登录接口测试")
    @pytest.mark.parametrize("moudle_name,case_name,request_method,request_url,req_data,code,exc_data", read_test_data(data_path, "Sheet1", None, 1, 2, 3, 4, 7, 8, 9))
    def test_login_case(self, moudle_name, case_name, request_method, request_url, req_data, code, exc_data):

            res_text = ApiFactory.get_login().login(moudle_name=moudle_name, case_name=case_name, request_method=request_method, url=request_url, data=eval(req_data))
            logging.info("返回结果：{}".format(res_text.json()))
            assert_common(res_text, code=code, msg=exc_data)
