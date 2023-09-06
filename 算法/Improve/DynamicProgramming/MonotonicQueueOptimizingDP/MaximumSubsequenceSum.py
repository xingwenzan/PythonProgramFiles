# 最大子序和 https://www.acwing.com/problem/content/137/

N = 300010


def prefixSum(lst):
    s = [0]
    for i in range(len(lst)):
        s.append(s[i] + lst[i])
    return s


def dp(lst, length):
    s = prefixSum(lst)
    ans = -float('inf')
    q = [0] * N
    hh = tt = 0
    for i in range(1, len(s)):
        if q[hh] < i - length: hh += 1
        ans = max(ans, s[i] - s[q[hh]])
        while hh <= tt and s[q[tt]] >= s[i]: tt -= 1
        tt += 1
        q[tt] = i
    return ans


n, m = map(int, input().split())
lst = list(map(int, input().split()))
print(dp(lst, m))
