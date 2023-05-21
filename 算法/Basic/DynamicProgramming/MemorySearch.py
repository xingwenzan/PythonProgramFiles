# 滑雪 https://www.acwing.com/problem/content/903/

N = 310
high = []
state = [[-1 for _ in range(N)] for _ in range(N)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def dp(r, c, row, col):
    if state[r][c] != -1:
        return state[r][c]
    state[r][c] = 1
    for i in range(4):
        x = r + dx[i]
        y = c + dy[i]
        if 0 <= x < row and 0 <= y < col and high[x][y] < high[r][c]:
            state[r][c] = max(state[r][c], dp(x, y, row, col) + 1)
    return state[r][c]


n, m = map(int, input().split())
for i in range(n):
    high.append(list(map(int, input().split())))
ans = 1
for r in range(n):
    for c in range(m):
        ans = max(ans, dp(r, c, n, m))
print(ans)
