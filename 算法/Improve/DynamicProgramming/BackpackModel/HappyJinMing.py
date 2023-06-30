# 开心的金明 https://www.acwing.com/problem/content/428/

n, m = map(int, input().split())
f = [0] * (n + 10)
for _ in range(m):
    v, p = map(int, input().split())
    w = v * p
    for i in range(n, v - 1, -1):
        f[i] = max(f[i], f[i - v] + w)
print(f[n])
