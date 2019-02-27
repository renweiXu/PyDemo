'''
字典(dictionary)
    一种可变容器模型，且可存储任意类型对象
    创建字典
        字典 = {键1：值1，键2：值2}
        dict = {"姓名":"张三","年龄":14}
    遍历字典的键，值，键值
    for(k,v) in dict.items()
'''
dict = {"姓名":"张三","年龄":14}
print(dict)
print("************")
#遍历键值
for(k,v) in dict.items():
    print(k)
    print(v)
    print(dict.get(k))
    print("************")
#遍历键
for key in dict:
    print(key)
    print(dict.get(key))
    print("************")
#遍历值
for value in dict.values():
    print(value)
print("*********")
#取出某个值
print(dict['姓名'])
print(dict.get('姓名'))
#添加数据
dict['性别'] = '男'
print(dict)
#删除数据
del  dict['性别']
print(dict)
#使用键来从字典中取值
key = '手机号'
#先判断key存不存 防止报错
if key in dict:
    print(dict[key])
else:
    print('当前key在字典中不存在,key='+key)
#修改数据
dict.update({'姓名':'李四'})
print(dict)