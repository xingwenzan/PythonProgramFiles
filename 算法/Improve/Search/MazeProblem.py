# 迷宫问题 https://www.acwing.com/problem/content/1078/

n = int(input())
lst = []  # 地图
for _ in range(n):
    lst.append(list(map(int, input().split())))
np = [[[-1, -1] for _ in range(n + 1)] for _ in range(n + 1)]


def bfs(sx, sy):
    dx, dy = [-1, 0, 1, 0], [0, -1, 0, 1]

    q = [[-1, -1] for _ in range((n + 1) * (n + 1))]
    hh = tt = 0
    q[0] = [sx, sy]

    while hh <= tt:
        tmp = q[hh]
        hh += 1
        for i in range(4):
            x = tmp[0] + dx[i]
            y = tmp[1] + dy[i]
            if x < 0 or y < 0 or x >= n or y >= n: continue  # 不存在
            if lst[x][y]: continue  # 墙
            if np[x][y][0] != -1: continue  # 走过了
            tt += 1
            q[tt] = [x, y]
            np[x][y] = tmp
    return


bfs(n - 1, n - 1)
p = [0, 0]
while True:
    print(p[0], p[1])
    if p[0] == n - 1 and p[1] == n - 1: break
    p = np[p[0]][p[1]]
