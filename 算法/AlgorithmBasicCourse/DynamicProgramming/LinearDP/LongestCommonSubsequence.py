# 最长公共子序列 https://www.acwing.com/problem/content/899/

N = 1010
sub = [[0 for _ in range(N)] for _ in range(N)]

n, m = map(int, input().split())
A = ' ' + input()
B = ' ' + input()

for i in range(1, n + 1, 1):
    for j in range(1, m + 1, 1):
        sub[i][j] = max(sub[i - 1][j], sub[i][j - 1])
        if A[i] == B[j]: sub[i][j] = max(sub[i][j], sub[i - 1][j - 1] + 1)  # sub[i][j] = sub[i-1][j-1]+1 亦可
print(sub[n][m])
