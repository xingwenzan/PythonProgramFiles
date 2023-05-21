# 01背包问题 https://www.acwing.com/problem/content/2/
# https://www.acwing.com/activity/content/code/content/625657/
# f[i][j] = max(f[i-1][j], f[i-1][j-v[i]]+w[i])

N = 1010
V, W = [0] * N, [0] * N


def naive(num, volume):
    alls = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(1, num + 1):
        for j in range(1, volume + 1):
            alls[i][j] = alls[i - 1][j]
            if j >= V[i]: alls[i][j] = max(alls[i][j], alls[i - 1][j - V[i]] + W[i])
    return alls[num][volume]


def optimization(num, volume):
    alls = [0] * N
    for i in range(1, num + 1):
        for j in range(volume, V[i] - 1, -1):
            alls[j] = max(alls[j], alls[j - V[i]] + W[i])
    return alls[volume]


n, bag_v = map(int, input().split())
for i in range(1, n + 1):
    V[i], W[i] = map(int, input().split())
print(naive(n, bag_v))
print(optimization(n, bag_v))
