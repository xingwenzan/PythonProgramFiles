# 递归实现组合型枚举 https://www.acwing.com/problem/content/95/

n, m = map(int, input().split())


def dfs(u, num, st):
    if num == m:
        for i in range(n):
            if (st >> i) & 1:
                print(i + 1, end=" ")
        print()
        return
    if u == n: return
    for i in range(u, n):
        dfs(i + 1, num + 1, st + (1 << i))


dfs(0, 0, 0)
