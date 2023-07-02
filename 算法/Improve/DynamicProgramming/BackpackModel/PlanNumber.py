# 背包问题求方案数 https://www.acwing.com/problem/content/11/

mod = int(1e9 + 7)
N, V = map(int, input().split())
f, g = [0] * (V + 10), [1] * (V + 10)  # 体积不超过 i 时最大价值、及其方案数

for _ in range(N):
    v, w = map(int, input().split())
    for i in range(V, v - 1, -1):
        newW = f[i - v] + w
        if f[i] < newW:
            f[i] = newW
            g[i] = g[i - v]
        elif f[i] == newW:
            g[i] += g[i - v]
print(g[V] % mod)
