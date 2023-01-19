# https://www.acwing.com/problem/content/description/3403/

n,k = list(map(int,input().split()));
digit = len(str(n))
num = 0

for i in range(1,n+1):
    for j in range(digit):
        if i%10==k:num+=1
        i=i//10

print(num)