# 医生接诊-收费

# coding=utf-8
# TaskSet是任务类、定义待测试的任务代码集如下的WebsiteTasks的类，task是子任务方法
from locust import HttpUser, TaskSet, task, between
from locust import events
from gevent._semaphore import Semaphore
import requests
import api_congfig
import time
import xlrd
import queue
import os
all_locusts_spawned = Semaphore()
all_locusts_spawned.acquire()

# 关闭安全请求警告
requests.packages.urllib3.disable_warnings()

# 开启脚本  点击下方Terminal打开控制台，cd 到对应文件目录下，执行locust -f locust.py
# 前台操作页面  打开http://localhost:8089/  输入并发数和增长率。

# 获取当前项目的目录
baseDir = os.path.dirname(os.path.abspath(__file__))
dataPath = baseDir + r"\getToken\token.xls"
excel = xlrd.open_workbook(dataPath)
table = excel.sheets()[0]
# 获取行数
nrows = table.nrows


# 通过locust基于gevent并发的机制，引入gevent的锁的概念，代入到locust的钩子函数中，实现集合点统一并发概念

@events.spawning_complete.add_listener  # 挂载到locust钩子函数（spawning_complete 产生所有模拟用户时触发）
def on_hatch_complete(**kwargs):
    all_locusts_spawned.release()  # 创建钩子方法



# 创建WebsiteTasks()类继承TaskSet类：用于定义测试业务
class WebsiteTasks(TaskSet):

    # 在测试前的初始化，先获取token且只获取一次
    def test_start(self):
        # body = '''{
        #     "phone": "13127851305",
        #     "password": "2aed8cddab870e350fca5dfc4f4cd526",
        #     "timestamp": 1637118195906
        # }'''
        # url = '/prod-api/auth/clinic/login?_t=' + str(congfig._t)
        # r = self.client.post(url, headers=head, data=body, verify=False)
        # assert '"code":200' in r.text, 'token接口获取失败\n结果------------%s' % r.text
        # a = r.json()
        # # 将获取到的token组装下放入head的token参数中
        # head['token'] = 'Bearer ' + a['data']['access_token']
        startTime = time.strftime('%Y-%m-%d %H:%M:%S')
        print("开始测试时间----------", startTime)

    def test_stop(self):
        endTime = time.strftime('%Y-%m-%d %H:%M:%S')
        print("结束测试时间----------", endTime)

    # 用@task()装饰下面方法为一个任务，括号里的值表示该行为的执行的权重，数值越大，执行频率越高
    @task(1)
    def charge(self):
        try:
            token = self.user.queue_data.get()  # 获取队列里的数据
        except queue.Empty:  # 队列取空后，直接退出
            exit(0)

        # 报文头
        head = {
            'Content-Type': 'application/json',
            'token': '%s' % token
        }

        all_locusts_spawned.wait()  # 限制在所有用户准备完成前处于等待状态

        # 1 获取用户信息
        clinicdepturl = '/prod-api/clinic/user/getInfo?_t=' + str(api_congfig._t)
        res_text = self.client.get(clinicdepturl, name='/user/getInfo', headers=head, verify=False)
        assert '操作成功' in res_text.text, '用户信息接口获取失败\n结果------------%s' % res_text.text
        deptId = res_text.json().get("user").get("deptId")
        jobId = res_text.json().get("user").get("jobId")
        doctorId = res_text.json().get("user").get("userId")

        # 2 预约挂号
        self.form_data = '''{
            "name": "%s",
            "birthday": "2005-11-16",
            "phone": "%s",
            "sex": 0,
            "jobId": %s,
            "deptId": %s,
            "doctorId": %s,
            "visitTime": "%s",
            "visitChannel": 0,
            "remarks": null,
            "addFamily": false,
            "patientFamilies": []
            }''' % (api_congfig.create_name(), api_congfig.str_phone, jobId, deptId, doctorId, api_congfig.visitTime)

        url = "/prod-api/clinic/patientregister?_t=" + str(api_congfig._t)
        # 支持post接口中带中文的参数
        form_data1 = self.form_data.encode("utf-8")
        # post方法推送, verify：Ture/False，默认是Ture，用于验证SSL证书开关
        res_text = self.client.post(url, name='/patientregister', headers=head, data=form_data1, verify=False)
        assert '"code":200' in res_text.text, '挂号接口获取失败\n结果------------%s' % res_text.text
        registerId = res_text.json().get("data").get("registerId")
        patientId = res_text.json().get("data").get("patientId")

        # 3 接诊
        body = {}
        patientregisterUrl = "/prod-api/clinic/patientregister/updatePatientRegister?visitStatus=1&registerId=" + str(registerId)
        res_text = self.client.put(patientregisterUrl, name='/updatePatientRegister?visitStatus=1', headers=head, data=body, verify=False)
        assert '操作成功' in res_text.text, '接诊接口获取失败\n结果------------%s' % res_text.text

        # 4 创建订单
        creatBody = {
            "registerId": '%s' % registerId
        }
        createUrl = "/prod-api/clinic/tvisitorder/create?_t=" + str(api_congfig._t)
        res_text = self.client.post(createUrl, name='/tvisitorder/create', headers=head, json=creatBody, verify=False)
        assert '操作成功' in res_text.text, '创建订单接口获取失败\n结果------------%s' % res_text.text

        # # 下单
        # placeAnOrderbody = {
        #     "medicalRecord": {
        #         "patientId": patientId,
        #         "visitType": 0,
        #         "returnVisitDate": "",
        #         "returnVisit": 0,
        #         "returnRemark": ""
        #     },
        #     "visitOrder": {
        #         "patientId": patientId,
        #         "totalMoney": 0
        #     },
        #     "stockPrescribe": 1,
        #     "patientRegister": {
        #         "registerId": registerId
        #     },
        #     "drugSubstratStockDtos": [],
        #     "orderItems": [],
        #     "optStatus": 2
        # }
        #
        # placeAnOrderUrl = "/prod-api/clinic/tvisitorder/placeAnOrder?_t=" + str(congfig._t)
        # res_text = self.client.post(placeAnOrderUrl, name='/placeAnOrder', headers=head, json=placeAnOrderbody, verify=False)
        # assert '操作成功' in res_text.text, '下单接口获取失败\n结果------------%s' % res_text.text

        # 5 订单录入
        visitOrderDVOInfoUrl = "/prod-api/clinic/tvisitorder/visitOrderDVOInfo/" + str(registerId) + "?_t=" + str(api_congfig._t)
        res_text = self.client.get(visitOrderDVOInfoUrl, name='/visitOrderDVOInfo', headers=head, verify=False)
        assert '操作成功' in res_text.text, '订单录入接口获取失败\n结果------------%s' % res_text.text


        # 6 查询药品信息
        selectMedicine = {
            "name": "牛黄解毒丸",
            "type": 0,
            "isLaid": 0
        }
        selectMedicineUrl = "/prod-api/clinic/medicine/info/selectMedicineStock?_t=" + str(api_congfig._t)
        res_text = self.client.post(selectMedicineUrl, name='/selectMedicineStock', headers=head, json=selectMedicine, verify=False)
        assert '操作成功' in res_text.text, '查询药品信息接口获取失败\n结果------------%s' % res_text.text
        clinicId = res_text.json().get("data")[0].get("clinicId")
        medicineId = res_text.json().get("data")[0].get("medicineId")
        total = res_text.json().get("data")[0].get("total")
        id = res_text.json().get("data")[0].get("id")
        stockId = res_text.json().get("data")[0].get("stockId")
        supplierId = res_text.json().get("data")[0].get("supplierId")
        packAmount = res_text.json().get("data")[0].get("packAmount")
        batchNo = res_text.json().get("data")[0].get("batchNo")
        stock = res_text.json().get("data")[0].get("stock")

        # 7 下单
        placeAnOrder = r'''{
            "medicalRecord": {
                "diagnosticResult": "感冒",
                "diagnosticResultCode": "",
                "patientId": %s,
                "visitType": 0,
                "returnVisitDate": "",
                "returnVisit": 0,
                "returnRemark": ""
            },
            "visitOrder": {
                "patientId": %s,
                "totalMoney": 0.2
            },
            "stockPrescribe": 1,
            "patientRegister": {
                "registerId": %s
            },
            "drugSubstratStockDtos": [
                {
                    "medicineId": %s,
                    "medicineName": "牛黄解毒丸",
                    "zeroFlag": 0,
                    "amount": 1,
                    "unit": "盒",
                    "isMedicine": 1,
                    "isType": true,
                    "type": 0,
                    "medListCodg": null,
                    "detItemFeeSumamt": 0.2,
                    "cnt": 1,
                    "singleDose": 1,
                    "singleDoseUnit": "",
                    "frequency": "",
                    "medicineType": 0,
                    "manufacturer": "丹东医创药业有限责任公司",
                    "level": null,
                    "cntUnit": "盒",
                    "pric": 0.2,
                    "spec": "12粒X3片",
                    "dosage": null,
                    "medListname": "牛黄解毒丸",
                    "medicalgetway": null,
                    "recipeName": "中西成药处方"
                }
            ],
            "orderItems": [
                {
                    "prescriptionType": 0,
                    "subTotal": 0.2,
                    "jsonstr": "{\"type\":\"中西成药\",\"data\":[{\"total\":%s,\"pieceTotal\":0,\"batchNo\":\"%s\",\"barCode\":\"\",\"pieceUnit\":\"\",\"packUnit\":\"盒\",\"pieceUnitName\":null,\"packUnitName\":null,\"pieceNumber\":null,\"medicineName\":\"牛黄解毒丸\",\"tradeName\":null,\"tradeNamePinyin\":\"\",\"specs\":\"12粒X3片\",\"type\":0,\"approvalNumber\":null,\"retailPrice\":0.2,\"piecePrice\":null,\"manufacturer\":\"丹东医创药业有限责任公司\",\"stock\":\"%s\",\"id\":%s,\"clinicId\":%s,\"namePinyin\":\"nhjdw\",\"manufacturerPinyin\":\"ddycyyyxzrgs\",\"packUnitId\":null,\"pieceUnitId\":null,\"zeroFlag\":false,\"zeroFlagSell\":false,\"packAmount\":%s,\"pieceAmount\":0,\"stockId\":\"%s\",\"newPrice\":0.1,\"medicineId\":%s,\"updateAmount\":0,\"updateFlag\":0,\"unit\":null,\"unitId\":null,\"expireDate\":\"2023-11-19 00:00:00\",\"supplierId\":%s,\"drugUsage\":null,\"singleDosage\":1,\"singleDosageUnit\":\"\",\"singleDose\":1,\"singleDoseUnit\":\"\",\"frequency\":\"\",\"isType\":true,\"projectLevel\":null,\"medicareFlag\":0,\"isWithHemp\":false,\"otcMedicineFlag\":false,\"countryCode\":null,\"frequencyRemark\":null,\"medicineTotalPurchasePrice\":null,\"drugMedicineIndex\":null,\"stockPrescribe\":0,\"formulation\":\"\",\"formulationCode\":null,\"salePrice\":0.2,\"amount\":1,\"days\":1,\"_XID\":\"row_%s\"}],\"remark\":\"\",\"chargeData\":[],\"subtotal\":0.2,\"drugMoney\":0.2,\"extraMoney\":0,\"totalMoney\":0.2}"
                }
            ],
            "optStatus": 1
        }''' % (patientId, patientId, registerId, medicineId, total, batchNo, stock, id, clinicId, packAmount, stockId, medicineId, supplierId, id)

        # 支持post接口中带中文的参数
        placeAnOrderData = placeAnOrder.encode("utf-8")
        placeAnOrderurl = "/prod-api/clinic/tvisitorder/placeAnOrder?_t=" + str(api_congfig._t)
        res_text = self.client.post(placeAnOrderurl, name='/placeAnOrder', headers=head, data=placeAnOrderData, verify=False)
        assert '操作成功' in res_text.text, '下单接口获取失败\n结果------------%s' % res_text.text
        tvisitorderId = res_text.json().get("data").get("visitOrder").get("id")

        # 8 收费
        chargebody = '''{
            "visitOrder": {
                "id": %s,
                "orderStatus": 0,
                "delZeroFlag": 0,
                "remark": null
            },
            "chargeRecord": {
                "receivableMoney": 0.2,
                "changeMoney": 0,
                "arrearsMoney": 0,
                "receivedMoney": 0.2,
                "discountMoney": 0,
                "cash": 0.2
            },
            "stockPrescribe": 1
        }''' % tvisitorderId

        chargeurl = "/prod-api/clinic/tvisitorder/charge?_t=" + str(api_congfig._t)
        res_text = self.client.post(chargeurl, name='/charge', headers=head, data=chargebody, verify=False)
        assert '操作成功' in res_text.text, '收费接口获取失败\n结果------------%s' % res_text.text

        self.user.queue_data.put_nowait(token)  # 把取出来的数据重新加入队列


# 创建WebsiteUser()类，继承httpUser类，用于定义模拟用户
class WebsiteUser(HttpUser):
    # 测试集
    tasks = [WebsiteTasks]
    # 推送地址
    host = "https://yccis.tyzsls.com"

    queue_data = queue.Queue()  # 创建队列，先进先出
    for i in range(0, nrows):  # 取值顺序从0开始
        token = table.row_values(i)[0]
        queue_data.put_nowait(token)  # 循环加入队列<全部>,循环完，继续执行
        wait_time = between(20, 20)

