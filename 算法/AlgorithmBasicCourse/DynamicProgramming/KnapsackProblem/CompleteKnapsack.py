# 完全背包问题 https://www.acwing.com/problem/content/3/
# https://www.acwing.com/video/945/
# f[i][j] = max(f[i-1][j], f[i][j-v[i]]+w[i])

N = 1010
v, w = [0] * N, [0] * N


def naive(num, volume):
    alls = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(1, num + 1):
        for j in range(1, volume + 1):
            alls[i][j] = alls[i - 1][j]
            if j >= v[i]: alls[i][j] = max(alls[i][j], alls[i][j - v[i]] + w[i])
    return alls[num][volume]


def optimization(num, volume):
    alls = [0] * N
    for i in range(1, num + 1):
        for j in range(v[i], volume + 1):
            alls[j] = max(alls[j], alls[j - v[i]] + w[i])
    return alls[volume]


n, V = map(int, input().split())
for i in range(1, n + 1):
    v[i], w[i] = map(int, input().split())
print(naive(n, V))
print(optimization(n, V))
