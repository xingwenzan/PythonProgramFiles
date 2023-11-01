# 双端队列广搜 电路维修 https://www.acwing.com/problem/content/177/

import collections

dx, dy = [-1, -1, 1, 1], [-1, 1, 1, -1]  # 当前点能到的点的相对位置
p = "\\/\\/"  # 当前点到对应位置所需的联通的线的形式
px, py = [-1, -1, 0, 0], [-1, 0, 0, -1]  # 当前点与能到的点在接线数组经过的元件对当前点的相对坐标


def bfs(row, col, lst):
    dist = [[float('inf')] * (col + 1) for _ in range(row + 1)]  # 到各点的“距离（操作数）”数组
    dist[0][0] = 0
    st = [[False] * (col + 1) for _ in range(row + 1)]  # 拿出来过（距离更新到最短）标记
    q = collections.deque()
    q.append([0, 0])
    while len(q):
        tmp = q.popleft()
        x, y = tmp[0], tmp[1]  # 当前点坐标
        if x == row and y == col: return dist[x][y]
        if st[x][y]: continue
        st[x][y] = True
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]  # 能到的点坐标
            if nx < 0 or ny < 0 or nx > row or ny > col: continue
            lx, ly = x + px[i], y + py[i]  # 当前点与能到点经过的元件的坐标
            w = (lst[lx][ly] != p[i])  # 是否需要操作，不一样 - 操作，一样 - 不操作
            d = dist[x][y] + w  # 从 x,y 到 nx,ny 是否需要额外操作
            if (d < dist[nx][ny]):
                # 新路径更近，更新
                dist[nx][ny] = d
                # 无须操作放队头，需要操作放对尾
                if w:
                    q.append([nx, ny])
                else:
                    q.appendleft([nx, ny])
    return dist[row][col]


t = int(input())
for _ in range(t):
    r, c = map(int, input().split())
    lst = []  # 初始“接线”数组
    for _ in range(r):
        lst.append(input())
    ans = bfs(r, c, lst)
    if ans == float('inf'):
        print("NO SOLUTION")
    else:
        print(ans)
