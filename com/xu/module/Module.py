'''
模块
    一个文件就是一个模块
        模块能定义函数、类和遍历
        模块里也能包含可执行的代码
    引用模块
        import 模块名
        from 模块名 import 引入部分
        as 别名
'''
#方式1
import xlrd as read_excel
#方式2 直接引用具体的方法
# from xlrd import  open_workbook
# read_excel.open_workbook()
'''
Pythod常用的内置模块
    time 用于获取时间戳或时间格式的转换
    datetime 包含更简单的时间计算方法
    random 用于生成随机数
    os 提供对操作系统进行调用的接口
    shutil 用于处理文件、文件夹、压缩包
'''
import random as r
#随机生成0-99的随机数
random_int = r.randint(0,100)
print(random_int)
#随机生成7个独立不相同的号码
random_list = r.sample(range(1,37),7)
print(random_list)
'''
Python常用第三方模块
    numpy 用于矩阵和向量运算
    pandas 提供了统计计算方法
    matplotlib 优秀的2D绘图库，常用于数据分析领域的图表绘制
    scipy 科学计算库，包含科学计算的方法
    sklearn 提供了机器学习的算法模型
    scrapy 优秀的爬虫框架，可以快速的完成爬虫的开发
'''