#定义一个打印等边三角形的函数
#print_triangle  函数名
#参数n 要打印几行
#有参函数
# def print_triangle(n):
#     #统计有多少个星号
#     starCount = 0
#     for line in range(n):
#         #line = 0,1,2,3
#         #输出空格
#         for space in  range(n-line-1):
#             print(' ',end='')
#         #输出每一行的星号
#         for star in range(line+1):
#             starCount += 1
#             print('*',end=' ')
#         print()
#     return   starCount
#调用函数
#python函数是向前引用的 先定义函数 在调用
# stars = print_triangle(5)
# print(stars)
#
# #不定长参数
# def print_triangle(n = 4):
#     #统计有多少个星号
#     starCount = 0
#     for line in range(n):
#         #line = 0,1,2,3
#         #输出空格
#         for space in  range(n-line-1):
#             print(' ',end='')
#         #输出每一行的星号
#         for star in range(line+1):
#             starCount += 1
#             print('*',end=' ')
#         print()
#     return   starCount
#n = 4 表示缺省参数 不传参数时 会默认打印4行
# print_triangle()
#end关键字参数
print("哈哈",end = '-')
#匿名函数 lambda定义匿名函数
#求和 有两个参数 arg1 arg2  业务逻辑就是 arg1+arg2
# sum = lambda  arg1,arg2:arg1+arg2;
# print(sum(1,6))

#上面sum匿名函数 等价于下面的sum1函数
# def sum1 (arg1,arg2):
#     return arg1+arg2;
#包裹位置参数  可变参数
'''
接受不定长个位置参数，参数会被组织成一个元组（元组：不可变的列表）传入
func_name(*args)
    参数表示为 *args
    调用函数时，参数自动会组织成一个元组
    传入的位置参数与组织成的元组索引位置一致
'''
def func_name(*args):
    for i in args:
        print(i,end=' ')

func_name('hello','world','python',1,2,3,4)
#包裹关键字参数
'''
接受不定长个关键字参数，参数会被组织成一个字典（字典：）传入
func_name(**kwargs)
    参数表示为 **kwargs
    调用函数时，参数自动会组织成一个字典传入
    传入的位置参数与组织成的字典的键值对应
'''
# def func_name(**kwargs):
#     print(type(kwargs))
#     #遍历key
#     for key in kwargs:
#         print(key,end='')
#         print(kwargs[key],end=' ')
#     #同时遍历key value
#     for key,v in kwargs.items():
#         print(key,v)
#
# func_name(key1 = 'hello',key2 = 'world',key3 = 'python')
#迭代器
#可迭代对象  list  tuple dict str
# str1 = "你好"
# for item in  str1:
#     print(item)

#生成器yield 可以替代return 把普通函数变成生成器
#使用了yield就可以用迭代器 进行遍历
def get_even(n):
    for i in range(n):
        if i % 2 == 0 :
            yield i
for item in  get_even(19):
    print(item)