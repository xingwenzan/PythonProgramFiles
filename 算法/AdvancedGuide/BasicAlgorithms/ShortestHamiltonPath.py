# 最短Hamilton路径 https://www.acwing.com/problem/content/93/

N = 22
# f[i][j] 0->j(j 是终点)，经过点的集合是 i
f = [[float('inf')] * N for _ in range(1 << N)]
f[1][0] = 0  # 0->0，只经过 0 点

n = int(input())
lst = []
for _ in range(n):
    lst.append(list(map(int, input().split())))

for i in range(1 << n):  # 所有路况
    for j in range(n):  # 终点为 j
        if (i >> j) & 1:  # 该路径到 j
            for k in range(n):  # 从 k 到 j
                if ((i - (1 << j)) >> k) & 1:  # 不到 j 的情况下能到 k
                    f[i][j] = min(f[i][j], f[i - (1 << j)][k] + lst[k][j])
print(f[(1 << n) - 1][n - 1])
