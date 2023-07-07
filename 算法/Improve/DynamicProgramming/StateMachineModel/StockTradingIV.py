# 股票买卖 IV https://www.acwing.com/problem/content/1059/
# f[i][0/1]   f[i][0] 第 i 次交易手中无票   f[i][1] 第 i 次交易手中有票

N, K = map(int, input().split())
w = list(map(int, input().split()))
f = [[0, 0] for _ in range(K + 10)]

for i in range(N):
    for j in range(1, K + 1):
        if i == 0:
            f[j][1] = -w[0]
        else:
            f[j][1] = max(f[j][1], f[j - 1][0] - w[i])
            f[j][0] = max(f[j][0], f[j][1] + w[i])

print(f[K][0])
