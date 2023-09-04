# 不要62 https://www.acwing.com/problem/content/1087/

N = 11
f = [[0] * 10 for _ in range(N)]

def init():  # 采用 DP 方式初始化
    # 一位数
    for i in range(10):
        if i != 4: f[1][i] = 1
    # 多位数
    for i in range(2, N):
        for j in range(10):  # 最高位
            if j == 4: continue
            for k in range(10):  # 次高位
                if k == 4 or (j == 6 and k == 2): continue
                f[i][j] += f[i - 1][k]
    return


def dp(n):
    if n == 0: return 1
    # 拆位
    num = []
    while n:
        num.append(n % 10)
        n //= 10
    # 正式 DP
    ans = 0
    last = 0  # 本题代表 num 当前为的前一位数字
    # 含前导 0 情况
    for i in range(len(num) - 1, -1, -1):  # 从高到低遍历位
        x = num[i]  # 该位对应数字
        # 遍历该位可能放的数字（左树）
        for j in range(x):
            if j == 4 or (last == 6 and j == 2): continue
            ans += f[i + 1][j]

        if x == 4 or (last == 6 and x == 2): break
        last = x

        if i == 0: ans += 1
    return ans


init()
l, r = map(int, input().split())
while l != 0 or r != 0:
    print(dp(r) - dp(l - 1))
    l, r = map(int, input().split())
