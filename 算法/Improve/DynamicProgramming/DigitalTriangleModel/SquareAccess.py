# 方格取数 https://www.acwing.com/problem/content/1029/
# f[k][i1][i2] k 两人各一共走k步 i1 一个人横向走了i1步 i2 另一个人横向走了i2步

T = 22
w = [[0 for _ in range(T)] for _ in range(T)]
f = [[[0 for _ in range(T)] for _ in range(T)] for _ in range(2 * T)]

n = int(input())
while 1:
    r, c, x = map(int, input().split())
    if r == 0 and c == 0 and x == 0: break
    w[r][c] = x

for k in range(2, 2 * n + 1):
    for i1 in range(1, n + 1):
        for i2 in range(1, n + 1):
            j1, j2 = k - i1, k - i2
            if 1 <= j1 <= n and 1 <= j2 <= n:
                t = w[i1][j1] if i1 == i2 else w[i1][j1] + w[i2][j2]
                f[k][i1][i2] = max(f[k - 1][i1][i2], f[k - 1][i1 - 1][i2], f[k - 1][i1][i2 - 1],
                                   f[k - 1][i1 - 1][i2 - 1])
                f[k][i1][i2] += t

print(f[2 * n][n][n])
