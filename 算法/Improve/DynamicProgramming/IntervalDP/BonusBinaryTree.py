# 加分二叉树 https://www.acwing.com/problem/content/481/

N = 35
f = [[0] * (N) for _ in range(N)]
g = [[0] * (N) for _ in range(N)]
out = []


def dp(lst, num):
    w = [0]
    w.extend(lst)
    for length in range(1, num + 1):
        l = 1
        while l + length - 1 <= num:
            r = l + length - 1
            if l == r:
                f[l][r], g[l][r] = w[l], l
            else:
                for k in range(l, r + 1):
                    left = 1 if l == k else f[l][k - 1]
                    right = 1 if r == k else f[k + 1][r]
                    score = left * right + w[k]
                    if score > f[l][r]:
                        f[l][r] = score
                        g[l][r] = k
            l += 1
    return f[1][num]


def dfs(l, r):
    if l > r: return
    k = g[l][r]
    out.append(k)
    dfs(l, k - 1)
    dfs(k + 1, r)
    return


n = int(input())
lst = list(map(int, input().split()))
print(dp(lst, n))
dfs(1, n)
print(" ".join(map(str, out)))
