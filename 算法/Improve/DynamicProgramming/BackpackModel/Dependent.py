# 有依赖的背包问题 https://www.acwing.com/problem/content/10/
# 树形 DP --(发现)--> 分组背包辅组解决，减少复杂度

# 初始化
MAX = 110
f = [[0 for _ in range(MAX)] for _ in range(MAX)]
h, e, p, idx = [-1] * MAX, [0] * MAX, [0] * MAX, 0
V, W = [0] * MAX, [0] * MAX
root = 0

n, v = map(int, input().split())


def add(x, father, vx, wx):
    global idx
    e[idx], p[idx], h[father] = x, h[father], idx
    idx += 1
    V[x], W[x] = vx, wx
    return


def dfs(u):
    # 分组背包选择子树（此时仅管子树体积情况，需后续添加 u 节点）
    np = h[u]  # next pointer
    while np != -1:  # 遍历该节点的每一个子节点
        son = e[np]
        dfs(son)
        for j in range(v - V[u], -1, -1):  # 遍历体积（子树及 u 总共占用体积），留不出 u 体积的不需要考虑
            for k in range(j + 1):  # 遍历剩余体积（子树占用体积）
                f[u][j] = max(f[u][j], f[u][j - k] + f[son][k])
        np = p[np]
    # 添加 u 节点
    for i in range(v, V[u] - 1, -1): f[u][i] = f[u][i - V[u]] + W[u]  # 可存下 u 的加上 u
    for i in range(V[u]): f[u][i] = 0  # 放不下 u 的全清零
    return


for i in range(1, n + 1, 1):
    vi, wi, pi = map(int, input().split())
    if pi == -1:
        root = i
        V[i], W[i] = vi, wi
    else:
        add(i, pi, vi, wi)
dfs(root)
print(f[root][v])
