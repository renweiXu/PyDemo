'''
求方差
'''
listA = [10091,13411,15823,17485,10555,11424]
listB = [13034,13943,17608,16672,18298,158392]
#先求平均数
def get_avg(list = []):
    sum_list = sum(list)
    return sum_list/(len(list))
#计算方差
def get_variance(list = []):
    avg = get_avg(list)
    num = 0
    for item in list:
        #求平方
        num +=pow(avg-item,2)
    result =  num/(len(list)-1)
    return result
varianceA = get_variance(listA)
varianceB = get_variance(listB)
print(varianceA,varianceB)

#通过调第三方类库 pandas来计算方差
import  pandas as ps
seriesA = ps.Series(listA)
seriesB = ps.Series(listB)
print(seriesA.var(),seriesB.var())
