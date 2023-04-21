# 分组背包问题 https://www.acwing.com/problem/content/9/
# f[i][j] = max(f[i-1][j], f[i-1][j-v[i][1]]+w[i][1], …… , f[i-1][j-v[i][s]]+w[i][s])

N = 110
V, W = [[0 for _ in range(N)] for _ in range(N)], [[0 for _ in range(N)] for _ in range(N)]
S = [0] * N


def naive(num, volume):
    alls = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(1, num + 1):
        for j in range(1, volume + 1):
            alls[i][j] = alls[i - 1][j]
            k = 1
            while k <= S[i]:
                if j >= V[i][k]:
                    alls[i][j] = max(alls[i][j], alls[i - 1][j - V[i][k]] + W[i][k])
                k += 1
    return alls[num][volume]


def optimization(num, volume):
    alls = [0] * N
    for i in range(1, num + 1):
        for j in range(volume, 0, -1):
            k = 1
            while k <= S[i]:
                if j >= V[i][k]:
                    alls[j] = max(alls[j], alls[j - V[i][k]] + W[i][k])
                k += 1
    return alls[volume]


n, bag_v = map(int, input().split())
for i in range(1, n + 1):
    S[i] = int(input())
    for j in range(1, S[i] + 1):
        V[i][j], W[i][j] = map(int, input().split())
print(naive(n, bag_v))
print(optimization(n, bag_v))
