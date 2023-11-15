# 迷宫 https://www.acwing.com/problem/content/1114/

from sys import setrecursionlimit

setrecursionlimit(5000)  # py 递归有上限，需要解锁上限

dx, dy = [-1, 0, 1, 0], [0, -1, 0, 1]

k = int(input())
for _ in range(k):
    n = int(input())
    lst = []
    for _ in range(n):
        lst.append(input())
    st = [[False] * n for _ in range(n)]
    xa, ya, xb, yb = map(int, input().split())


    def dfs(ux, uy, ex, ey):
        if ux == ex and uy == ey: return True

        st[ux][uy] = True
        ans = False
        for i in range(4):
            nx, ny = ux + dx[i], uy + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= n: continue
            if st[nx][ny]: continue
            if lst[nx][ny] == '#': continue
            ans = (ans or dfs(nx, ny, ex, ey))
            if ans: return ans

        return ans


    if lst[xa][ya] != '#' and lst[xb][yb] != '#' and dfs(xa, ya, xb, yb):
        print("YES")
    else:
        print("NO")
