'''
函数
    有组织的、可重复使用的代码块
    用于执行一个单一的。相关动作的代码块
    函数的使用
        定义
            def 函数名（参数列表）
                函数代码块
                [return 返回值]
        调用
            [变量] = 函数名(入参)
        注意事项
            前向引用：必须先定义函数，在调用
'''
def get_triangle(n):
    #输出几行
    for line in range(n):
        #输出空格
        for get_space in range(n-line-1):
            print(" ",end="")
        #输出*
        for get_star in  range(line+1):
            print("*",end=" ")
        print()
        line += 1
        if line == 3:
            return "结束"

print(get_triangle(4))