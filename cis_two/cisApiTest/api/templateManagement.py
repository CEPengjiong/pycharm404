"""
模板管理
"""

from utils.request_common import request_common
import api_config

_t = str(api_config._t)

class templateManagement:


    # 模板管理列表查询
    def templatePage(self, moudle_name, case_name, request_method, url, data):

        return request_common(moudle_name, case_name, request_method, url=url, data=data)

    # 模板管理列表根据名称查询
    def templatePage_name(self, moudle_name, case_name, request_method, url, data, title):
        url = url + title
        return request_common(moudle_name, case_name, request_method, url=url, data=data)

    # 查询模板详情
    def templatedetails(self, moudle_name, case_name, request_method, url, data, templateId):
        url = url + str(templateId) + "?_t=" + _t
        return request_common(moudle_name, case_name, request_method, url=url, data=data)

    # 新增模板
    def templateAdd(self, moudle_name, case_name, request_method, url, data, total, batchNo, pieceTotal, packUnit, specs, retailPrice, manufacturer, stock, id, clinicId, namePinyin,
                    manufacturerPinyin, packAmount, pieceAmount, stockId, newPrice, medicineId, expireDate, supplierId, medicineName):

        data["title"] = "接口测试" + _t
        data["syntheticMedicineVOS"][0]["total"] = total
        data["syntheticMedicineVOS"][0]["batchNo"] = batchNo
        data["syntheticMedicineVOS"][0]["pieceTotal"] = pieceTotal
        data["syntheticMedicineVOS"][0]["packUnit"] = packUnit
        data["syntheticMedicineVOS"][0]["specs"] = specs
        data["syntheticMedicineVOS"][0]["retailPrice"] = retailPrice
        data["syntheticMedicineVOS"][0]["manufacturer"] = manufacturer
        data["syntheticMedicineVOS"][0]["stock"] = stock
        data["syntheticMedicineVOS"][0]["id"] = id
        data["syntheticMedicineVOS"][0]["clinicId"] = clinicId
        data["syntheticMedicineVOS"][0]["namePinyin"] = namePinyin
        data["syntheticMedicineVOS"][0]["manufacturerPinyin"] = manufacturerPinyin
        data["syntheticMedicineVOS"][0]["packAmount"] = packAmount
        data["syntheticMedicineVOS"][0]["pieceAmount"] = pieceAmount
        data["syntheticMedicineVOS"][0]["stockId"] = stockId
        data["syntheticMedicineVOS"][0]["newPrice"] = newPrice
        data["syntheticMedicineVOS"][0]["medicineId"] = medicineId
        data["syntheticMedicineVOS"][0]["expireDate"] = expireDate
        data["syntheticMedicineVOS"][0]["supplierId"] = supplierId
        data["syntheticMedicineVOS"][0]["medicineName"] = medicineName
        data["syntheticMedicineVOS"][0]["salePrice"] = retailPrice
        url = url + _t
        return (request_common(moudle_name, case_name, request_method, url=url, data=data), data["title"])

    # 编辑模板
    def templateEdit(self, moudle_name, case_name, request_method, url, data, packUnit, specs, retailPrice, manufacturer, clinicId, medicineId,medicineName, templateId, titlePy, doctorId, id2, createBy, createTime, title):
        data["templateId"] = templateId
        data["titlePy"] = titlePy
        data["doctorId"] = doctorId
        data["title"] = title
        data["clinicId"] = clinicId
        data["syntheticMedicineVOS"][0]["id"] = id2
        data["syntheticMedicineVOS"][0]["clinicTemplateId"] = templateId
        data["syntheticMedicineVOS"][0]["medicineId"] = medicineId
        data["syntheticMedicineVOS"][0]["medicineName"] = medicineName
        data["syntheticMedicineVOS"][0]["manufacturer"] = manufacturer
        data["syntheticMedicineVOS"][0]["specs"] = specs
        data["syntheticMedicineVOS"][0]["packUnit"] = packUnit
        data["syntheticMedicineVOS"][0]["retailPrice"] = retailPrice
        data["syntheticMedicineVOS"][0]["salePrice"] = retailPrice
        data["createTime"] = createTime
        data["createBy"] = createBy
        return request_common(moudle_name, case_name, request_method, url=url, data=data)


    # 删除模板
    def templateDelete(self, moudle_name, case_name, request_method, url, data, templateId):
        url = url + str(templateId)
        return request_common(moudle_name, case_name, request_method, url=url, data=data)


