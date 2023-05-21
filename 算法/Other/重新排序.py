# 原题链接：https://www.acwing.com/problem/content/4658/

'''
# 无脑循环 + 双重排序

n = int(input())
A = list(map(int,input().split()))
m = int(input())
originalNumSum = 0
w = [0 for i in range(n)]

for i in range(m):
    s = list(map(int,input().split()))
    for i in range(s[0]-1,s[1]):
        originalNumSum += A[i]
        w[i] += 1

w.sort(),A.sort()
newNumSum = 0
for i in range(n):
    newNumSum += w[i]*A[i]

print(newNumSum-originalNumSum)
'''


# 差分 + 双重排序（贪心）

n = int(input())
A = list(map(int,input().split()))
m = int(input())
w = [0 for i in range(n+1)]

for i in range(m):
    s = list(map(int,input().split()))
    w[s[0]-1] +=1
    w[s[1]] -=1
originalNumSum = 0
for i in range(n):
    w[i+1] += w[i]
    originalNumSum += w[i]*A[i]

w.pop(),w.sort(),A.sort()
newNumSum = 0
for i in range(n):
    newNumSum += w[i]*A[i]

print(newNumSum-originalNumSum)