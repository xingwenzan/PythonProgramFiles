# 城堡问题 https://www.acwing.com/problem/content/1100/


N = 55
M = N * N
q = [[0, 0] for _ in range(M)]
st = [[False] * N for _ in range(N)]
# 读入
n, m = map(int, input().split())
lst = []
for _ in range(n): lst.append(list(map(int, input().split())))


def bfs(x, y):
    ans = 0
    dx, dy = [0, -1, 0, 1], [-1, 0, 1, 0]

    hh = tt = 0
    q[0] = [x, y]
    st[x][y] = True

    while (hh <= tt):
        t = q[hh]
        hh += 1
        ans += 1

        for d in range(4):
            i, j = t[0], t[1]
            if (lst[i][j] >> d) & 1: continue
            i += dx[d]
            j += dy[d]
            if st[i][j]: continue

            tt += 1
            q[tt] = [i, j]
            st[i][j] = True

    return ans


cnt, area = 0, 0
for i in range(n):
    for j in range(m):
        if not st[i][j]:
            cnt += 1
            area = max(area, bfs(i, j))
print(cnt)
print(area)
