# 树的中心 https://www.acwing.com/problem/content/1075/
# 本题长度 c>0，无负权边，可 d1、d2 直接初始化为 0，也无须特判叶子节点

N = int(1e4 + 10)
h, e, ne, idx = [-1] * N, [0] * (2 * N), [0] * (2 * N), 0
w = [0] * (2 * N)
'''
d1[i]   i 为起点的向下的最大长度
d2[i]   i 为起点的向下的次大长度
p1[i]   i 为起点的向下的最大长度对应的子节点
up[i]   i 为起点的向上的最大长度 = 其父节点的不经过自己的最大长度(向上或向下) + 自己到父节点的距离
'''
d1, d2, p1, up = [0] * N, [0] * N, [0] * N, [0] * N


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


# 通过遍历 u 的所有子节点，获取其向下到端点的最大长度和次大长度，函数返回 d1[u]
def dfs_d(u, father):
    i = h[u]
    while i != -1:
        son = e[i]
        if son != father:
            d = dfs_d(son, u) + w[i]
            if d >= d1[u]:
                d2[u], d1[u] = d1[u], d
                p1[u] = son
            elif d > d2[u]:
                d2[u] = d
        i = ne[i]
    return d1[u]


# 通过遍历 u 的所有子节点，获取其子节点向上到端点的最大长度，无返回值
def dfe_u(u, father):
    i = h[u]
    while i != -1:
        son = e[i]
        if son != father:
            if p1[u] != son:
                up[son] = max(up[u], d1[u]) + w[i]
            else:
                up[son] = max(up[u], d2[u]) + w[i]
            dfe_u(son, u)
        i = ne[i]


n = int(input())
for _ in range(n - 1):
    a, b, c = map(int, input().split())
    add2(a, b, c)
dfs_d(1, -1)
dfe_u(1, -1)
ans = float('inf')
for i in range(1, n + 1): ans = min(ans, max(d1[i], up[i]))
print(ans)
