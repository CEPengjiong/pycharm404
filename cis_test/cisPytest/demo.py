# # 调试文件
#
# import urllib3
#
# urllib3.disable_warnings()
#
# 1.执行脚本:Terminal输入pytest
# 2.第二步复制环境变量文件
# copy environment.properties report\environment.properties
# # 3.将执行生成在report目录的xml文件转化生成html格式的allure报告:
# allure generate report -o report/html --clean
# # 4.选中生成的index.html报告文件,浏览器打开,查看allure报告


# 检查依赖包
# pip list

# PyMySQL                0.9.3
# pytest                 6.1.2
# allure-pytest
# pytest-html            2.1.1
# pytest-ordering        0.6
# pytest-rerunfailures   9.1.1
# PyYAML                 5.3.1
# requests               2.24.0
# urllib3                1.25.8
# wheel                  0.35.1
# allure的bin目录添加到环境变量
