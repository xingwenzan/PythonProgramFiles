# 数字组合 https://www.acwing.com/problem/content/280/

n, m = map(int, input().split())
a = list(map(int, input().split()))
f = [0] * (m + 10)
f[0] = 1  # 空集也是一个方案
for i in range(n):
    for j in range(m, a[i] - 1, -1):
        f[j] += f[j - a[i]]

print(f[m])
