# 医生接诊-收费

# coding=utf-8
# TaskSet是任务类、定义待测试的任务代码集如下的WebsiteTasks的类，task是子任务方法
from locust import HttpUser, TaskSet, task, between
import requests
import api_congfig
import time
import xlrd
# 关闭安全请求警告
requests.packages.urllib3.disable_warnings()

# 开启脚本  点击下方Terminal打开控制台，cd 到对应文件目录下，执行locust -f locust.py
# 前台操作页面  打开http://localhost:8089/  输入并发数和增长率。

# 2021-11-16 20:28:09 格式

# 获取token、查询客户接口共用一个相同的head
head = {
            'Content-Type': 'application/json',
        }

# 创建WebsiteTasks()类继承TaskSet类：用于定义测试业务
class WebsiteTasks(TaskSet):

    # 在测试前的初始化，先获取token且只获取一次
    def test_start(self):
        body = '''{
            "phone": "13127851305",
            "password": "2aed8cddab870e350fca5dfc4f4cd526",
            "timestamp": 1637118195906
        }'''
        url = '/prod-api/auth/clinic/login?_t=' + str(api_congfig._t)
        r = self.client.post(url, headers=head, data=body, verify=False)
        assert '"code":200' in r.text, 'token接口获取失败\n结果------------%s' % r.text
        a = r.json()
        # 将获取到的token组装下放入head的token参数中
        head['token'] = 'Bearer ' + a['data']['access_token']
        startTime = time.strftime('%Y-%m-%d %H:%M:%S')
        print("开始测试时间----------", startTime)

    def test_stop(self):
        endTime = time.strftime('%Y-%m-%d %H:%M:%S')
        print("结束测试时间----------", endTime)

    # 用@task()装饰下面方法为一个任务，括号里的值表示该行为的执行的权重，数值越大，执行频率越高
    @task(1)
    def patientregister(self):
        # 报文体
        self.form_data = '''{
            "name": "''' + api_congfig.create_name() + '''",
            "birthday": "2005-11-16",
            "phone": "''' + api_congfig.str_phone + '''",
            "sex": 0,
            "jobId": 1,
            "deptId": 210,
            "doctorId": 3073,
            "visitTime": "''' + api_congfig.visitTime + '''",
            "visitChannel": 0,
            "remarks": null,
            "addFamily": false,
            "patientFamilies": []
            }'''

        url = "/prod-api/clinic/patientregister?_t=" + str(api_congfig._t)
        # 支持post接口中带中文的参数
        form_data1 = self.form_data.encode("utf-8")
        # post方法推送, verify：Ture/False，默认是Ture，用于验证SSL证书开关
        res_text = self.client.post(url, name='/login', headers=head, data=form_data1, verify=False)
        assert '"code":200' in res_text.text, '挂号接口获取失败\n结果------------%s' % res_text.text
        registerId = res_text.json().get("data").get("registerId")
        patientId = res_text.json().get("data").get("patientId")

        # 接诊
        body = {}
        patientregisterUrl = "/prod-api/clinic/patientregister/updatePatientRegister?visitStatus=1&registerId=" + str(registerId)
        res_text = self.client.put(patientregisterUrl, name='/updatePatientRegister?visitStatus=1', headers=head, data=body, verify=False)
        assert '操作成功' in res_text.text, '接诊接口获取失败\n结果------------%s' % res_text.text

        # 创建订单
        creatBody = {
            "registerId": '%s' % registerId
        }
        createUrl = "/prod-api/clinic/tvisitorder/create?_t=" + str(api_congfig._t)
        res_text = self.client.post(createUrl, name='/tvisitorder/create', headers=head, json=creatBody, verify=False)
        assert '操作成功' in res_text.text, '创建订单接口获取失败\n结果------------%s' % res_text.text

        # 下单
        placeAnOrderbody = {
            "medicalRecord": {
                "patientId": patientId,
                "visitType": 0,
                "returnVisitDate": "",
                "returnVisit": 0,
                "returnRemark": ""
            },
            "visitOrder": {
                "patientId": patientId,
                "totalMoney": 0
            },
            "stockPrescribe": 1,
            "patientRegister": {
                "registerId": registerId
            },
            "drugSubstratStockDtos": [],
            "orderItems": [],
            "optStatus": 2
        }

        placeAnOrderUrl = "/prod-api/clinic/tvisitorder/placeAnOrder?_t=" + str(api_congfig._t)
        res_text = self.client.post(placeAnOrderUrl, name='/placeAnOrder', headers=head, json=placeAnOrderbody, verify=False)
        assert '操作成功' in res_text.text, '下单接口获取失败\n结果------------%s' % res_text.text

        # 订单录入
        visitOrderDVOInfoUrl = "/prod-api/clinic/tvisitorder/visitOrderDVOInfo/" + str(registerId) + "?_t=" + str(api_congfig._t)
        res_text = self.client.get(visitOrderDVOInfoUrl, name='/visitOrderDVOInfo', headers=head, verify=False)
        assert '操作成功' in res_text.text, '订单录入接口获取失败\n结果------------%s' % res_text.text



# 创建WebsiteUser()类，继承httpUser类，用于定义模拟用户
class WebsiteUser(HttpUser):
    # 测试集
    tasks = [WebsiteTasks]
    # 推送地址
    host = "https://t1cis.tyzsls.com"
    # 等待时间 between(min_wait,max_wait),单位秒
    wait_time = between(20, 20)
