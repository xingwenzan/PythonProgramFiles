# 宝藏 https://www.acwing.com/problem/content/531/
# 解析（本题暂无视频） https://www.acwing.com/solution/content/4026/

INF = float('inf')
N, M = 12, 1 << 12
f = [[INF for _ in range(N)] for _ in range(M)]  # 状态定义：f[i][h],当前生成树的状态是i，且树的深度为h的方案 的最小代价
for i in range(N): f[1 << i][0] = 0  # 赞助商决定免费赞助他打通一条从地面到某个宝藏屋的通道
g = [0] * M  # g[i] 表示 i 与 g[i] 状态一步相互转移，若 g[i]&j==j 则可由 i 一步到 j
d = [[INF for _ in range(N)] for _ in range(N)]  # d[i,j] 为 i 和 j 之间最小距离
for i in range(N): d[i][i] = 0

# 距离读入
n, m = map(int, input().split())
for i in range(m):
    a, b, w = map(int, input().split())
    # 索引从 0 开始
    a -= 1
    b -= 1
    d[a][b] = d[b][a] = min(d[a][b], w)

# 获取 g，即 i 最多可一步到达的状态 g[i]
for i in range(1 << n):
    for j in range(n):
        if (i >> j) & 1:
            for k in range(n):
                if d[j][k] != INF:
                    g[i] |= 1 << k

# DP
for i in range(1 << n):
    # 遍历 i 的所有子集 j（不包含 i 和 0，从 i 到 i 没有意义），获取到 i 的最小总代价
    j = (i - 1) & i
    while j:
        if (g[j] & i) == i:  # 只对可以一步转移到 i 的进行处理
            remain = j ^ i  # 取得 j 到 i 差的位
            cost = 0  # j 到 i 的花费（1 层）
            # 遍历所有缺的位 k，获取补全所缺位的最小花费
            for k in range(n):
                if (remain >> k) & 1:
                    tmp = INF
                    # 获取 j 状态有的所有位，并比较到缺的这个位 k 的代价，获取最小值
                    for u in range(n):
                        if (j >> u) & 1:
                            tmp = min(tmp, d[u][k])
                    cost += tmp
            for k in range(n): f[i][k] = min(f[i][k], f[j][k - 1] + cost * k)
        j = (j - 1) & i
# 比较各层级总代价，获取最小总代价
ans = INF
for i in range(n): ans = min(ans, f[(1 << n) - 1][i])
print(ans)
