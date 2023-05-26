# 传纸条 https://www.acwing.com/problem/content/277/
# `方格取数` 方法可过（该题本身写法待定）

T = 55
w = []
f = [[[0 for _ in range(T)] for _ in range(T)] for _ in range(2 * T)]

m, n = map(int, input().split())
for _ in range(m):
    w.append(list(map(int, input().split())))

for k in range(2, m + n + 1):
    for i1 in range(1, m + 1):
        for i2 in range(1, m + 1):
            j1, j2 = k - i1, k - i2
            if 1 <= j1 <= n and 1 <= j2 <= n:
                t = w[i1 - 1][j1 - 1]
                if i1 != i2: t += w[i2 - 1][j2 - 1]
                f[k][i1][i2] = max(f[k - 1][i1][i2], f[k - 1][i1 - 1][i2], f[k - 1][i1][i2 - 1],
                                   f[k - 1][i1 - 1][i2 - 1])
                f[k][i1][i2] += t

print(f[m + n][m][m])
