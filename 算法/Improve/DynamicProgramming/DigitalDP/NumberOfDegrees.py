# 度的数量 https://www.acwing.com/problem/content/1083/
"""
数位 DP 套路
题目套路   [l,r] 范围内满足某条件数的个数
DP 套路   dp(r)-dp(l-1)
解题套路  dp(x)
    转化为 b 进制数表示   x = a_(n-1) * b^(n-1) + a_(n-2) * b^(n-2) + ... + a_(0) * b^(0)
    以树的方式分类（视频 14:14 处）   父节点下左树为该位的 a in [0,a_(n-i)-1]，此时左树代表必小于等于原数 x；右树为 a = a_(n-i)
    视情况计算求解
"""

N = 35
f = [[0] * N for _ in range(N)]  # f[a,b] 求组合数，即 C_a^b


def init():
    for i in range(N):
        for j in range(i + 1):
            if j == 0:
                f[i][j] = 1
            else:
                f[i][j] = f[i - 1][j] + f[i - 1][j - 1]
    return


def dp(n, b, k):
    # 边界情况
    if n == 0: return 0
    # 将 n 换成 b 进制表示，其中索引高者表示高位
    num = []
    while n:
        num.append(n % b)
        n //= b
    # 从高到低位遍历更新，每位只能填 0 或 1
    ans = 0  # 结果
    last = 0  # 表示前置情况，本题表示已经确定的 1 的数量
    for i in range(len(num) - 1, -1, -1):
        x = num[i]
        if x:  # 左树
            ans += f[i][k - last]  # 此位填 0 的满足的数量
            if x > 1:  # 即左树可能存在此位填 1 的情况，需要加上
                ans += f[i][k - last - 1]
                # 且此时填 1 或 0 已经无影响，可以跳出左树
                break
            else:  # x=1，左树是否为 1 受后面影响，不能从此处直接计算，last++ 后下次更新，由于此位为 0 已求完，则只考虑为 1 情况
                last += 1
                if last > k: break
        # 最右侧分支上的方案（last==k 只计算一次即可，且仅有正好除了 k 个 1 全是 0 的才有必要 +1）
        if i == 0 and last == k: ans += 1
    return ans


l, r = map(int, input().split())
k = int(input())
b = int(input())
init()
print(dp(r, b, k) - dp(l - 1, b, k))
