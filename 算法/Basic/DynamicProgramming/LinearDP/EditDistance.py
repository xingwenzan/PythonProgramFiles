# 编辑距离 https://www.acwing.com/problem/content/901/

N = 1010
strs = []
sub = [[0 for _ in range(N)] for _ in range(N)]


def sed(strA, strB):  # ShortestEditDistance
    n = len(strA)
    m = len(strB)
    A = ' ' + strA
    B = ' ' + strB
    # 初始化，空字符串到 A B 分别多少步
    for i in range(n + 1): sub[i][0] = i
    for i in range(m + 1): sub[0][i] = i

    for i in range(1, n + 1, 1):
        for j in range(1, m + 1, 1):
            sub[i][j] = min(sub[i - 1][j] + 1, sub[i][j - 1] + 1)
            sub[i][j] = min(sub[i][j], sub[i - 1][j - 1] + (A[i] != B[j]))
    return sub[n][m]


n, m = map(int, input().split())
for i in range(n):
    strs.append(input())
for i in range(m):
    lst = list(input().split())
    ans = 0
    for j in range(n):
        if sed(lst[0], strs[j]) <= int(lst[1]): ans += 1
    print(ans)
