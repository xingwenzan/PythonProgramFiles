# 最长公共上升子序列 https://www.acwing.com/problem/content/274/
# 解析 https://www.acwing.com/video/364/

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
f = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
for i in range(1, n + 1, 1):
    tmp = 0
    for j in range(1, n + 1, 1):
        f[i][j] = f[i - 1][j]
        if a[i - 1] == b[j - 1]: f[i][j] = max(f[i][j], tmp + 1)
        if b[j - 1] < a[i - 1]: tmp = max(tmp, f[i - 1][j])
ans = 0
for i in range(1, n + 1, 1): ans = max(ans, f[n][i])
print(ans)
