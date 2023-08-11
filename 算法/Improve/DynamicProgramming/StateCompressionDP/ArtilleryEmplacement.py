# 炮兵阵地 https://www.acwing.com/problem/content/294/

N, M = 105, 1 << 10
g = [0] * N  # 存地图
state = []  # 所有合法状态
cnt = [0] * M  # 各状态 1 的个数
head = {}  # 各状态可以转移到的状态（a 可转移到 b，b 亦可转移到 a）
'''
滚动数组储存
原为 f[i,j,k]，i 为到第 i 行，j、k 为 i、i-1 行状态
现为 f[2,j,k]，2 为前第 1、2 行（滚动），j、k 不变，且当时作为前第 2 行者也用作第 i 行
'''
f = [[[0 for _ in range(M)] for _ in range(M)] for _ in range(2)]


def check(x):
    return ((x << 1) & x) == 0 and ((x << 2) & x) == 0


def count1(num):
    ans = 0
    while num:
        ans += num & 1
        num >>= 1
    return ans


# 地图读入
n, m = map(int, input().split())
for i in range(1, n + 1):
    lst = input()
    for j in range(m):
        g[i] += ((lst[j] == 'H') << j)
# 合法状态筛选
for i in range(1 << m):
    if check(i):
        state.append(i)
        cnt[i] = count1(i)
# 获取可（被）转移状态
for i in state:
    for j in state:
        if (i & j) == 0:
            if i in head:
                head[i].append(j)
            else:
                head[i] = [j]
# DP
for i in range(1, n + 1):  # i 行
    for j in state:  # i 行状态
        for k in head[j]:  # i-1 行状态
            for u in head[j]:  # i-2 行状态
                if (k & u): continue
                # 理论上 i、i-1、i-2 都要判定是否在 H，后两者如果不合法其 f 一定是 0，不影响计算
                if j & g[i]: continue
                f[i & 1][j][k] = max(f[i & 1][j][k], f[(i - 1) & 1][k][u] + cnt[j])
ans = 0
for i in state:
    for j in head[i]:
        ans = max(ans, f[n & 1][i][j])
print(ans)
