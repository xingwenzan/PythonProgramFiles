# 信使 https://www.acwing.com/problem/content/description/1130/

n, m = map(int, input().split())
d = [[float('inf')] * (n + 10) for i in range(n + 10)]
for i in range(1, n + 1): d[i][i] = 0
for _ in range(m):
    a, b, w = map(int, input().split())
    d[a][b] = d[b][a] = min(d[a][b], w)
for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            d[i][j] = min(d[i][j], d[i][k] + d[k][j])
'''ans = 0
for i in range(1, n + 1):
    if d[1][i] == float('inf'):
        ans = -1
        break
    else:
        ans = max(ans, d[1][i])'''
ans = max(d[1][1:n + 1])
if ans == float('inf'):
    print(-1)
else:
    print(ans)
