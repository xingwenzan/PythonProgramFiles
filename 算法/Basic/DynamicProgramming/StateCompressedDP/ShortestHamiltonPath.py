# 最短Hamilton路径 https://www.acwing.com/problem/content/93/

N = 20
M = 1 << N
# f[i][j] 表示 i 对应状态且最后一个点为 j 的状态的最短路径
f = [[1e9 for _ in range(N)] for _ in range(M)]
f[1][0] = 0  # 只经过 0 号位置且终点为 0 的距离一定为 0
w = []  # 两点间距离 w[i][j] 是 i 号点到 j 号点的距离


def dp(num):
    for i in range(1, 1 << num, 2):  # 从 0 号位开始且无论如何必须经过 0 号位
        for j in range(num):  # 遍历所有点做终点，0 号点不做终点，即 range(1,num) 也可
            if (i >> j) & 1:  # 该状态下经过 j 号点
                for k in range(num):  # 遍历所有点做倒数第二点
                    if (i >> k) & 1:  # 该状态下经过 k 号点
                        f[i][j] = min(f[i][j], f[i - (1 << j)][k] + w[k][j])
    return f[(1 << num) - 1][num - 1]


n = int(input())
for i in range(n):
    w.append(list(map(int, input().split())))
print(dp(n))
