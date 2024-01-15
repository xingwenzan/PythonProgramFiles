# 生日蛋糕 https://www.acwing.com/problem/content/170/

M = 25

n = int(input())
m = int(input())

R, H = [float('inf')] * M, [float('inf')] * M
min_V, min_S = [0] * M, [0] * M
for i in range(1, m + 1):
    min_V[i] = min_V[i - 1] + i ** 3  # 前 i 层累计最小体积
    min_S[i] = min_S[i - 1] + 2 * i * i  # 前 i 层累计最小面积
ans = float('inf')
'''
u: 当前所在层数
v: 之前所有层数占据的体积
s: 之前所有层数累积的面积
'''


def dfs(u, v, s):
    global ans
    if v + min_V[u] > n: return
    if s + min_S[u] >= ans: return
    if s + 2 * (n - v) / R[u + 1] >= ans: return

    if u == 0:
        if v == n: ans = min(ans, s)
        return

    for r in range(int(min(R[u + 1] - 1, (n - v) ** (1 / 2))), u - 1, -1):
        for h in range(int(min(H[u + 1] - 1, (n - v) / r / r)), u - 1, -1):
            t = 0
            if u == m: t = r * r
            R[u], H[u] = r, h
            dfs(u - 1, v + r * r * h, s + t + 2 * r * h)


dfs(m, 0, 0)

if ans == float('inf'): ans = 0
print(ans)
