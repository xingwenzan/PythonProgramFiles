# 货币系统 https://www.acwing.com/problem/content/1023/

n, m = map(int, input().split())
f = [0] * (m + 10)
f[0] = 1

for i in range(n):
    v = int(input())
    for j in range(v, m + 1, 1):
        f[j] += f[j - v]

print(f[m])
