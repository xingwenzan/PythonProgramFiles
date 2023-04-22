# 数字三角形 https://www.acwing.com/problem/content/900/
# f 更新前存三角形输入值，更新后存 到该点的路径最大值

N = 510
f = [[0 for _ in range(N)] for _ in range(N)]


def dp(num):  # 最上面的是 (0,0)，num 是行数，故最下面一行是 num-1，从倒数第二行更新
    for i in range(num - 2, -1, -1):
        for j in range(i + 1):
            f[i][j] += max(f[i + 1][j], f[i + 1][j + 1])
    return f[0][0]


n = int(input())
for i in range(n):
    f[i] = list(map(int, input().split()))
print(dp(n))
