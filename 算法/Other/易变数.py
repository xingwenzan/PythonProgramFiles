# https://www.acwing.com/problem/content/description/5274/
# 由题 f(x)<x
# 数位DP

def get1(x):
    cnt = 0
    while x:
        if x & 1: cnt += 1
        x >>= 1
    return cnt


s = input()
n = len(s)
k = int(input())
mod = int(1e9 + 7)

if k == 0:
    print(1)
elif k == 1:
    print(n - 1)
else:
    # 预处理初始化前 1000 的操作次数(n<=2**1000,f(n)<1000)
    # (即 0~1000 个 1 的数操作一次后需要的操作次数)
    f = [0] * 1001
    # f[1] = 0
    for i in range(2, 1001):
        f[i] = f[get1(i)] + 1
    # 预处理 DP 的 f[i][j] 记为 dp[i][j] = dp[i-1][j] + dp[i-1][j+1]
    # 代表前面 j 个 1，后面 i 个随便放且 总操作数 = k 的数的数量
    dp = [[0] * 1001 for _ in range(1001)]
    for i in range(1, n + 1): dp[0][i] = 1 if (f[i] == k - 1) else 0
    for i in range(1, n + 1):
        for j in range(n + 1):
            dp[i][j] = dp[i - 1][j]
            if j + 1 <= n: dp[i][j] = (dp[i][j] + dp[i - 1][j + 1]) % mod
    t, ans = 0, 0  # t 前有 t 个 1
    for i in range(n):
        if s[i] == '1':
            ans = (ans + dp[n - i - 1][t]) % mod
            t += 1
    if f[t] == k - 1: ans = (ans + 1) % mod
    print(ans)
