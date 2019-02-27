#列表（list）
'''
存储、处理一组元素的数据结构
创建列表
列表 = [元素1，元素2]
访问元素列表
1.使用for循环遍历列表元素
2.使用索引访问列表元素
    list[index]
    list[-index]
3.截取列表元素
    list[start_index:end_index]
    start_index和end_index均可省略
'''
list1 = [1,2,3,'张三',12.5]
for item in list1:
    print(item,end=' ')
    print()
print("******************")
for item in list1:
    print(list1[0])
    print(list1[1])
    print(list1[2])
    print(list1[3])
    print(list1[4])
    print("******************")
print(list1[-1])
print("******************")
for index in range(len(list1)):
    print(list1[index])
print("******************")
print('数组长度：')
print(len(list1))
print("******************")
print('获取列表前两位：')
print(list1[0:2])
print('获取列表第二个后面所有数据：')
print(list1[1:])
print("截取所有数据")
print(list1[:])
'''
添加列表元素
    list.append(obj)  追加
    list.insert(index,obj) 插入
删除列表项
    del list[index]
    del list[start_index,end_index]
'''
list1.append('王五')
print(list1)
list1.insert(2,'李四')
print(list1)
del list1[2]
print(list1)
del list1[2:3]
print(list1)
#删除下标2以后所有数据包括2
del list1[2:]
print(list1)