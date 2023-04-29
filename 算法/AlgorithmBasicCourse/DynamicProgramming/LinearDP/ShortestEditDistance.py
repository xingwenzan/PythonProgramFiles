# 最短编辑距离 https://www.acwing.com/activity/content/problem/content/1094/
# https://www.acwing.com/video/334/

N = 1010
sub = [[0 for _ in range(N)] for _ in range(N)]

n = int(input())
A = ' ' + input()
m = int(input())
B = ' ' + input()

# 初始化，空字符串到 A B 分别多少步
for i in range(n + 1): sub[i][0] = i
for i in range(m + 1): sub[0][i] = i

for i in range(1, n + 1, 1):
    for j in range(1, m + 1, 1):
        sub[i][j] = min(sub[i - 1][j] + 1, sub[i][j - 1] + 1)
        # sub[i][j] = min(sub[i][j], sub[i - 1][j - 1] + (A[i] != B[j]))   # 与下面的 if 等同
        if A[i] == B[j]:
            sub[i][j] = min(sub[i][j], sub[i - 1][j - 1])
        else:
            sub[i][j] = min(sub[i][j], sub[i - 1][j - 1] + 1)
print(sub[n][m])
