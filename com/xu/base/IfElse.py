def  get_score(n):
    if n >= 90:
        return "优秀"
    elif  ( n >= 80 and  n<85 ) :
        return "良好"
    else :
        return "合格"
result = get_score(86)
print(result)

n=60
if n >= 90:
    print( "优秀")
elif n >= 80:
    print( "良好")
else:
    print( "合格")