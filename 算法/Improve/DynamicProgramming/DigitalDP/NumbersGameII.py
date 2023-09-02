# 数字游戏 II https://www.acwing.com/problem/content/1086/

N, M = 15, 110
f = [[[0] * M for _ in range(10)] for _ in range(N)]  # f[i,j,k] 最高位为 j，余数是 k，共 i 位的目标数数量


def mod(x, y):
    return (x % y + y) % y


def init(p):  # 采用 DP 方式初始化
    global f
    f = [[[0] * M for _ in range(10)] for _ in range(N)]
    # 一位数
    for i in range(10): f[1][i][i % p] += 1
    # 多位数
    for i in range(2, N):
        for j0 in range(10):  # j 从 0 到 9
            for k in range(p):
                for j1 in range(10):  # 次高位
                    f[i][j0][k] += f[i - 1][j1][mod(k - j0, p)]  # 带上 i 号位模为 k，不带则为 k-j0
    return


def dp(n, p):
    if n == 0: return 1
    # 拆位
    num = []
    while n:
        num.append(n % 10)
        n //= 10
    # 正式 DP
    ans = 0
    last = 0  # 本题代表 num 前几位之和
    # 含前导 0 情况
    for i in range(len(num) - 1, -1, -1):  # 从高到低遍历位
        x = num[i]  # 该位对应数字
        # 遍历该位可能放的数字（左树）
        for j in range(x):
            ans += f[i + 1][j][mod(-last, p)]  # 带上前 i 位模为 0，不带则为 -last
        last += x
        if i == 0 and last % p == 0: ans += 1
    return ans


while True:
    try:
        l, r, p = map(int, input().split())
    except:
        break
    init(p)
    print(dp(r, p) - dp(l - 1, p))
