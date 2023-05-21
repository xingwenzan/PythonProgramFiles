# 双指针实验 判断子序列 https://www.acwing.com/problem/content/2818/

n,m = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

i = 0
j = 0

while i<n and j<m:
    if a[i]==b[j]:
        i+=1
    j+=1

if i==n:print("Yes")
else:print("No")