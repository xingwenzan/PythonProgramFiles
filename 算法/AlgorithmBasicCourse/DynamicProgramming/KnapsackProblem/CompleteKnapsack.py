# 完全背包问题 https://www.acwing.com/problem/content/3/
# https://www.acwing.com/video/945/
# f[i][j] = max(f[i-1][j], f[i][j-v[i]]+w[i])

N = 1010
vi, wi = [0] * N, [0] * N


def naive(num, volume):
    alls = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(1, num + 1):
        for j in range(1, volume + 1):
            alls[i][j] = alls[i - 1][j]
            if j >= vi[i]: alls[i][j] = max(alls[i][j], alls[i][j - vi[i]] + wi[i])
    return alls[num][volume]


def optimization(num, volume):
    alls = [0] * N
    for i in range(1, num + 1):
        for j in range(vi[i], volume + 1):
            alls[j] = max(alls[j], alls[j - vi[i]] + wi[i])
    return alls[volume]


n, v = map(int, input().split())
for i in range(1, n + 1):
    vi[i], wi[i] = map(int, input().split())
print(naive(n, v))
print(optimization(n, v))
