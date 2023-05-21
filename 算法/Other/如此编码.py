# https://www.acwing.com/problem/content/4702/
'''
# 麻烦版本

n,m = list(map(int,input().split()))
a = list(map(int,input().split()))
c = [0 for i in range(n+1)]
c[0]=1
for i in range(1,n+1):
    c[i] = c[i-1]*a[i-1]

b = [0 for i in range(n)]
for i in range(n):
    ans = m//c[n-i-1]
    if ans<a[n-i-1]:
        b[n-1-i] = ans
    else:b[n-1-i] = c[n-i-1]
    m -= b[n-i-1]*c[n-i-1]

print(" ".join(map(str,b)))
'''

# 简洁版本
n,m = list(map(int,input().split()))
a = list(map(int,input().split()))
b = []

for i in range(n):
    bi = m%a[i]
    b.append(bi)
    m = m//a[i]

print(" ".join(map(str,b)))