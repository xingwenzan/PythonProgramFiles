# 小国王 https://www.acwing.com/problem/content/1066/
# f[i][j][k]   前 i 行摆好，已经摆放 j 给国王，第 i 行状态 k

N, M, S = 12, 110, 1 << 10
state = []  # 所有合法状态
cnt = [0] * S  # 各状态 1 的个数
head = {}  # 各状态可以转移到的状态（a 可转移到 b，b 亦可转移到 a）
f = [[[0 for _ in range(S)] for _ in range(M)] for _ in range(N)]


def check(s):  # 判断该状态是否合法
    return s & (s << 1) == 0


def count1(num):  # 判断该状态有多少 1
    ans = 0
    while num:
        ans += num & 1
        num >>= 1
    return ans


n, k = map(int, input().split())  # n*n 棋盘，k 个国王
# 合法状态筛选
for i in range(1 << n):
    if check(i):
        state.append(i)
        cnt[i] = count1(i)
# 枚举各状态可转移状态
for i in state:
    for j in state:
        if i & j == 0 and check(i | j):
            if i in head:
                head[i].append(j)
            else:
                head[i] = [j]
# DP
f[0][0][0] = 1
for i in range(1, n + 2):
    for j in range(k + 1):
        for s1 in state:  # 第 i 行状态
            for s2 in head[s1]:  # i-1 行状态
                f[i][j][s1] += f[i - 1][j - cnt[s1]][s2]
print(f[n + 1][k][0])
