# 二维费用的背包问题 https://www.acwing.com/problem/content/8/

N, V, M = map(int, input().split())
f = [[0 for _ in range(110)] for _ in range(110)]
for _ in range(N):
    v, m, w = map(int, input().split())
    for i in range(V, v - 1, -1):
        for j in range(M, m - 1, -1):
            f[i][j] = max(f[i][j], f[i - v][j - m] + w)
print(f[V][M])
