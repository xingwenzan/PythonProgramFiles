"""
# 多重背包问题 III https://www.acwing.com/problem/content/6/
# 多重背包的单调队列优化方法
#   https://www.acwing.com/solution/content/6500/
#   https://www.acwing.com/solution/content/53507/
#   https://www.acwing.com/activity/content/code/content/117236/
"""

f = [0] * 20010
# cf = []   # copy f
ids = [0] * 20010  # 用于记录单调队列窗口中留下的数的索引 —— 索引数组

N, V = map(int, input().split())
for _ in range(N):
    v, w, s = map(int, input().split())
    cf = f.copy()  # copy f
    for i in range(v):  # 模 v 的余数
        hh, tt = 0, -1  # 单调队列索引数组窗口的头索引、尾索引，用于框住窗口
        for j in range(i, V + 1, v):
            if hh <= tt and ids[hh] < j - s * v: hh += 1  # 单调队列窗口不空且头在窗口外，砍头
            while hh <= tt and cf[ids[tt]] - (ids[tt] - i) // v * w <= cf[j] - (
                    j - i) // v * w: tt -= 1  # 保证窗口单调递减，否则断尾
            tt += 1
            ids[tt] = j
            f[j] = cf[ids[hh]] + (j - ids[hh]) // v * w  # 更新 f[j] 最大值
print(f[V])
