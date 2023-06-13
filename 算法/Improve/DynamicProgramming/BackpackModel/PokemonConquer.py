# 宠物小精灵之收服 https://www.acwing.com/problem/content/1024/

N, M, K = map(int, input().split())
f = [[0 for _ in range(M + 10)] for _ in range(N + 10)]
for _ in range(K):
    n, m = map(int, input().split())
    for i in range(N, n - 1, -1):
        for j in range(M - 1, m - 1, -1):
            f[i][j] = max(f[i - n][j - m] + 1, f[i][j])

k = M - 1
while k > 0 and f[N][k - 1] == f[N][M - 1]: k -= 1
print(f[N][M - 1], M - k)
