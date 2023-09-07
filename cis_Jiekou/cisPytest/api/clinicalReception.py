# 封装医生接诊接口
import time
from utils.request_common import request_common
import datetime as DT
import api_config

# 转换成13位时间戳
endTime = DT.date.today()
beginTime = endTime - DT.timedelta(days=10)
t = time.time()
_t = int(t)

# 格式化成2021-09-13 11:45:39形式
visitTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

class clinicalReception:

    # 获取用户信息
    def getInfo(self, moudle_name, case_name, request_method, url, data):
        url = url + str(_t)
        return request_common(moudle_name, case_name, request_method, url=url, data=data)

    # 挂号
    def registration(self, moudle_name, case_name, request_method, url, data,  deptId, jobId, doctorId):

        data["deptId"] = deptId
        data["jobId"] = jobId
        data["doctorId"] = doctorId
        data["visitTime"] = visitTime

        url = url + str(_t)

        return request_common(moudle_name, case_name, request_method, url=url, data=data)

    # 查询接诊列表
    def getRegisterList(self, moudle_name, case_name, request_method, url, data):
        if case_name == "查询接诊中列表":
            url = url + "_t=" + str(_t) + "&pageNum=1&pageSize=5&beginTime=" + str(beginTime) + "&endTime=" + str(endTime) + "&visitStatus=1"
        elif case_name == "查询已接诊列表":
            url = url + "_t=" + str(_t) + "&pageNum=1&pageSize=5&beginTime=" + str(beginTime) + "&endTime=" + str(endTime) + "&visitStatus=2"
        else:
            url = url + "_t=" + str(_t) + "&pageNum=1&pageSize=5&visitStatus=0"
        return request_common(moudle_name, case_name, request_method, url=url, data=data)


    # 接诊
    def updatePatientRegister(self, moudle_name, case_name, request_method, url, data, registerId):

        url = url + str(registerId)
        return request_common(moudle_name, case_name, request_method, url=url, data=data)

    # 创建订单
    def createVisitorder(self, moudle_name, case_name, request_method, url, data, registerId):

        data["registerId"] = registerId
        url = url + str(_t)
        return request_common(moudle_name, case_name, request_method, url=url, data=data)

    # 订单信息录入
    def visitOrderDVOInfo(self, moudle_name, case_name, request_method, url, data, registerId):
        url = url + str(registerId) + "?_t=" + str(_t)
        return request_common(moudle_name, case_name, request_method, url=url, data=data)

    # 取消接诊
    def deletePatientRegister(self, moudle_name, case_name, request_method, url, data, registerId2):
        url = url + str(registerId2) + "&cause="
        return request_common(moudle_name, case_name, request_method, url=url, data=data)

    # 药品搜索
    def selectMedicineStock(self, moudle_name, case_name, request_method, url, data):
        url = url + str(_t)
        return request_common(moudle_name, case_name, request_method, url=url, data=data)

    # 下单
    def placeAnOrder(self, moudle_name, case_name, request_method, url, data, registerId, patientId,batchNo,total, pieceTotal, packUnit, specs, retailPrice,
                     manufacturer, stock, id, clinicId, namePinyin, manufacturerPinyin, packAmount, pieceAmount, stockId, newPrice, medicineId, expireDate, supplierId, medicineName):

        data["patientRegister"]["registerId"] = registerId
        data["medicalRecord"]["patientId"] = patientId
        data["visitOrder"]["patientId"] = patientId
        data["visitOrder"]["totalMoney"] = retailPrice
        data["drugSubstratStockDtos"][0]["medicineId"] = medicineId
        data["drugSubstratStockDtos"][0]["medicineName"] = medicineName
        data["drugSubstratStockDtos"][0]["unit"] = packUnit
        data["drugSubstratStockDtos"][0]["detItemFeeSumamt"] = retailPrice
        data["drugSubstratStockDtos"][0]["batchNo"] = batchNo
        data["drugSubstratStockDtos"][0]["manufacturer"] = manufacturer
        data["drugSubstratStockDtos"][0]["cntUnit"] = packUnit
        data["drugSubstratStockDtos"][0]["salePrice"] = retailPrice
        data["drugSubstratStockDtos"][0]["pric"] = retailPrice
        data["drugSubstratStockDtos"][0]["spec"] = specs
        data["drugSubstratStockDtos"][0]["medListname"] = medicineName

        data["orderItems"][0]["subTotal"] = retailPrice
        data["orderItems"][0]["jsonstr"] = "{\"type\":\"中西成药\",\"data\":[{\"total\":%s,\"pieceTotal\":%s,\"batchNo\":\"%s\",\"barCode\":\"\",\"pieceUnit\":\"\",\"packUnit\":\"%s\",\"pieceUnitName\":null,\"packUnitName\":null,\"pieceNumber\":null,\"medicineName\":\"%s\",\"tradeName\":null,\"tradeNamePinyin\":\"\",\"specs\":\"%s\",\"type\":0,\"approvalNumber\":null,\"retailPrice\":%s,\"piecePrice\":null,\"manufacturer\":\"%s\",\"stock\":\"%s\",\"id\":%s,\"clinicId\":%s,\"namePinyin\":\"%s\",\"manufacturerPinyin\":\"%s\",\"packUnitId\":null,\"pieceUnitId\":null,\"zeroFlag\":false,\"zeroFlagSell\":false,\"packAmount\":%s,\"pieceAmount\":%s,\"stockId\":\"%s\",\"newPrice\":%s,\"medicineId\":%s,\"updateAmount\":0,\"updateFlag\":0,\"unit\":null,\"unitId\":null,\"expireDate\":\"%s\",\"supplierId\":%s,\"drugUsage\":null,\"singleDosage\":1,\"singleDosageUnit\":\"\",\"singleDose\":1,\"singleDoseUnit\":\"\",\"frequency\":\"\",\"isType\":true,\"projectLevel\":null,\"medicareFlag\":0,\"isWithHemp\":true,\"otcMedicineFlag\":true,\"countryCode\":null,\"frequencyRemark\":null,\"medicineTotalPurchasePrice\":null,\"drugMedicineIndex\":null,\"stockPrescribe\":1,\"formulation\":\"\",\"formulationCode\":null,\"tcmdrugUsedWay\":2,\"salePrice\":%s,\"amount\":1,\"days\":1,\"_XID\":\"row_%s\",\"_X_ID\":\"row_174\"}],\"remark\":\"\",\"chargeData\":[],\"subtotal\":%s,\"drugMoney\":%s,\"extraMoney\":0,\"totalMoney\":%s}" \
                                        % (total, pieceTotal, batchNo, packUnit, medicineName, specs, retailPrice, manufacturer, stock, id, clinicId,
                                           namePinyin, manufacturerPinyin, packAmount, pieceAmount, stockId, int(newPrice), medicineId, expireDate, supplierId, retailPrice, id, retailPrice, retailPrice, retailPrice)
        url = url + str(_t)
        return request_common(moudle_name, case_name, request_method, url=url, data=data)

    # 校验是否处方药
    def checkedPrescriptionsDrug(self, moudle_name, case_name, request_method, url, data, visitOrderId, orderType):

        data["visitOrderId"] = visitOrderId
        data["orderType"] = orderType
        url = url + str(_t)
        return request_common(moudle_name, case_name, request_method, url=url, data=data)

    # 收费
    def charge(self, moudle_name, case_name, request_method, url, data, visitOrderId, retailPrice):

        data["visitOrder"]["id"] = visitOrderId
        data["chargeRecord"]["cash"] = retailPrice
        data["chargeRecord"]["receivableMoney"] = retailPrice
        data["chargeRecord"]["receivedMoney"] = retailPrice

        if case_name == "欠费":
            data["visitOrder"]["id"] = visitOrderId
            data["chargeRecord"]["cash"] = retailPrice
            data["chargeRecord"]["receivableMoney"] = retailPrice
            data["chargeRecord"]["arrearsMoney"] = retailPrice

        url = url + str(_t)
        return request_common(moudle_name, case_name, request_method, url=url, data=data)

    # 已收费-查询
    def chargeManagementInfo(self, moudle_name, case_name, request_method, url, data, visitOrderId):

        url = url + str(visitOrderId) + "?_t=" + str(_t)
        return request_common(moudle_name, case_name, request_method, url=url, data=data)

    # 代收费-校验有无结算单
    def check(self, moudle_name, case_name, request_method, url, data, visitOrderId):
        url = url + str(_t)
        data["cisOrderId"] = visitOrderId
        return request_common(moudle_name, case_name, request_method, url=url, data=data)

    # 收费管理-已收费-退费
    def orderRefund(self, moudle_name, case_name, request_method, url, data, visitOrderId, retailPrice):
        url = url + str(_t)
        data["visitOrder"]["id"] = visitOrderId
        data["refundFee"]["cash"] = retailPrice
        return request_common(moudle_name, case_name, request_method, url=url, data=data)

    # 打印处方笺
    def printPrescription(self,moudle_name, case_name, request_method, url, data, orderNo):
        url = url + str(_t) + "&orderNo=" + orderNo + "&type=0"
        return request_common(moudle_name, case_name, request_method, url=url, data=data)

    # 查询病历id
    def orderCancelVerify(self, moudle_name, case_name, request_method, url, data, visitOrderId):
        url =url + str(visitOrderId) + "?_t="+str(_t)
        return request_common(moudle_name, case_name, request_method, url=url, data=data)

    # 退回处方
    def returnPrescription(self, moudle_name, case_name, request_method, url, data, medicalRecordId):
        url =url + str(medicalRecordId)
        return request_common(moudle_name, case_name, request_method, url=url, data=data)

    # 获取预约id
    def getRegisterList2(self, moudle_name, case_name, request_method, url, data):

        url = url +str(_t) + "&visitStatus=1&patNameOrPhone=接口测试"
        return request_common(moudle_name, case_name, request_method, url=url, data=data)

    def cancelCharge(self, moudle_name, case_name, request_method, url, data, visitOrderId):
        url = url + str(visitOrderId)
        return request_common(moudle_name, case_name, request_method, url=url, data=data)