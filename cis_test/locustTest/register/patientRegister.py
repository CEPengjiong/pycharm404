# 医生接诊-预约挂号

# coding=utf-8
# TaskSet是任务类、定义待测试的任务代码集如下的WebsiteTasks的类，task是子任务方法
from locust import HttpUser, TaskSet, task, between
from locust import events
from gevent._semaphore import Semaphore
import requests
import os
import sys
import logging
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
import api_congfig
import xlrd
import queue
from datetime import datetime
all_locusts_spawned = Semaphore()
all_locusts_spawned.acquire()
'''
开启脚本  点击下方Terminal打开控制台，cd 到对应文件目录下，执行locust -f locust.py
前台操作页面  打开http://localhost:8089/  输入并发数和增长率。
'''

# 关闭安全请求警告
requests.packages.urllib3.disable_warnings()

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

    # # 在测试前的初始化，先获取token且只获取一次
    # def on_start(self):
    #     body = '''{
    #         "phone": "13127851305",
    #         "password": "2aed8cddab870e350fca5dfc4f4cd526",
    #         "timestamp": 1637118195906
    #     }'''
    #     url = '/prod-api/auth/clinic/login?_t=' + str(api_congfig._t)
    #     r = self.client.post(url, headers=head, data=body, verify=False)
    #     assert '"code":200' in r.text, 'token接口获取失败\n结果------------%s' % r.text
    #     a = r.json()
    #     # 将获取到的token组装下放入head的token参数中
    #     head['token'] = 'Bearer ' + a['data']['access_token']
    #     print('获取到的token = ', head['token'])

    @events.test_start.add_listener
    def on_test_start(environment, **kwargs):
        global start
        start = datetime.now()
        print("开始测试时间------", start)

    @events.test_stop.add_listener
    def on_test_stop(environment, **kwargs):
        end = datetime.now()
        print("结束测试时间------%s\n执行时间差------%s" % (end, end - start))


    # 用@task()装饰下面方法为一个任务，括号里的值表示该行为的执行的权重，数值越大，执行频率越高
    @task(1)
    # 表示一个行为
    def patientregister(self):
        try:
            token = self.user.queue_data.get()  # 获取队列里的数据

        except queue.Empty:  # 队列取空后，直接退出
            exit(0)

        # 报文头
        self.head = {
            'Content-Type': 'application/json',
            'token': '%s' % token
        }

        all_locusts_spawned.wait()  # 限制在所有用户准备完成前处于等待状态

        # 1 获取用户信息
        clinicdepturl = '/prod-api/clinic/user/getInfo?_t=' + str(api_congfig._t)
        res_text = self.client.get(clinicdepturl, name='/user/getInfo', headers=self.head, verify=False)
        assert '操作成功' in res_text.text, '/user/getInfo接口获取失败\n结果------------%s' % res_text.text
        deptId = res_text.json().get("user").get("deptId")
        jobId = res_text.json().get("user").get("jobId")
        doctorId = res_text.json().get("user").get("userId")
        # logging.info("\n接口：" + clinicdepturl + "\n返回结果:{}".format(res_text.json()))

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
                  }''' % (
        api_congfig.create_name(), api_congfig.str_phone, jobId, deptId, doctorId, api_congfig.visitTime)

        url = "/prod-api/clinic/patientregister?_t=" + str(api_congfig._t)
        # 支持post接口中带中文的参数
        form_data1 = self.form_data.encode("utf-8")
        # post方法推送, verify：Ture/False，默认是Ture，用于验证SSL证书开关

        res_text = self.client.post(url, headers=self.head, name='/patientregister', data=form_data1, verify=False)
        assert '操作成功' in res_text.text, '/patientregister接口获取失败\n结果------------%s' % res_text.text
        logging.info("\n接口："+url+"\n返回结果:{}".format(res_text.json()))

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

    # 等待时间 between(min_wait,max_wait),单位秒
    wait_time = between(0, 1)


if __name__ == '__main__':
    os.system(r"locust -f D:\cis_test\locustTest\register\patientRegister.py")