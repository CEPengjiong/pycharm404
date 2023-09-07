# 采购入库-新增入库

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
import logging
all_locusts_spawned = Semaphore()
all_locusts_spawned.acquire()


# 关闭安全请求警告
requests.packages.urllib3.disable_warnings()

# 开启脚本  点击下方Terminal打开控制台，cd 到对应文件目录下，执行locust -f locust.py
# 前台操作页面  打开http://localhost:8089/  输入并发数和增长率。


# 获取当前项目地址并打开excel表
path = api_congfig.baseDir
dataPath = path + r"\getToken\token.xls"
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


    def test_start(self):
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

        # 获取采购药品信息
        body = {
            "name": "牛黄解毒丸",
            "isLaid": 1
        }
        url = '/prod-api/clinic/medicine/info/medicineStockByPurchase?_t=' + str(api_congfig._t)
        # body1 = body.encode("utf-8")
        res_text = self.client.post(url, name='/medicineStockByPurchase', headers=head, json=body, verify=False)
        assert '操作成功' in res_text.text, '获取采购药品信息\n结果------------%s' % res_text.text
        supplierId = res_text.json().get("data")[0].get("supplierId")
        medicineId = res_text.json().get("data")[0].get("medicineId")
        logging.info("\n接口："+url+"\n返回结果:{}".format(res_text.json()))

        # 采购入库-新增入库
        body = '''{
                "supplierId": %s,
                "purchaseTime": "",
                "detailList": [
                 {
                        "newMedicine": false,
                        "amount": 100,
                        "unit": "盒",
                        "retailQuantity": "100",
                        "retailUnit": "盒",
                        "predictAmount": "",
                        "unitPrice": 0.01,
                        "batchNo": "20211119",
                        "expireTime": "2025-11-19",
                        "costPrice": 0.2,
                        "purchaseDetailVo": {
                            "barCode": "",
                            "medicineName": "牛黄解毒丸",
                            "specs": "12粒X3片",
                            "manufacturer": "丹东医创药业有限责任公司",
                            "type": 0,
                            "approvalNumber": null,
                            "retailPrice": 0.2,
                            "purchaseUnit": "盒",
                            "isType": true
                        },
                        "_XID": "row_51",
                        "isHandwork": true,
                        "unitUnanimous": true,
                        "medicineId": %s
                    }
                ],
                "medicinePurchase": {
                    "totalMoney": 1,
                    "purchaseType": 1,
                    "state": 0
                },
                "batSaleNo": "",
                "vencuscode": ""
            }''' % (supplierId, medicineId)

        # 支持post接口中带中文的参数
        # form_data1 = self.body.encode("utf-8")
        url = '/prod-api/clinic/medicine/purchase/savePurchase?_t=' + str(api_congfig._t)
        res_text = self.client.post(url, name='/savePurchase', headers=head, json=body, verify=False)
        assert '操作成功' in res_text.text, '保存采购信息接口获取失败\n结果------------%s' % res_text.text
        logging.info("\n接口："+url+"\n返回结果:{}".format(res_text.json()))
        self.user.queue_data.put_nowait(token)  # 把取出来的数据重新加入队列


# 创建WebsiteUser()类，继承httpUser类，用于定义模拟用户
class WebsiteUser(HttpUser):
    # 测试集
    tasks = [WebsiteTasks]
    # 推送地址
    host = "https://t3cis.tyzsls.com"

    queue_data = queue.Queue()  # 创建队列，先进先出
    for i in range(0, nrows):  # 取值顺序从0开始
        token = table.row_values(i)[0]
        queue_data.put_nowait(token)  # 循环加入队列<全部>,循环完，继续执行
        wait_time = between(20, 20)

if __name__ == '__main__':
    os.system(r"locust -f D:\cis_test\locustTest\purchase\savePurchase.py")