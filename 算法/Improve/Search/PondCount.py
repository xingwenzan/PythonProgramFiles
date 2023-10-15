# 池塘计数 https://www.acwing.com/problem/content/1099/

N = 1010
M = N * N
q = [[0, 0] for _ in range(M)]
st = [[False] * N for _ in range(N)]
# 读入
n, m = map(int, input().split())
lst = []
for _ in range(n): lst.append(input())


def bfs(x, y):
    hh = tt = 0
    q[0] = [x, y]
    st[x][y] = True
    while (hh <= tt):
        t = q[hh]
        hh += 1
        for x in range(t[0] - 1, t[0] + 2):
            for y in range(t[1] - 1, t[1] + 2):
                if x == t[0] and y == t[1]: continue
                if x < 0 or y < 0 or x >= n or y >= m: continue
                if lst[x][y] == '.' or st[x][y] == True: continue

                tt += 1
                q[tt] = [x, y]
                st[x][y] = True
    return


ans = 0
for i in range(n):
    for j in range(m):
        if lst[i][j] == 'W' and st[i][j] == False:
            ans += 1
            bfs(i, j)
print(ans)
