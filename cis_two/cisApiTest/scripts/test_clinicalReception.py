import json
import logging
import allure
import pytest
import os
import sys
from utils.assert_common import assert_common
from utils.ReadTabDataUtils import read_test_data
from api.api_factory import ApiFactory
import api_config

@allure.feature("门诊管理模块")
class TestClinicalReception:
    curPath = os.path.abspath(os.path.dirname(__file__))
    rootPath = os.path.split(curPath)[0]
    sys.path.append(rootPath)
    data_path = rootPath + r"\data\clinicalReception.xls"

    '''
    @allure.severity装饰器按严重性级别来标记case　　　
    执行指定测试用例 --allure-severities blocker
    BLOCKER = 'blocker'　　阻塞缺陷
    CRITICAL = 'critical'　严重缺陷
    NORMAL = 'normal'　　  一般缺陷
    MINOR = 'minor'　　    次要缺陷
    TRIVIAL = 'trivial'　　轻微缺陷　
    '''


    @allure.story("医生接诊菜单")
    @allure.severity("BLOCKER")
    @allure.description("001预约挂号-接诊-收费-退费")
    @pytest.mark.parametrize("moudle_name,case_name,request_method,request_url,req_data,code,exc_data", read_test_data(data_path, "收费", None, 1, 2, 3, 4, 7, 8, 9))
    def test_charge_case(self, moudle_name, case_name, request_method, request_url, req_data, code, exc_data,clinic_login):
        # logging.info("请求的header：{}".format(api_config.request_header))
        global deptId, jobId, doctorId, registerId, visitOrderId, patientId, batchNo, total, pieceTotal, packUnit, specs, retailPrice, manufacturer, stock, id, clinicId, namePinyin, manufacturerPinyin,\
            packAmount, pieceAmount, stockId, newPrice, medicineId, expireDate, supplierId, orderType, medicineName


        if case_name == "getInfo":
            res_text = ApiFactory.get_clinicalReception().getInfo(moudle_name=moudle_name, case_name=case_name, request_method=request_method, url=request_url, data=req_data)
            logging.info("返回结果：{}".format(res_text.json()))
            assert_common(res_text, msg=exc_data)
            deptId = res_text.json().get("user").get("deptId")
            jobId = res_text.json().get("user").get("jobId")
            doctorId = res_text.json().get("user").get("userId")

        if case_name == "预约挂号":
            res_text = ApiFactory.get_clinicalReception().registration(moudle_name=moudle_name, case_name=case_name, request_method=request_method, url=request_url, data=json.loads(req_data), deptId=deptId, jobId=jobId, doctorId=doctorId)
            logging.info("返回结果：{}".format(res_text.json()))
            assert_common(res_text, msg=exc_data)
            registerId = res_text.json().get("data").get("registerId")
            patientId = res_text.json().get("data").get("patientId")

        if case_name == "创建订单":
            res_text = ApiFactory.get_clinicalReception().createVisitorder(moudle_name=moudle_name, case_name=case_name, request_method=request_method, url=request_url, data=eval(req_data), registerId=registerId)
            logging.info("返回结果：{}".format(res_text.json()))
            assert_common(res_text, msg=exc_data)

        if case_name == "订单录入":
            res_text = ApiFactory.get_clinicalReception().visitOrderDVOInfo(moudle_name=moudle_name, case_name=case_name, request_method=request_method, url=request_url, data=req_data, registerId=registerId)
            logging.info("返回结果：{}".format(res_text.json()))
            assert_common(res_text, msg=exc_data)


        if case_name == "药品搜索":
            res_text = ApiFactory.get_clinicalReception().selectMedicineStock(moudle_name=moudle_name, case_name=case_name, request_method=request_method, url=request_url, data=json.loads(req_data))
            logging.info("返回结果：{}".format(res_text.json()))
            assert_common(res_text, msg=exc_data)
            batchNo = res_text.json().get("data")[0].get("batchNo")
            total = res_text.json().get("data")[0].get("total")
            pieceTotal = res_text.json().get("data")[0].get("pieceTotal")
            packUnit = res_text.json().get("data")[0].get("packUnit")
            specs = res_text.json().get("data")[0].get("specs")
            retailPrice = res_text.json().get("data")[0].get("retailPrice")
            manufacturer = res_text.json().get("data")[0].get("manufacturer")
            stock = res_text.json().get("data")[0].get("stock")
            id = res_text.json().get("data")[0].get("id")
            clinicId = res_text.json().get("data")[0].get("clinicId")
            namePinyin = res_text.json().get("data")[0].get("namePinyin")
            manufacturerPinyin = res_text.json().get("data")[0].get("manufacturerPinyin")
            packAmount = res_text.json().get("data")[0].get("packAmount")
            pieceAmount = res_text.json().get("data")[0].get("pieceAmount")
            stockId = res_text.json().get("data")[0].get("stockId")
            newPrice = res_text.json().get("data")[0].get("newPrice")
            medicineId = res_text.json().get("data")[0].get("medicineId")
            expireDate = res_text.json().get("data")[0].get("expireDate")
            supplierId = res_text.json().get("data")[0].get("supplierId")
            medicineName = res_text.json().get("data")[0].get("medicineName")



        if case_name == "下单":
            res_text = ApiFactory.get_clinicalReception().placeAnOrder(moudle_name=moudle_name, case_name=case_name, request_method=request_method, url=request_url, data=json.loads(req_data), registerId=registerId, patientId=patientId, batchNo=batchNo,
                                                                       total=total, pieceTotal=pieceTotal, packUnit=packUnit, specs=specs, retailPrice=retailPrice,  manufacturer=manufacturer, stock=stock, id=id, clinicId=clinicId, namePinyin=namePinyin,
                                                                       manufacturerPinyin=manufacturerPinyin, packAmount=packAmount, pieceAmount=pieceAmount, stockId=stockId, newPrice=newPrice, medicineId=medicineId, expireDate=expireDate,
                                                                       supplierId=supplierId, medicineName=medicineName)
            logging.info("返回结果：{}".format(res_text.json()))
            assert_common(res_text, msg=exc_data)
            visitOrderId = res_text.json().get("data").get("visitOrder").get("id")
            orderType = res_text.json().get("data").get("visitOrder").get("orderType")
            logging.info("下单后获取到的visitOrderID为：{}".format(visitOrderId))


        if case_name == "校验是否处方药":
            res_text = ApiFactory.get_clinicalReception().checkedPrescriptionsDrug(moudle_name=moudle_name, case_name=case_name, request_method=request_method, url=request_url, data=json.loads(req_data), visitOrderId=visitOrderId, orderType=orderType)
            logging.info("返回结果：{}".format(res_text.json()))
            assert_common(res_text, msg=exc_data)

        if moudle_name == "收费发药":
            res_text = ApiFactory.get_clinicalReception().charge(moudle_name=moudle_name, case_name=case_name, request_method=request_method, url=request_url, data=json.loads(req_data), visitOrderId=visitOrderId, retailPrice=retailPrice)
            logging.info("返回结果：{}".format(res_text.json()))
            assert_common(res_text, msg=exc_data)

        if moudle_name == "收费管理查询":
            res_text = ApiFactory.get_clinicalReception().chargeManagementInfo(moudle_name=moudle_name, case_name=case_name, request_method=request_method, url=request_url, data=req_data, visitOrderId=visitOrderId)
            logging.info("返回结果：{}".format(res_text.json()))
            assert_common(res_text, msg=exc_data)
            if case_name == "退费校验":
                status = res_text.json().get("data").get("status")
                assert status == 3, "退费失败，退费后，订单号%s 返回的status!=3，实际status=%s" % (visitOrderId, status)

        if case_name == '退费':
            res_text = ApiFactory.get_clinicalReception().orderRefund(moudle_name=moudle_name, case_name=case_name, request_method=request_method, url=request_url, data=json.loads(req_data), visitOrderId=visitOrderId, retailPrice=retailPrice)
            logging.info("返回结果：{}".format(res_text.json()))
            assert_common(res_text, msg=exc_data)


    @allure.story("医生接诊菜单")
    @allure.severity("BLOCKER")
    @allure.description("002预约挂号-接诊-欠费-补交")
    @pytest.mark.parametrize("moudle_name,case_name,request_method,request_url,req_data,code,exc_data",
                                 read_test_data(data_path, "欠费", None, 1, 2, 3, 4, 7, 8, 9))
    def test_arrearage_case(self, moudle_name, case_name, request_method, request_url, req_data, code,
                                        exc_data, clinic_login):
        # logging.info("请求的header：{}".format(api_config.request_header))
        global deptId, jobId, doctorId, registerId, visitOrderId, patientId, batchNo, total, pieceTotal, packUnit, specs, retailPrice, manufacturer, stock, id, clinicId, namePinyin, manufacturerPinyin, \
                packAmount, pieceAmount, stockId, newPrice, medicineId, expireDate, supplierId, orderType, medicineName

        if case_name == "getInfo":
            res_text = ApiFactory.get_clinicalReception().getInfo(moudle_name=moudle_name, case_name=case_name,
                                                                      request_method=request_method, url=request_url,
                                                                      data=req_data)
            logging.info("返回结果：{}".format(res_text.json()))
            assert_common(res_text, msg=exc_data)
            deptId = res_text.json().get("user").get("deptId")
            jobId = res_text.json().get("user").get("jobId")
            doctorId = res_text.json().get("user").get("userId")

        if case_name == "预约挂号":
            res_text = ApiFactory.get_clinicalReception().registration(moudle_name=moudle_name, case_name=case_name,
                                                                           request_method=request_method,
                                                                           url=request_url, data=json.loads(req_data),
                                                                           deptId=deptId, jobId=jobId,
                                                                           doctorId=doctorId)
            logging.info("返回结果：{}".format(res_text.json()))
            assert_common(res_text, msg=exc_data)
            registerId = res_text.json().get("data").get("registerId")
            patientId = res_text.json().get("data").get("patientId")

        if case_name == "创建订单":
            res_text = ApiFactory.get_clinicalReception().createVisitorder(moudle_name=moudle_name,
                                                                               case_name=case_name,
                                                                               request_method=request_method,
                                                                               url=request_url, data=eval(req_data),
                                                                               registerId=registerId)
            logging.info("返回结果：{}".format(res_text.json()))
            assert_common(res_text, msg=exc_data)

        if case_name == "订单录入":
            res_text = ApiFactory.get_clinicalReception().visitOrderDVOInfo(moudle_name=moudle_name,
                                                                                case_name=case_name,
                                                                                request_method=request_method,
                                                                                url=request_url, data=req_data,
                                                                                registerId=registerId)
            logging.info("返回结果：{}".format(res_text.json()))
            assert_common(res_text, msg=exc_data)

        if case_name == "药品搜索":
            res_text = ApiFactory.get_clinicalReception().selectMedicineStock(moudle_name=moudle_name,
                                                                                  case_name=case_name,
                                                                                  request_method=request_method,
                                                                                  url=request_url,
                                                                                  data=json.loads(req_data))
            logging.info("返回结果：{}".format(res_text.json()))
            assert_common(res_text, msg=exc_data)
            batchNo = res_text.json().get("data")[0].get("batchNo")
            total = res_text.json().get("data")[0].get("total")
            pieceTotal = res_text.json().get("data")[0].get("pieceTotal")
            packUnit = res_text.json().get("data")[0].get("packUnit")
            specs = res_text.json().get("data")[0].get("specs")
            retailPrice = res_text.json().get("data")[0].get("retailPrice")
            manufacturer = res_text.json().get("data")[0].get("manufacturer")
            stock = res_text.json().get("data")[0].get("stock")
            id = res_text.json().get("data")[0].get("id")
            clinicId = res_text.json().get("data")[0].get("clinicId")
            namePinyin = res_text.json().get("data")[0].get("namePinyin")
            manufacturerPinyin = res_text.json().get("data")[0].get("manufacturerPinyin")
            packAmount = res_text.json().get("data")[0].get("packAmount")
            pieceAmount = res_text.json().get("data")[0].get("pieceAmount")
            stockId = res_text.json().get("data")[0].get("stockId")
            newPrice = res_text.json().get("data")[0].get("newPrice")
            medicineId = res_text.json().get("data")[0].get("medicineId")
            expireDate = res_text.json().get("data")[0].get("expireDate")
            supplierId = res_text.json().get("data")[0].get("supplierId")
            medicineName = res_text.json().get("data")[0].get("medicineName")

        if case_name == "下单":
            res_text = ApiFactory.get_clinicalReception().placeAnOrder(moudle_name=moudle_name, case_name=case_name,
                                                                           request_method=request_method,
                                                                           url=request_url, data=json.loads(req_data),
                                                                           registerId=registerId, patientId=patientId,
                                                                           batchNo=batchNo,
                                                                           total=total, pieceTotal=pieceTotal,
                                                                           packUnit=packUnit, specs=specs,
                                                                           retailPrice=retailPrice,
                                                                           manufacturer=manufacturer, stock=stock,
                                                                           id=id, clinicId=clinicId,
                                                                           namePinyin=namePinyin,
                                                                           manufacturerPinyin=manufacturerPinyin,
                                                                           packAmount=packAmount,
                                                                           pieceAmount=pieceAmount, stockId=stockId,
                                                                           newPrice=newPrice, medicineId=medicineId,
                                                                           expireDate=expireDate,
                                                                           supplierId=supplierId,
                                                                           medicineName=medicineName)
            logging.info("返回结果：{}".format(res_text.json()))
            assert_common(res_text, msg=exc_data)
            visitOrderId = res_text.json().get("data").get("visitOrder").get("id")
            orderType = res_text.json().get("data").get("visitOrder").get("orderType")
            logging.info("下单后获取到的visitOrderID为：{}".format(visitOrderId))

        if case_name == "校验是否处方药":
            res_text = ApiFactory.get_clinicalReception().checkedPrescriptionsDrug(moudle_name=moudle_name,
                                                                                       case_name=case_name,
                                                                                       request_method=request_method,
                                                                                       url=request_url,
                                                                                       data=json.loads(req_data),
                                                                                       visitOrderId=visitOrderId,
                                                                                       orderType=orderType)
            logging.info("返回结果：{}".format(res_text.json()))
            assert_common(res_text, msg=exc_data)

        if moudle_name == "收费发药":
            res_text = ApiFactory.get_clinicalReception().charge(moudle_name=moudle_name, case_name=case_name,
                                                                     request_method=request_method, url=request_url,
                                                                     data=json.loads(req_data),
                                                                     visitOrderId=visitOrderId, retailPrice=retailPrice)
            logging.info("返回结果：{}".format(res_text.json()))
            assert_common(res_text, msg=exc_data)

        if moudle_name == "收费管理查询":
            res_text = ApiFactory.get_clinicalReception().chargeManagementInfo(moudle_name=moudle_name,
                                                                                   case_name=case_name,
                                                                                   request_method=request_method,
                                                                                   url=request_url, data=req_data,
                                                                                   visitOrderId=visitOrderId)
            logging.info("返回结果：{}".format(res_text.json()))
            assert_common(res_text, msg=exc_data)



    @allure.story("医生接诊菜单")
    @allure.severity("BLOCKER")
    @allure.description("003预约挂号-接诊-划价-收费")
    @pytest.mark.parametrize("moudle_name,case_name,request_method,request_url,req_data,code,exc_data",
                                 read_test_data(data_path, "划价", None, 1, 2, 3, 4, 7, 8, 9))
    def test_placeAnOrder_case(self, moudle_name, case_name, request_method, request_url, req_data, code,
                                exc_data, clinic_login):
        # logging.info("请求的header：{}".format(api_config.request_header))
        global deptId, jobId, doctorId, registerId, visitOrderId, patientId, batchNo, total, pieceTotal, packUnit, specs, retailPrice, manufacturer, stock, id, clinicId, namePinyin, manufacturerPinyin, \
                packAmount, pieceAmount, stockId, newPrice, medicineId, expireDate, supplierId, orderType, medicineName, orderNo

        if case_name == "getInfo":
            res_text = ApiFactory.get_clinicalReception().getInfo(moudle_name=moudle_name, case_name=case_name,
                                                                      request_method=request_method, url=request_url,
                                                                      data=req_data)
            logging.info("返回结果：{}".format(res_text.json()))
            assert_common(res_text, msg=exc_data)
            deptId = res_text.json().get("user").get("deptId")
            jobId = res_text.json().get("user").get("jobId")
            doctorId = res_text.json().get("user").get("userId")

        if case_name == "预约挂号":
            res_text = ApiFactory.get_clinicalReception().registration(moudle_name=moudle_name, case_name=case_name,
                                                                           request_method=request_method,
                                                                           url=request_url, data=json.loads(req_data),
                                                                           deptId=deptId, jobId=jobId,
                                                                           doctorId=doctorId)
            logging.info("返回结果：{}".format(res_text.json()))
            assert_common(res_text, msg=exc_data)
            registerId = res_text.json().get("data").get("registerId")
            patientId = res_text.json().get("data").get("patientId")

        if case_name == "创建订单":
            res_text = ApiFactory.get_clinicalReception().createVisitorder(moudle_name=moudle_name,
                                                                               case_name=case_name,
                                                                               request_method=request_method,
                                                                               url=request_url, data=eval(req_data),
                                                                               registerId=registerId)
            logging.info("返回结果：{}".format(res_text.json()))
            assert_common(res_text, msg=exc_data)

        if case_name == "订单录入":
            res_text = ApiFactory.get_clinicalReception().visitOrderDVOInfo(moudle_name=moudle_name,
                                                                                case_name=case_name,
                                                                                request_method=request_method,
                                                                                url=request_url, data=req_data,
                                                                                registerId=registerId)
            logging.info("返回结果：{}".format(res_text.json()))
            assert_common(res_text, msg=exc_data)

        if case_name == "药品搜索":
            res_text = ApiFactory.get_clinicalReception().selectMedicineStock(moudle_name=moudle_name, case_name=case_name , request_method=request_method, url=request_url, data=json.loads(req_data))
            logging.info("返回结果：{}".format(res_text.json()))
            assert_common(res_text, msg=exc_data)
            batchNo = res_text.json().get("data")[0].get("batchNo")
            total = res_text.json().get("data")[0].get("total")
            pieceTotal = res_text.json().get("data")[0].get("pieceTotal")
            packUnit = res_text.json().get("data")[0].get("packUnit")
            specs = res_text.json().get("data")[0].get("specs")
            retailPrice = res_text.json().get("data")[0].get("retailPrice")
            manufacturer = res_text.json().get("data")[0].get("manufacturer")
            stock = res_text.json().get("data")[0].get("stock")
            id = res_text.json().get("data")[0].get("id")
            clinicId = res_text.json().get("data")[0].get("clinicId")
            namePinyin = res_text.json().get("data")[0].get("namePinyin")
            manufacturerPinyin = res_text.json().get("data")[0].get("manufacturerPinyin")
            packAmount = res_text.json().get("data")[0].get("packAmount")
            pieceAmount = res_text.json().get("data")[0].get("pieceAmount")
            stockId = res_text.json().get("data")[0].get("stockId")
            newPrice = res_text.json().get("data")[0].get("newPrice")
            medicineId = res_text.json().get("data")[0].get("medicineId")
            expireDate = res_text.json().get("data")[0].get("expireDate")
            supplierId = res_text.json().get("data")[0].get("supplierId")
            medicineName = res_text.json().get("data")[0].get("medicineName")

        if case_name == "下单":
            res_text = ApiFactory.get_clinicalReception().placeAnOrder(moudle_name=moudle_name, case_name=case_name,
                                                                           request_method=request_method,
                                                                           url=request_url, data=json.loads(req_data),
                                                                           registerId=registerId, patientId=patientId,
                                                                           batchNo=batchNo,
                                                                           total=total, pieceTotal=pieceTotal,
                                                                           packUnit=packUnit, specs=specs,
                                                                           retailPrice=retailPrice,
                                                                           manufacturer=manufacturer, stock=stock,
                                                                           id=id, clinicId=clinicId,
                                                                           namePinyin=namePinyin,
                                                                           manufacturerPinyin=manufacturerPinyin,
                                                                           packAmount=packAmount,
                                                                           pieceAmount=pieceAmount, stockId=stockId,
                                                                           newPrice=newPrice, medicineId=medicineId,
                                                                           expireDate=expireDate,
                                                                           supplierId=supplierId,
                                                                           medicineName=medicineName)
            logging.info("返回结果：{}".format(res_text.json()))
            assert_common(res_text, msg=exc_data)
            visitOrderId = res_text.json().get("data").get("visitOrder").get("id")
            orderType = res_text.json().get("data").get("visitOrder").get("orderType")
            logging.info("下单后获取到的visitOrderID为：{}".format(visitOrderId))

        if moudle_name == "收费管理查询":
            res_text = ApiFactory.get_clinicalReception().chargeManagementInfo(moudle_name=moudle_name, case_name=case_name, request_method=request_method, url=request_url, data=req_data, visitOrderId=visitOrderId)
            logging.info("返回结果：{}".format(res_text.json()))
            assert_common(res_text, msg=exc_data)
            orderNo = res_text.json().get("data").get("drugSubstratStockDtos")[0].get("orderNo")

        if case_name == "检验结算单":
            res_text = ApiFactory.get_clinicalReception().check(moudle_name=moudle_name, case_name=case_name, request_method=request_method, url=request_url, data=eval(req_data), visitOrderId=visitOrderId)
            logging.info("返回结果：{}".format(res_text.json()))
            assert_common(res_text, msg=exc_data)

        if case_name == "校验是否处方药":
            res_text = ApiFactory.get_clinicalReception().checkedPrescriptionsDrug(moudle_name=moudle_name, case_name=case_name, request_method=request_method, url=request_url, data=json.loads(req_data), visitOrderId=visitOrderId, orderType=orderType)
            logging.info("返回结果：{}".format(res_text.json()))
            assert_common(res_text, msg=exc_data)

        if moudle_name == "收费发药":
            res_text = ApiFactory.get_clinicalReception().charge(moudle_name=moudle_name, case_name=case_name, request_method=request_method, url=request_url, data=json.loads(req_data), visitOrderId=visitOrderId, retailPrice=retailPrice)
            logging.info("返回结果：{}".format(res_text.json()))
            assert_common(res_text, msg=exc_data)

        if case_name == "打印处方笺":
            res_text = ApiFactory.get_clinicalReception().printPrescription(moudle_name=moudle_name, case_name=case_name,request_method=request_method, url=request_url, data=req_data, orderNo=orderNo)
            logging.info("返回结果：{}".format(res_text.json()))
            assert_common(res_text, msg=exc_data)


    @allure.story("医生接诊菜单")
    @allure.severity("BLOCKER")
    @allure.description("004预约挂号-接诊-划价-退回处方-取消接诊")
    @pytest.mark.parametrize("moudle_name,case_name,request_method,request_url,req_data,code,exc_data", read_test_data(data_path, "退回处方", None, 1, 2, 3, 4, 7, 8, 9))
    def test_returnPrescription_case(self, moudle_name, case_name, request_method, request_url, req_data, code,
                                exc_data, clinic_login):
        # logging.info("请求的header：{}".format(api_config.request_header))
        global deptId, jobId, doctorId, registerId, visitOrderId, patientId, batchNo, total, pieceTotal, packUnit, specs, retailPrice, manufacturer, stock, id, clinicId, namePinyin, manufacturerPinyin, \
                packAmount, pieceAmount, stockId, newPrice, medicineId, expireDate, supplierId, orderType, medicineName, medicalRecordId, registerId2

        if case_name == "getInfo":
            res_text = ApiFactory.get_clinicalReception().getInfo(moudle_name=moudle_name, case_name=case_name,
                                                                      request_method=request_method, url=request_url,
                                                                      data=req_data)
            logging.info("返回结果：{}".format(res_text.json()))
            assert_common(res_text, msg=exc_data)
            deptId = res_text.json().get("user").get("deptId")
            jobId = res_text.json().get("user").get("jobId")
            doctorId = res_text.json().get("user").get("userId")

        if case_name == "预约挂号":
            res_text = ApiFactory.get_clinicalReception().registration(moudle_name=moudle_name, case_name=case_name,
                                                                           request_method=request_method,
                                                                           url=request_url, data=json.loads(req_data),
                                                                           deptId=deptId, jobId=jobId,
                                                                           doctorId=doctorId)
            logging.info("返回结果：{}".format(res_text.json()))
            assert_common(res_text, msg=exc_data)
            registerId = res_text.json().get("data").get("registerId")
            patientId = res_text.json().get("data").get("patientId")

        if case_name == "创建订单":
            res_text = ApiFactory.get_clinicalReception().createVisitorder(moudle_name=moudle_name,
                                                                               case_name=case_name,
                                                                               request_method=request_method,
                                                                               url=request_url, data=eval(req_data),
                                                                               registerId=registerId)
            logging.info("返回结果：{}".format(res_text.json()))
            assert_common(res_text, msg=exc_data)

        if case_name == "订单录入":
            res_text = ApiFactory.get_clinicalReception().visitOrderDVOInfo(moudle_name=moudle_name,
                                                                                case_name=case_name,
                                                                                request_method=request_method,
                                                                                url=request_url, data=req_data,
                                                                                registerId=registerId)
            logging.info("返回结果：{}".format(res_text.json()))
            assert_common(res_text, msg=exc_data)

        if case_name == "药品搜索":
            res_text = ApiFactory.get_clinicalReception().selectMedicineStock(moudle_name=moudle_name, case_name=case_name , request_method=request_method, url=request_url, data=json.loads(req_data))
            logging.info("返回结果：{}".format(res_text.json()))
            assert_common(res_text, msg=exc_data)
            batchNo = res_text.json().get("data")[0].get("batchNo")
            total = res_text.json().get("data")[0].get("total")
            pieceTotal = res_text.json().get("data")[0].get("pieceTotal")
            packUnit = res_text.json().get("data")[0].get("packUnit")
            specs = res_text.json().get("data")[0].get("specs")
            retailPrice = res_text.json().get("data")[0].get("retailPrice")
            manufacturer = res_text.json().get("data")[0].get("manufacturer")
            stock = res_text.json().get("data")[0].get("stock")
            id = res_text.json().get("data")[0].get("id")
            clinicId = res_text.json().get("data")[0].get("clinicId")
            namePinyin = res_text.json().get("data")[0].get("namePinyin")
            manufacturerPinyin = res_text.json().get("data")[0].get("manufacturerPinyin")
            packAmount = res_text.json().get("data")[0].get("packAmount")
            pieceAmount = res_text.json().get("data")[0].get("pieceAmount")
            stockId = res_text.json().get("data")[0].get("stockId")
            newPrice = res_text.json().get("data")[0].get("newPrice")
            medicineId = res_text.json().get("data")[0].get("medicineId")
            expireDate = res_text.json().get("data")[0].get("expireDate")
            supplierId = res_text.json().get("data")[0].get("supplierId")
            medicineName = res_text.json().get("data")[0].get("medicineName")

        if case_name == "下单":
            res_text = ApiFactory.get_clinicalReception().placeAnOrder(moudle_name=moudle_name, case_name=case_name,
                                                                           request_method=request_method,
                                                                           url=request_url, data=json.loads(req_data),
                                                                           registerId=registerId, patientId=patientId,
                                                                           batchNo=batchNo,
                                                                           total=total, pieceTotal=pieceTotal,
                                                                           packUnit=packUnit, specs=specs,
                                                                           retailPrice=retailPrice,
                                                                           manufacturer=manufacturer, stock=stock,
                                                                           id=id, clinicId=clinicId,
                                                                           namePinyin=namePinyin,
                                                                           manufacturerPinyin=manufacturerPinyin,
                                                                           packAmount=packAmount,
                                                                           pieceAmount=pieceAmount, stockId=stockId,
                                                                           newPrice=newPrice, medicineId=medicineId,
                                                                           expireDate=expireDate,
                                                                           supplierId=supplierId,
                                                                           medicineName=medicineName)
            logging.info("返回结果：{}".format(res_text.json()))
            assert_common(res_text, msg=exc_data)
            visitOrderId = res_text.json().get("data").get("visitOrder").get("id")
            orderType = res_text.json().get("data").get("visitOrder").get("orderType")
            logging.info("下单后获取到的visitOrderID为：{}".format(visitOrderId))

        if case_name == "查询病历id":
            res_text = ApiFactory.get_clinicalReception().orderCancelVerify(moudle_name=moudle_name, case_name=case_name, request_method=request_method, url=request_url, data=req_data, visitOrderId=visitOrderId)
            logging.info("返回结果：{}".format(res_text.json()))
            assert_common(res_text, msg=exc_data)
            medicalRecordId = res_text.json().get("data").get("medicalRecordId")

        if case_name == "退回处方":
            res_text = ApiFactory.get_clinicalReception().returnPrescription(moudle_name=moudle_name, case_name=case_name, request_method=request_method, url=request_url, data=req_data, medicalRecordId=medicalRecordId)
            logging.info("返回结果：{}".format(res_text.json()))
            assert_common(res_text, msg=exc_data)

        if case_name == "获取预约id":
            res_text = ApiFactory.get_clinicalReception().getRegisterList2(moudle_name=moudle_name, case_name=case_name, request_method=request_method, url=request_url, data=req_data)
            logging.info("返回结果：{}".format(res_text.json()))
            assert_common(res_text, msg=exc_data)
            registerId2 = res_text.json().get("data").get("records")[0].get("registerId")
            print("获取registerId2的值：", registerId2)

        if case_name == "取消接诊":
            res_text = ApiFactory.get_clinicalReception().deletePatientRegister(moudle_name=moudle_name, case_name=case_name, request_method=request_method, url=request_url, data=req_data, registerId2=registerId2)
            logging.info("返回结果：{}".format(res_text.json()))
            assert_common(res_text, msg=exc_data)

    @allure.story("医生接诊菜单")
    @allure.severity("BLOCKER")
    @allure.description("005预约挂号-接诊-划价-取消收费")
    @pytest.mark.parametrize("moudle_name,case_name,request_method,request_url,req_data,code,exc_data", read_test_data(data_path, "取消收费", None, 1, 2, 3, 4, 7, 8, 9))
    def test_returnPrescription_case(self, moudle_name, case_name, request_method, request_url, req_data, code,
                                exc_data, clinic_login):
        # logging.info("请求的header：{}".format(api_config.request_header))
        global deptId, jobId, doctorId, registerId, visitOrderId, patientId, batchNo, total, pieceTotal, packUnit, specs, retailPrice, manufacturer, stock, id, clinicId, namePinyin, manufacturerPinyin, \
                packAmount, pieceAmount, stockId, newPrice, medicineId, expireDate, supplierId, orderType, medicineName

        if case_name == "getInfo":
            res_text = ApiFactory.get_clinicalReception().getInfo(moudle_name=moudle_name, case_name=case_name,
                                                                      request_method=request_method, url=request_url,
                                                                      data=req_data)
            logging.info("返回结果：{}".format(res_text.json()))
            assert_common(res_text, msg=exc_data)
            deptId = res_text.json().get("user").get("deptId")
            jobId = res_text.json().get("user").get("jobId")
            doctorId = res_text.json().get("user").get("userId")

        if case_name == "预约挂号":
            res_text = ApiFactory.get_clinicalReception().registration(moudle_name=moudle_name, case_name=case_name,
                                                                           request_method=request_method,
                                                                           url=request_url, data=json.loads(req_data),
                                                                           deptId=deptId, jobId=jobId,
                                                                           doctorId=doctorId)
            logging.info("返回结果：{}".format(res_text.json()))
            assert_common(res_text, msg=exc_data)
            registerId = res_text.json().get("data").get("registerId")
            patientId = res_text.json().get("data").get("patientId")

        if case_name == "创建订单":
            res_text = ApiFactory.get_clinicalReception().createVisitorder(moudle_name=moudle_name,
                                                                               case_name=case_name,
                                                                               request_method=request_method,
                                                                               url=request_url, data=eval(req_data),
                                                                               registerId=registerId)
            logging.info("返回结果：{}".format(res_text.json()))
            assert_common(res_text, msg=exc_data)

        if case_name == "订单录入":
            res_text = ApiFactory.get_clinicalReception().visitOrderDVOInfo(moudle_name=moudle_name,
                                                                                case_name=case_name,
                                                                                request_method=request_method,
                                                                                url=request_url, data=req_data,
                                                                                registerId=registerId)
            logging.info("返回结果：{}".format(res_text.json()))
            assert_common(res_text, msg=exc_data)

        if case_name == "药品搜索":
            res_text = ApiFactory.get_clinicalReception().selectMedicineStock(moudle_name=moudle_name, case_name=case_name , request_method=request_method, url=request_url, data=json.loads(req_data))
            logging.info("返回结果：{}".format(res_text.json()))
            assert_common(res_text, msg=exc_data)
            batchNo = res_text.json().get("data")[0].get("batchNo")
            total = res_text.json().get("data")[0].get("total")
            pieceTotal = res_text.json().get("data")[0].get("pieceTotal")
            packUnit = res_text.json().get("data")[0].get("packUnit")
            specs = res_text.json().get("data")[0].get("specs")
            retailPrice = res_text.json().get("data")[0].get("retailPrice")
            manufacturer = res_text.json().get("data")[0].get("manufacturer")
            stock = res_text.json().get("data")[0].get("stock")
            id = res_text.json().get("data")[0].get("id")
            clinicId = res_text.json().get("data")[0].get("clinicId")
            namePinyin = res_text.json().get("data")[0].get("namePinyin")
            manufacturerPinyin = res_text.json().get("data")[0].get("manufacturerPinyin")
            packAmount = res_text.json().get("data")[0].get("packAmount")
            pieceAmount = res_text.json().get("data")[0].get("pieceAmount")
            stockId = res_text.json().get("data")[0].get("stockId")
            newPrice = res_text.json().get("data")[0].get("newPrice")
            medicineId = res_text.json().get("data")[0].get("medicineId")
            expireDate = res_text.json().get("data")[0].get("expireDate")
            supplierId = res_text.json().get("data")[0].get("supplierId")
            medicineName = res_text.json().get("data")[0].get("medicineName")

        if case_name == "下单":
            res_text = ApiFactory.get_clinicalReception().placeAnOrder(moudle_name=moudle_name, case_name=case_name,
                                                                           request_method=request_method,
                                                                           url=request_url, data=json.loads(req_data),
                                                                           registerId=registerId, patientId=patientId,
                                                                           batchNo=batchNo,
                                                                           total=total, pieceTotal=pieceTotal,
                                                                           packUnit=packUnit, specs=specs,
                                                                           retailPrice=retailPrice,
                                                                           manufacturer=manufacturer, stock=stock,
                                                                           id=id, clinicId=clinicId,
                                                                           namePinyin=namePinyin,
                                                                           manufacturerPinyin=manufacturerPinyin,
                                                                           packAmount=packAmount,
                                                                           pieceAmount=pieceAmount, stockId=stockId,
                                                                           newPrice=newPrice, medicineId=medicineId,
                                                                           expireDate=expireDate,
                                                                           supplierId=supplierId,
                                                                           medicineName=medicineName)
            logging.info("返回结果：{}".format(res_text.json()))
            assert_common(res_text, msg=exc_data)
            visitOrderId = res_text.json().get("data").get("visitOrder").get("id")
            orderType = res_text.json().get("data").get("visitOrder").get("orderType")
            logging.info("下单后获取到的visitOrderID为：{}".format(visitOrderId))

        if case_name == "取消收费":
            res_text = ApiFactory.get_clinicalReception().cancelCharge(moudle_name=moudle_name, case_name=case_name, request_method=request_method, url=request_url, data=req_data, visitOrderId=visitOrderId)
            logging.info("返回结果：{}".format(res_text.json()))
            assert_common(res_text, msg=exc_data)

