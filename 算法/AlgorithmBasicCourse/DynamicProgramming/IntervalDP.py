# 石子合并 https://www.acwing.com/problem/content/284/

N = 310
f = [[1e9 for _ in range(N)] for _ in range(N)]
for i in range(N):
    f[i][i] = 0


def prefixSum(lst, length):
    ans = [0]
    for i in range(length):
        ans.append(ans[i] + lst[i])
    return ans


def dp(lst, n):
    s = prefixSum(lst, n)
    for length in range(2, n + 1):
        i = 1
        while i + length - 1 <= n:
            l, r = i, i + length - 1
            for k in range(l, r):
                f[l][r] = min(f[l][r], f[l][k] + f[k + 1][r] + s[r] - s[l - 1])
            i += 1
    return f[1][n]


n = int(input())
lst = list(map(int, input().split()))
print(dp(lst, n))
