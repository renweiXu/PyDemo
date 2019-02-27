'''
异常
    程序在运行过程中所发生的非常正常时间
        算数运算错误
        索引越界
        读取文件异常
        语法错误
        ······
        NameError:当程序尝试访问一个未声明的变量或者函数时，会引发
        ZeroDivisonError:在计算过程中，当除数为0的情况并执行时，会引发
        SyntaxError：当程序出现语法错误，会引发
        IndexError：当访问序列中不存在的索引时，会引发
        KeyError：当访问映射中不存在的键是，会引发
        BaseException：当程序运行时，遇到任何异常，会引发
    捕获异常语法
        try:
            语句块1
        except ErrorName1
            语句块2
        except ErrorName2
            语句3
        except：
            语句4
        else：
            语句5
    注意事项：有多个except时，应该先子类，后父类
'''
#计算平均成绩
def mean_points(score=[],names=[]):
    try:
        all_score = sum(score)
        mean_score = all_score/len(names)
    except ZeroDivisionError as e:
        #as e 给异常起别名
        print("出现异常")
        return e
    except BaseException:
        #except BaseException: 等价于 except:二选一
        return BaseException
    except:
        return "程序发生异常"
    else:
        print("只有当try执行的时候，该代码块才会执行")
    finally:
        print('结束')
    return mean_score
score = [90,80,70]
name = ["张三","lisi"]
mean_score = mean_points(score)
print(mean_score)