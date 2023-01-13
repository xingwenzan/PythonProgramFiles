"""https://www.acwing.com/problem/content/4703/"""

'''
# 二进制枚举 O(n2^n)
n, x = list(map(int, input().split()))
a = []
for i in range(n):
    a.append(int(input()))
res = sum(a)
for i in range(1 << n):
    money = 0
    for j in range(n):
        if i >> j & 1: money += a[j]
    if money >= x: res = min(res, money)
print(res)
'''

# 01背包法 O(nm) m是总价

n, x = list(map(int, input().split()))
a = []
for i in range(n):
    a.append(int(input()))
m = sum(a) - x
f = [0] * (m+1)
for i in range(n):
    for j in range(m, 0, -1):
        if j>=a[i]:
            f[j] = max(f[j], f[j - a[i]] + a[i])
print(sum(a) - f[m])
