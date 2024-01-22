# 排书 https://www.acwing.com/problem/content/182/

w = [[0] for i in range(5)]


def f():  # 估价函数
    s = 0
    for i in range(n - 1):
        if lst[i + 1] != lst[i] + 1: s += 1
    return (s + 2) // 3


def check():  # 检查当前 lst 是否符合要求
    for i in range(n):
        if lst[i] != i + 1: return False
    return True


def dfs(u, m):
    global lst
    if u + f() > m: return False
    if check(): return True

    # 换位置
    for i in range(n):
        for j in range(i, n):
            for k in range(j + 1, n):
                w[u] = lst.copy()  # 备份
                lst = w[u][0:i] + w[u][j + 1:k + 1] + w[u][i:j + 1] + w[u][k + 1:]
                if dfs(u + 1, m): return True
                lst = w[u].copy()

    return False


T = int(input())
for i in range(T):
    n = int(input())
    lst = list(map(int, input().split()))
    depth = 0
    while depth < 5 and not dfs(0, depth): depth += 1  # 迭代加深
    if depth >= 5:
        print("5 or more")
    else:
        print(depth)
