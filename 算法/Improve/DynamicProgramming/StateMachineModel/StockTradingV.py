# 股票买卖 V https://www.acwing.com/problem/content/1060/
# f[i][0/1/2]   f[i][0] 第 i 天交易手中有票   f[i][1] 第 i 天交易手中无票且不在冷静期   f[i][2] 第 i 天交易手中无票且在冷静期

N = int(input())
w = list(map(int, input().split()))
f = [[0, 0, 0] for _ in range(N + 10)]
f[0][0], f[0][1], f[0][2] = -w[0], 0, 0
for i in range(1, N):
    f[i][0] = max(f[i - 1][0], f[i - 1][1] - w[i])
    f[i][1] = max(f[i - 1][2], f[i - 1][1])
    f[i][2] = f[i - 1][0] + w[i]
print(max(f[N - 1]))
