# 红与黑 https://www.acwing.com/problem/content/1115/

dx, dy = [-1, 0, 1, 0], [0, -1, 0, 1]

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0: break
    lst = []
    st = [[False] * w for _ in range(h)]
    sx, sy = -1, -1
    for i in range(h):
        s = input()
        lst.append(s)
        if sx == -1:
            for j in range(w):
                if s[j] == '@':
                    sx = i
                    sy = j
                    break


    def dfs(x, y):
        res = 1
        st[x][y] = True
        for i in range(4):
            tx, ty = x + dx[i], y + dy[i]
            if tx < 0 or ty < 0 or tx >= h or ty >= w: continue
            if lst[tx][ty] == '#': continue
            if st[tx][ty]: continue
            res += dfs(tx, ty)
        return res


    print(dfs(sx, sy))
