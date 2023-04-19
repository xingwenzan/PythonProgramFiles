# 多重背包问题 I https://www.acwing.com/problem/content/4/
# f[i][j] = max(f[i-1][j], f[i-1][j-v[i]]+w[i],……,f[i-1][j-k*v[i]]+k*w[i],……,f[i-1][j-s[i]*v[i]]+s[i]*w[i])

N = 110
V, W, S = [0] * N, [0] * N, [0] * N


def naive(num, volume):
    alls = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(1, num + 1):
        for j in range(1, volume + 1):
            alls[i][j] = alls[i - 1][j]
            k = 1
            while j >= k * V[i] and k <= S[i]:
                alls[i][j] = max(alls[i][j], alls[i - 1][j - k * V[i]] + k * W[i])
                k += 1
    return alls[num][volume]


n, bag_v = map(int, input().split())
for i in range(1, n + 1):
    V[i], W[i], S[i] = map(int, input().split())
print(naive(n, bag_v))
