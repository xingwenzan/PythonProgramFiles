# 多重背包问题 II https://www.acwing.com/problem/content/5/
# 多重背包的二进制优化方法，将 s 拆分成 1 2 4 8 …… 2^k …… 2^n s-2^n 个该物品的组合。然后 01
# 01 朴素版会 MLE，只能用 01 优化版
import math

N = 1000 * (int(math.log2(2000)) + 1) + 10  # 11010
V, W = [0] * N, [0] * N
idx = 0


def add(v, w, s):
    global idx
    bit = 1
    while bit <= s:
        idx += 1
        V[idx] = bit * v
        W[idx] = bit * w
        s -= bit
        bit *= 2
    if s > 0:
        idx += 1
        V[idx] = s * v
        W[idx] = s * w
    return 0


def optimization(volume):
    global idx
    alls = [0] * N
    for i in range(1, idx + 1):
        for j in range(volume, V[i] - 1, -1):
            alls[j] = max(alls[j], alls[j - V[i]] + W[i])
    return alls[volume]


n, bag_v = map(int, input().split())
for i in range(1, n + 1):
    v, w, s = map(int, input().split())
    add(v, w, s)
print(optimization(bag_v))
