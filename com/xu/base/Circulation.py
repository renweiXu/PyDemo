num=1
while num<5:
    print(num,end=" ")
    num +=1
print()
#for 循环 便利表达式全部的值
'''
for item in range():
range(num1,num2)
遍历 [num1,num2)，左闭右开
range(n)
遍历[0,n)
'''
for item in range(10):
    print(item,end=' ')
print()
for item in range(4,10):
    print(item,end=' ')

print()
def get_num(n):
    for line in  range(n):
        for space_count in range(n-line-1):
            print(' ',end='')
        for star in range(line+1):
            print('*',end=' ')
        print()
get_num(4)

n=10
for num in range (n):
    n -= 1
    if n%2==0 :
        if n == 6:
            continue
        print(n)
    if n==5:
        break;