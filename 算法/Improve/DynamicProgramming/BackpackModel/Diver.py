# 潜水员 https://www.acwing.com/problem/content/1022/

m, n = map(int, input().split())
k = int(input())
f = [[1e9 for _ in range(80)] for _ in range(22)]
f[0][0] = 0
for _ in range(k):
    a, b, c = map(int, input().split())
    for i in range(m, -1, -1):
        for j in range(n, -1, -1):
            f[i][j] = min(f[i][j], f[max(0, i - a)][max(0, j - b)] + c)
print(f[m][n])
