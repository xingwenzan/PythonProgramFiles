# 马走日 https://www.acwing.com/problem/content/1118/
# 会 TLE

dx, dy = [1, 1, -1, -1, 2, 2, -2, -2], [2, -2, 2, -2, 1, -1, 1, -1]
st = [[False] * 10 for _ in range(10)]

t = int(input())
for _ in range(t):
    n, m, x, y = map(int, input().split())
    ans = 0


    def dfs(ux, uy, cnt):
        global ans
        if cnt == n * m:
            ans += 1
            return
        st[ux][uy] = True
        for i in range(8):
            tx, ty = ux + dx[i], uy + dy[i]
            if tx < 0 or ty < 0 or tx >= n or ty >= m: continue
            if st[tx][ty]: continue
            dfs(tx, ty, cnt + 1)
        st[ux][uy] = False
        return


    dfs(x, y, 1)
    print(ans)
