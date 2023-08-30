# 数字游戏 https://www.acwing.com/problem/content/1084/
# 视频 https://www.acwing.com/video/488/

N = 15  # 2^31 有 10 位
f = [[0] * N for _ in range(N)]  # f[i,j] 最高位为 j，共 i 位的不降数数量


def init():  # 采用 DP 方式初始化
    # 一位数
    for i in range(10): f[1][i] = 1
    # 多位数
    for i in range(2, N):
        for j in range(10):  # j 从 0 到 9
            for k in range(j, 10):  # 第 i 位的后一位 >= j
                f[i][j] += f[i - 1][k]
    return


def dp(n):
    if n == 0: return 1  # 理论上不需要特判，但下方拆位的时候如果 n 是 0 可能为空列表
    # 拆位
    num = []
    while n:
        num.append(n % 10)
        n //= 10
    # 正式 DP
    ans = 0
    last = 0  # 本题代表 num 正在处理位的上一位数字
    for i in range(len(num) - 1, -1, -1):  # 从高到低遍历位
        x = num[i]  # 该位对应数字
        # 遍历该位可能放的数字（左树）
        for j in range(last, x):
            ans += f[i + 1][j]
        # 本位数 < 上一位数，右树没了，循环停止
        if x < last: break
        last = x
        if i == 0: ans += 1
    return ans


init()
while True:
    try:
        L, R = map(int, input().split())
    except:
        break
    print(dp(R) - dp(L - 1))
