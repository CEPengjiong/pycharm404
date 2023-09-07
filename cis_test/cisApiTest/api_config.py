"""
description: 静态变量配置文件；诊所端host地址,每个接口公用的部分,且测试环境变化只需改这里就可以
time: 2022/08/12
author: chenling
"""
import logging.handlers
import os
import pymysql
import time
import datetime as DT


'''
env == "first_test"  第一套测试环境
env == "second_test" 第二套测试环境
env == "uat" uat环境
env == "prod" 生产环境
'''

env = "uat"

def get_env():
    if env == "first_test":
        host_url = "https://t1cis.tyzsls.com/"
        return host_url
    elif env == "second_test":
        host_url = "https://t2cis.tyzsls.com/"
        return host_url
    elif env == "uat":
        host_url = "https://g1cis.tyzsls.com"
        return host_url
    elif env == "prod":
        host_url = "https://cis.tyzsls.com"
        return host_url

# 请求头
request_header = {"Content-type": "application/json;charset=UTF-8"}
excelImportHeader = {}

# 获取时间戳格式：1644384179
endTime = DT.date.today()
beginTime = endTime - DT.timedelta(days=10)
t = time.time()
_t = int(t)

# 格式化成2021-09-13 11:45:39形式
visitTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())


# 获取当前日期和往前推7天的日期
today = DT.date.today()
week_ago = today - DT.timedelta(days=7)
week_later = today + DT.timedelta(days=7)
print(week_ago)
print(today)

# 获取当前项目的目录
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# print("当前项目得目录", BASE_DIR)

# 自定义time值
device_time = time.strftime("%Y-%m-%dT%H:%M:%S:+08:00", time.localtime())

# 初始化项目日志
log_path = BASE_DIR + "\log\clinic-{}.log".format(time.strftime('%Y%m%d %H%M%S'))


def init_log():
    """日志初始化配置"""
    # 创建日志器对象
    logger = logging.getLogger()
    # 设置日志级别
    logger.setLevel(logging.INFO)
    # 处理器对象  -控制台显示
    sh = logging.StreamHandler()
    # 处理器对象  -文件存储
    fh = logging.handlers.TimedRotatingFileHandler(log_path, backupCount=7, encoding="UTF-8")
    # 创建格式化器对象
    fmt = '%(asctime)s %(levelname)s [%(name)s] [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s'
    # 将格式化器添加导处理器
    sh.setFormatter(logging.Formatter(fmt))
    fh.setFormatter(logging.Formatter(fmt))
    # 将处理器添加到日志器当中
    logger.addHandler(sh)
    logger.addHandler(fh)

# 获取环境的配置
def getConf(env, conf):
    if env == 'first_test':
        if conf == 'db':
            db = {
                'host': '8.129.60.19',
                'port': 22022,
                'user': 'devops',
                'passwd': 'eBuv_^P^UFwuvf(p~U$Oj8',
                'db': 'ty_cis_test',
                'charset': 'utf8'
            }
            return db
        elif conf == 'second_test':
            db = {
                'host': '8.129.60.19',
                'port': 3306,
                'user': 'cis1',
                'passwd': 'Tongy@123#',
                'db': 'ty_cis_test1',
                'charset': 'utf8'
            }
            return db


# 查询数据库
def sqlSelect(env, sql):
    # 获取配置 暂时只有测试环境
    conf = getConf(env, 'db')
    # print('conf', conf)
    # 打开数据库连接
    db = pymysql.connect(
        host=conf['host'],
        port=conf['port'],
        user=conf['user'],
        passwd=conf['passwd'],
        db=conf['db'],
        charset=conf['charset']
    )
    # print('db', db)
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()
    # print('db', db)
    try:
        # 执行SQL语句
        # print('sql',sql)
        cursor.execute(sql)
        # 获取所有记录列表
        results = cursor.fetchall()
        # print("获取数据成功！！")
    except ZeroDivisionError as e:
        logging.info("获取数据失败！！！ 报错信息：{}".format(e))
    # 关闭数据库连接
    cursor.close()
    db.close()
    # print('results',results)
    # assert not len(results) == 0, '查询结果为空！！sql:%s' % sql
    if len(results) == 0:
        logging.info("查询结果为空！！！sql:{}".format(sql))
    return results

def checkMysql(env, sql, checkPoint):
    # 查询校验数据库
    try:
        # sql是要查询的表和字段
        checkMysql = sqlSelect(env, sql)
        # print('len(checkMysql)', len(checkMysql))
        assert not len(checkMysql) == 0, '查询结果为空！！'
        logging.info("sql:{},\nsql查询结果:{}".format(sql, checkMysql))
        for row in checkMysql:
            # print('row', row)
            i = 0
            for a in row:
                assert a == checkPoint[i], '数据库不正确！！%s != %s' % (a, checkPoint[i])
                i += 1
        logging.info("checkMysql验证通过")
    except ZeroDivisionError as e:
        logging.info("获取数据失败！！！报错信息:{}".format(e))

