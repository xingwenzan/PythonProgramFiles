# Windy数 https://www.acwing.com/problem/content/1085/

N = 15
f = [[0] * N for _ in range(N)]  # f[i,j] 最高位为 j，共 i 位的 Windy 数数量


def init():  # 采用 DP 方式初始化
    # 一位数
    for i in range(10): f[1][i] = 1
    # 多位数
    for i in range(2, N):
        for j in range(10):  # j 从 0 到 9
            for k in range(10):
                if abs(j - k) >= 2:  # j、k 差至少为 2
                    f[i][j] += f[i - 1][k]
    return


def dp(n):
    if n == 0: return 0
    # 拆位
    num = []
    while n:
        num.append(n % 10)
        n //= 10
    '''
    分情况讨论是否含前导 0 原因
    假如size = 5；
    每个数都是从位数5开始枚举，但其实00013也是windy数，（这个前导0导致res没加）但其实13也在范围内
    '''
    # 正式 DP
    ans = 0
    last = -2  # 本题代表 num 正在处理位的上一位数字
    # 含前导 0 情况
    for i in range(len(num) - 1, -1, -1):  # 从高到低遍历位
        x = num[i]  # 该位对应数字
        # 遍历该位可能放的数字（左树）
        for j in range(x):
            if j == 0 and i == len(num) - 1: continue
            if abs(j - last) >= 2: ans += f[i + 1][j]
        # 本位数与上一位数差 <2，右树没了，循环停止
        if abs(x - last) < 2: break
        last = x
        if i == 0: ans += 1
    # 特殊处理不含前导 0 情况
    for i in range(1, len(num)):
        for j in range(1, 10):
            ans += f[i][j]
    return ans


init()
L, R = map(int, input().split())
print(dp(R) - dp(L - 1))
