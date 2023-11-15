# 激光炸弹 https://www.acwing.com/problem/content/101/

N = 5050
f = [[0] * N for _ in range(N)]


def prefix_sum():
    for i in range(1, N):
        for j in range(1, N):
            f[i][j] += f[i - 1][j] + f[i][j - 1] - f[i - 1][j - 1]
    return


n, r = map(int, input().split())
mx, my = 0, 0
for _ in range(n):
    x, y, w = map(int, input().split())
    f[x + 1][y + 1] += w  # 地图坐标从 0,0 开始，为方便计算，地图坐标在数组中都 +1
    mx = max(x, mx)
    my = max(y, my)
prefix_sum()
ans = 0
for i in range(1, mx + 2):
    for j in range(1, my + 2):
        x, y = min(mx + 1, i + r - 1), min(my + 1, j + r - 1)
        ans = max(ans, f[x][y] - f[x][j - 1] - f[i - 1][y] + f[i - 1][j - 1])
print(ans)
