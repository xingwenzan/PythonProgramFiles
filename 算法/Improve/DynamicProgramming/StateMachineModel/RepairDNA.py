"""
修复DNA https://www.acwing.com/problem/content/1055/
Tire 树 + AC 自动机
AC 自动机
    用于多个字符串之间的前缀、后缀匹配，且由后缀指向前缀
    fail[i]
        用于存放 Tire 树中第 i 行应当指向的行数（fail[i] 行）
        这两行对应的是同一个字母，且在 fail[i]!=0 时上一个字母也相同
    学习链接   https://www.acwing.com/blog/content/695/
"""

N, INF = 1010, float('inf')


def get(c):
    if c == 'A':
        return 0
    elif c == 'C':
        return 1
    elif c == 'G':
        return 2
    return 3


def add(s):
    global idx
    p = 0
    for i in range(len(s)):
        c = get(s[i])
        if tire[p][c] == 0:
            idx += 1
            tire[p][c] = idx
        p = tire[p][c]
    dar[p] = 1
    return


def build():
    q = [0] * N
    hh, tt = 0, -1
    for i in range(4):
        if tire[0][i]:
            tt += 1
            q[tt] = tire[0][i]
    while hh <= tt:
        t = q[hh]
        hh += 1
        for i in range(4):
            p = tire[t][i]
            if p == 0:
                tire[t][i] = tire[ne[t]][i]
            else:
                ne[p] = tire[ne[t]][i]
                dar[p] |= dar[ne[p]]
                tt += 1
                q[tt] = p
    return


T = 1
while True:

    tire = [[0, 0, 0, 0] for _ in range(N)]
    ne = [0] * N
    idx = 0
    dar = [0] * N

    n = int(input())
    if n == 0: break
    for _ in range(n):
        add(input())
    build()
    s = input()
    m = len(s)
    f = [[INF for _ in range(N)] for _ in range(N)]
    f[0][0] = 0
    for i in range(m):
        for j in range(idx + 1):
            for k in range(4):
                t = get(s[i]) != k
                p = tire[j][k]
                if dar[p] == 0: f[i + 1][p] = min(f[i + 1][p], f[i][j] + t)
    ans = INF
    for i in range(idx + 1): ans = min(ans, f[m][i])
    if ans == INF: ans = -1
    print("Case {}: {}".format(T, ans))
    T += 1
