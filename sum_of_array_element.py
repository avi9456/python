from re import I


print("enter list :")
lis=list(map(int,input().split()))
sum=0
for i in lis:
    sum+=i
print(sum)