# 绿色通道 https://www.acwing.com/problem/content/1092/

n, t = map(int, input().split())
lst = [0]
lst.extend(list(map(int, input().split())))


def check(lim):
    f, q = [0] * (n + 10), [0] * (n + 10)
    hh = tt = 0
    for i in range(1, n + 1):
        if q[hh] < i - lim - 1: hh += 1
        f[i] = f[q[hh]] + lst[i]
        while hh <= tt and f[q[tt]] >= f[i]: tt -= 1
        tt += 1
        q[tt] = i

    for i in range(n, n - lim - 1, -1):
        if f[i] <= t: return True
    return False


l, r = 0, n
while l < r:
    mid = (l + r) >> 1
    if check(mid):
        r = mid
    else:
        l += 1
print(r)
