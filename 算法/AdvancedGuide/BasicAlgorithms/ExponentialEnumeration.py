# 递归实现指数型枚举 https://www.acwing.com/problem/content/94/

n = int(input())


def dfs(u, st):
    if u == n:
        for i in range(n):
            if (st >> i) & 1: print(i + 1, end=" ")
        print()
        return
    dfs(u + 1, st)
    dfs(u + 1, st | (1 << u))


dfs(0, 0)
