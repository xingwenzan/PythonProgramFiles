# 多源BFS 矩阵距离 https://www.acwing.com/problem/content/175/

n, m = map(int, input().split())
dist = [[-1] * m for _ in range(n)]
lst = []
for _ in range(n):
    lst.append(input())

q = [[-1, -1] for _ in range((n + 1) * (m + 1))]
hh, tt = 0, -1

for i in range(n):
    for j in range(m):
        if lst[i][j] == '1':
            dist[i][j] = 0
            tt += 1
            q[tt] = [i, j]

dx, dy = [-1, 0, 1, 0], [0, -1, 0, 1]
while hh <= tt:
    tmp = q[hh]
    hh += 1
    for i in range(4):
        x = tmp[0] + dx[i]
        y = tmp[1] + dy[i]
        if x < 0 or y < 0 or x >= n or y >= m: continue
        if dist[x][y] != -1: continue

        dist[x][y] = dist[tmp[0]][tmp[1]] + 1
        tt += 1
        q[tt] = [x, y]

for i in range(n):
    print(" ".join(map(str, dist[i])))
