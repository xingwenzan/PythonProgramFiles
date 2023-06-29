# 机器分配 https://www.acwing.com/problem/content/1015/

N, M = 11, 16
f = [[0 for _ in range(M)] for _ in range(N)]
w = [[0 for _ in range(M)] for _ in range(N)]
num = [0] * N  # 每个公司的个数

n, m = map(int, input().split())
# 价值读入
for i in range(1, n + 1, 1):
    lst = list(map(int, input().split()))
    for j in range(1, m + 1, 1):
        w[i][j] = lst[j - 1]
# 计算
for i in range(1, n + 1, 1):  # 公司
    for j in range(1, m + 1, 1):  # 体积（最多 j 个机器的情况）
        for k in range(0, j + 1, 1):  # i 号 公司 k 个机器的价值
            f[i][j] = max(f[i][j], f[i - 1][j - k] + w[i][k])
print(f[n][m])
j = m
for i in range(n, 0, -1):
    for k in range(j + 1):
        if f[i][j] == f[i - 1][j - k] + w[i][k]:
            num[i] = k
            j -= k
            break
for i in range(1, n + 1, 1):
    print(i, num[i])
