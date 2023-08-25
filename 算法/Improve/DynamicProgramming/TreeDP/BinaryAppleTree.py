# 二叉苹果树 https://www.acwing.com/problem/content/1076/
# 简化版有依赖背包问题   有依赖的背包问题 https://www.acwing.com/problem/content/10/

N = 110
# 本题输入格式中无法确定方向，故使用无向图
h, e, ne, idx = [-1] * N, [0] * (2 * N), [0] * (2 * N), 0
w = [0] * (2 * N)
f = [[0] * N for _ in range(N)]


def add1(father, son, length):
    global idx
    w[idx] = length
    e[idx] = son
    ne[idx] = h[father]
    h[father] = idx
    idx += 1
    return


def add2(p1, p2, length):
    add1(p1, p2, length)
    add1(p2, p1, length)
    return


n, v = map(int, input().split())


def dfs(u, father):
    global v
    i = h[u]
    while i != -1:
        son = e[i]
        if son != father:
            dfs(son, u)
            for j in range(v, 0, -1):
                for k in range(j):
                    f[u][j] = max(f[u][j], f[u][j - k - 1] + f[son][k] + w[i])
        i = ne[i]
    return


for _ in range(n - 1):
    a, b, c = map(int, input().split())
    add2(a, b, c)
dfs(1, -1)
print(f[1][v])
