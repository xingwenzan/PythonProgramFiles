# 最低通行费 https://www.acwing.com/problem/content/1020/

T = 110
f = [[1e9 for _ in range(T)] for _ in range(T)]
f[0][1], f[1][0] = 0, 0

n = int(input())
w = []
for _ in range(n):
    w.append(list(map(int, input().split())))
for r in range(1, n + 1):
    for c in range(1, n + 1):
        f[r][c] = min(f[r - 1][c], f[r][c - 1]) + w[r - 1][c - 1]
print(f[n][n])
