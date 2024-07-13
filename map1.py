def addition(n):
    return n+n
num=(1,2,3,4)
result=map(addition,num)
print(list(result))

n1=(1,2,3,5)
n2=(2,3,45,55)
 
result=map(lambda x,y:x+y,n1,n2)
print(list(result))


str=['sat','sum','mon']
tst=list(map(list,str))
print(tst)