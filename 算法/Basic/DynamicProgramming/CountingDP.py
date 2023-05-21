# 整数划分 https://www.acwing.com/problem/content/902/
# https://www.acwing.com/video/332/
# https://www.acwing.com/activity/content/code/content/62496/

N, mod = 1010, int(1e9 + 7)


def bag(x):
    f = [0] * N
    f[0] = 1
    for i in range(1, x + 1):
        for j in range(i, x + 1):
            f[j] = (f[j] + f[j - i]) % mod
    return f[x]


def other(x):
    f = [[0 for _ in range(N)] for _ in range(N)]
    f[1][1] = 1
    for i in range(2, x + 1):
        for j in range(1, i + 1):
            f[i][j] = (f[i - 1][j - 1] + f[i - j][j]) % mod
    ans = 0
    for i in range(1, x + 1):
        ans = (ans + f[x][i]) % mod
    return ans


n = int(input())
print(bag(n))
print(other(n))
