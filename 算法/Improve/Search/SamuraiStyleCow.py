# 武士风度的牛 https://www.acwing.com/problem/content/190/

dx, dy = [2, 2, 1, -1, -2, -2, 1, -1], [1, -1, 2, 2, 1, -1, -2, -2]

c, r = map(int, input().split())
lst = []
kx, ky = -1, -1
for i in range(r):
    lst.append(input())
    if kx == -1:
        for j in range(c):
            if lst[i][j] == 'K': kx, ky = i, j


def bfs():
    size = [[-1] * c for _ in range(r)]
    size[kx][ky] = 0
    q = [[-1, -1] for _ in range((c + 1) * (r + 1))]
    hh = tt = 0
    q[0] = [kx, ky]
    while hh <= tt:
        tmp = q[hh]
        hh += 1
        for i in range(8):
            x = tmp[0] + dx[i]
            y = tmp[1] + dy[i]
            if x < 0 or y < 0 or x >= r or y >= c: continue
            if lst[x][y] == "*": continue
            if size[x][y] != -1: continue
            if lst[x][y] == 'H': return size[tmp[0]][tmp[1]] + 1
            size[x][y] = size[tmp[0]][tmp[1]] + 1
            tt += 1
            q[tt] = [x, y]
    return -1


print(bfs())
