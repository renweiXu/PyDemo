'''
元组（）
    与列表类似，不同之处在于元组的元素不能修改
    创建元组
        元组 = (元素1，元素2，···)
        ppp = (123,12.5,'张三')
    元组元素不可被修改 不能向元组里面添加新的元素
'''
tuple = (12.5,123,'张三')
for item in tuple:
    print(item)
print('***********')
for index in range(len(tuple)):
    print(tuple[index])
print(tuple[1:3])
