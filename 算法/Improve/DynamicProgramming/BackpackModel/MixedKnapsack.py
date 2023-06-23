# 混合背包问题 https://www.acwing.com/problem/content/7/
# 先判断是否完全，否则使用二进制优化多重解决

N, V = map(int, input().split())
f = [0] * (V + 10)
for _ in range(N):
    v, w, s = map(int, input().split())
    if s == 0:  # 完全
        for i in range(v, V + 1, 1):
            f[i] = max(f[i - v] + w, f[i])
    else:  # 01 或多重，使用二进制优化多重解决
        if s == -1: s = 1
        k = 1
        while k <= s:
            for i in range(V, k * v - 1, -1):
                f[i] = max(f[i], f[i - k * v] + k * w)
            s -= k
            k *= 2
        if s > 0:
            for i in range(V, s * v - 1, -1):
                f[i] = max(f[i], f[i - s * v] + s * w)
print(f[V])
