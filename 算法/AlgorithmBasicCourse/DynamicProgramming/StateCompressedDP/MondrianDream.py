# 蒙德里安的梦想 https://www.acwing.com/problem/content/293/

from sys import stdin

N = 12  # 最多 12 列(0 - 11 号)
M = 1 << N  # 单列最多 M 钟状态
# f[i][j] 代表到 i 号列之前(不含 i 号)所有列已经摆好，且按 j 的二进制表示凸出(1 凸出 0 不凸出)到 i 号列的状态
f = [[0 for _ in range(M)] for _ in range(N)]
st = [True] * M  # 单列状态可行性，st[j] 是 j 号状态下是否不存在连续奇数个空格，true 为不存在 - 状态合法
state = [[] for _ in range(M)]  # 记录状态可行性，state[j] 代表 i 号列状态为 j 时所有合法的 i-1 号列的合法状态


def dp(row, col):  # row 行 col 列棋盘
    # 预处理单列所有合法状态
    # 合法：不存在连续奇数个空格
    for i in range(1 << row):  # 遍历该列所有可能的状态
        cnt = 0  # 记录连续的0的个数
        isValid = True  # 该状态没有奇数个连续的 0 则标记为 true
        for j in range(row):  # 遍历该列所有位置
            if (i >> j) & 1:  # 判断第 j 位是否位 1
                if cnt & 1:  # 如果是奇数
                    isValid = False
                    break
            else:
                cnt += 1
        if cnt & 1:  # 如果是走到了最后，判断一下
            isValid = False
        st[i] = isValid
    # 预处理两列间状态合法
    # 合法：不存在冲突摆放且摆放后不存在连续奇数空格
    state = [[] for _ in range(M)]  # 重置
    for j in range(1 << row):  # i 号列所有状态
        for k in range(1 << row):  # i-1 号列所有状态
            if (j & k) == 0 and st[j | k]:
                state[j].append(k)
    # dp
    f = [[0 for _ in range(M)] for _ in range(N)]  # 重置
    f[0][0] = 1
    # 这里需要回忆状态表示的定义
    # 按定义这里是：前第-1列都摆好，且从-1列到第0列伸出来的状态为0的方案数。
    # 首先，这里没有-1列，最少也是0列。
    # 其次，没有伸出来，即没有横着摆的。即这里第0列只有竖着摆这1种状态。
    for i in range(1, col + 1):  # 遍历每一列:第i列合法范围是(0~m-1列)
        for j in range(1 << row):  # 遍历当前列（第i列）所有状态j
            for k in state[j]:  # 遍历第i-1列的状态k，如果“真正”可行，就转移
                f[i][j] += f[i - 1][k]  # 当前列的方案数就等于之前的第i-1列所有状态k的累加。
    # 最后答案是什么呢？
    # f[m][0]表示 前m-1列都处理完，并且第m-1列没有伸出来的所有方案数。
    # 即整个棋盘处理完的方案数
    return f[col][0]


for line in stdin.readlines()[:-1]:
    n, m = map(int, line.split())
    print(dp(n, m))
