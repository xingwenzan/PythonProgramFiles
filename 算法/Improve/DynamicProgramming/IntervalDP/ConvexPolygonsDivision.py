# 凸多边形的划分 https://www.acwing.com/problem/content/1071/
# 由题划分之后每条边都一定会被用上，故无须把环做成 2 倍链，直接从（1，n）断开即可

N = 55
INF = float('inf')
f = [[0] * N for _ in range(N)]


def dp(lst, num):
    w = [0]
    w.extend(lst)
    for length in range(3, num + 1):
        l = 1
        while l + length - 1 <= num:
            r = l + length - 1
            f[l][r] = INF
            for k in range(l + 1, r):
                f[l][r] = min(f[l][r], f[l][k] + f[k][r] + w[l] * w[k] * w[r])
            l += 1
    return f[1][num]


n = int(input())
lst = list(map(int, input().split()))
print(dp(lst, n))
