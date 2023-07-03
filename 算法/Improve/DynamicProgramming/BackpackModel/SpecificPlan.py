# 背包问题求具体方案 https://www.acwing.com/problem/content/12/

N, V = map(int, input().split())
f = [[0 for _ in range(V + 10)] for _ in range(N + 10)]
v, w = [0] * (N + 10), [0] * (N + 10)
for i in range(1, N + 1, 1):
    v[i], w[i] = map(int, input().split())
for i in range(N, 0, -1):
    for j in range(V + 1):
        f[i][j] = f[i + 1][j]
        if j >= v[i]: f[i][j] = max(f[i][j], f[i + 1][j - v[i]] + w[i])
j = V
ans = []
for i in range(1, N + 1, 1):
    if j >= v[i] and f[i][j] == f[i + 1][j - v[i]] + w[i]:
        ans.append(i)
        j -= v[i]
print(" ".join(map(str, ans)))
