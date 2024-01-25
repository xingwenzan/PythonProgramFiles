# 回转游戏 https://www.acwing.com/problem/content/183/
"""
棋盘编号/索引
      0     1
      2     3
4  5  6  7  8  9  10
      11    12
13 14 15 16 17 18 19
      20    21
      22    23
"""
# 各操作所操作棋子的编号
op = [[0, 2, 6, 11, 15, 20, 22],  # A
      [1, 3, 8, 12, 17, 21, 23],  # B
      [10, 9, 8, 7, 6, 5, 4],  # C
      [19, 18, 17, 16, 15, 14, 13],  # D
      [23, 21, 17, 12, 8, 3, 1],  # E
      [22, 20, 15, 11, 6, 2, 0],  # F
      [13, 14, 15, 16, 17, 18, 19],  # G
      [4, 5, 6, 7, 8, 9, 10]]  # H
op_re = [5, 4, 7, 6, 1, 0, 3, 2]  # 各操作反向操作对应操作编号
center = [6, 7, 8, 11, 12, 15, 16, 17]  # 棋盘中心棋子的编号
path = [-1] * 100  # 操作记录
d = "ABCDEFGH"  # 不同操作编号对应的操作名


def f():
    tmp = [0] * 4
    for i in range(8):
        tmp[lst[center[i]]] += 1
    return 8 - max(tmp)


def check():
    return f() == 0


def doing(x):
    tmp = lst[op[x][0]]
    for i in range(6):
        lst[op[x][i]] = lst[op[x][i + 1]]
    lst[op[x][-1]] = tmp
    return


def dfs(u, m, last):
    if u + f() > m: return False
    if check(): return True

    for i in range(8):
        if last != -1 and last == op_re[i]: continue
        path[u] = i
        doing(i)
        if dfs(u + 1, m, i): return True
        doing(op_re[i])

    return False


while True:
    lst = list(map(int, input().split()))
    if lst[0] == 0: break
    depth = 0
    while not dfs(0, depth, -1): depth += 1
    if depth == 0:
        print("No moves needed")
    else:
        ans = ""
        for i in path[0:depth]: ans += d[i]
        print(ans)
    print(lst[6])
