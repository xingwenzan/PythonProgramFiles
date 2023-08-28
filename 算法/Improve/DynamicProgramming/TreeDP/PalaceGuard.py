# 皇宫看守 https://www.acwing.com/problem/content/1079/
# DP 图   https://cdn.acwing.com/media/article/image/2022/10/29/197723_510b605257-Screenshot-2022-10-29-133343.jpg
# 由于采用 DFS 从下往上更新，故 dfs(root) 即可
# 每个点都只需要赋一次权，故不在 add 里赋权

import sys

sys.setrecursionlimit(65536)

N = 1510
h, e, ne, idx = [-1] * N, [0] * N, [0] * N, 0
w = [0] * N
f = [[0] * 3 for _ in range(N)]
isRoot = [True] * N
root = 1
INF = float('inf')


def add(father, son):
    global idx
    e[idx] = son
    ne[idx] = h[father]
    h[father] = idx
    idx += 1
    return


def dfs(u):
    f[u][2] = w[u]
    s = 0
    i = h[u]
    while i != -1:
        son = e[i]
        dfs(son)
        f[u][0] += min(f[son][1], f[son][2])
        f[u][2] += min(f[son])
        s += min(f[son][1], f[son][2])
        i = ne[i]
    f[u][1] = INF
    i = h[u]
    while i != -1:
        son = e[i]
        f[u][1] = min(f[u][1], s - min(f[son][1], f[son][2]) + f[son][2])
        i = ne[i]
    return


n = int(input())
for _ in range(n):
    lst = list(map(int, input().split()))
    a = lst[0]
    w[a] = lst[1]
    for b in lst[3:]:
        add(a, b)
        isRoot[b] = False
while not isRoot[root]: root += 1
dfs(root)
print(min(f[root][1], f[root][2]))
