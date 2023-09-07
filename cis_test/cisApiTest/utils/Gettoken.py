import xlrd
import xlwt
import os
import requests
import time
# 关闭安全请求警告
requests.packages.urllib3.disable_warnings()

'''
2021/11/18 作者：pj
从account表中读取到账号信息，通过login接口发送post请求，得到token值后，存入一个新表token.xls
'''
class getToken(object):

    def login(self, url):
        # 10位时间戳
        t = time.time()
        _t = int(t)

        # 获取当前项目的目录
        baseDir = os.path.dirname(os.path.abspath(__file__))
        dataPath = baseDir + r"\account.xls"
        excel = xlrd.open_workbook(dataPath)

        # 通过索引顺序获取
        table = excel.sheets()[0]
        print(table)
        print(type(table))

        # 获取行数
        nrows = table.nrows
        print('总行数:', nrows)
        print("该文档有%i行" % nrows)

        # 获取列数
        ncols = table.ncols
        print('该文档有%i列' % ncols)

        # 获取整行或整列的值
        '''row_values = table.row_values(i) , col_values = table.col_values(j) , 其中i为行号， j为列号# 行号、列号索引从0开始'''
        # row_values = table.row_values(0)
        # col_values = table.col_values(2)

        # 获取指定单元格数据
        # value = table.cell(i, j).value , i-行号， j-列号
        # 例如获取第2行、第1列的数据
        # value = table.cell(1, 0).value
        # print('获取第二行第一列数据', int(value))

        head = {
            'Content-Type': 'application/json',
        }

        # 创建一个workbook 设置编码
        workbook = xlwt.Workbook()
        # 创建一个worksheet
        worksheet = workbook.add_sheet('token')

        # 遍历打印所有行数据
        for i in range(0, nrows):
            # 每一行数据
            # print(table.row_values(i))
            # body = {
            #     "phone": int(table.row_values(i)[0]),
            #     "password": table.row_values(i)[1],
            #     "timestamp": table.row_values(i)[2]
            # }
            print('正在执行第 %s 行' % i)
            urls = url + '/prod-api/clinic/tclinicbase/testToken?phone=' + str(int(table.row_values(i)[0]))
            r = requests.get(urls, headers=head,  verify=False)
            assert '"code":200' in r.text, 'token接口:%s 获取失败\n结果------------%s' % (urls, r.text)
            a = r.json()
            # 将获取到的token组装下放入head的token参数中
            token = 'Bearer ' + a['access_token']
            # print('token=', token)

            # 将token值写入worksheet表中
            worksheet.write(i, 0, label=token)
        workbook.save('token' + '.xls')
        print("保存结束")



if __name__ == '__main__':
    url = 'https://yccis.tyzsls.com'
    Token = getToken()
    Token.login(url)