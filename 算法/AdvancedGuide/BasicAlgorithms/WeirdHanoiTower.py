# 奇怪的汉诺塔 https://www.acwing.com/problem/content/98/ DP思想
# https://zh.wikipedia.org/zh-hans/%E6%B1%89%E8%AF%BA%E5%A1%94

# 3 塔汉诺塔问题时的解
d = [(1 << i) - 1 for i in range(13)]

f = [float('inf')] * 13
f[0] = 0
for i in range(1, 13):
    for j in range(i):
        f[i] = min(f[i], f[j] * 2 + d[i - j])
    print(f[i])
