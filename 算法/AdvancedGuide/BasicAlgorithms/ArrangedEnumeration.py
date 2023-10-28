# 递归实现排列型枚举 https://www.acwing.com/problem/content/96/

n = int(input())
path = [0] * n


def dfs(u, st):
    if u == n:
        print(" ".join(map(str, path)))
        return
    for i in range(n):
        if (st >> i) & 1 == 0:
            path[u] = i + 1
            dfs(u + 1, st + (1 << i))
            path[u] = 0


dfs(0, 0)
