# 任务安排3 https://www.acwing.com/problem/content/304/

def prefixSum(lst):
    s = [0]
    for i in range(len(lst)):
        s.append(s[i] + lst[i])
    return s


def dp(n, s, c, t):
    C = prefixSum(c)
    T = prefixSum(t)
    f = [0] * (n + 10)
    q = [0] * (n + 10)
    hh = tt = 0
    for i in range(1, n + 1):
        l, r = hh, tt
        while l < r:
            mid = (l + r) >> 1
            if (f[q[mid + 1]] - f[q[mid]]) > (T[i] + s) * (C[q[mid + 1]] - C[q[mid]]):
                r = mid
            else:
                l = mid + 1

        j = q[r]
        f[i] = f[j] + T[i] * (C[i] - C[j]) + s * (C[n] - C[j])
        while hh < tt and (f[q[tt]] - f[q[tt - 1]]) * (C[i] - C[q[tt]]) >= (f[i] - f[q[tt]]) * (
                C[q[tt]] - C[q[tt - 1]]): tt -= 1
        tt += 1
        q[tt] = i
    return f[n]


n, s = map(int, input().split())
c, t = [], []
for _ in range(n):
    ti, ci = map(int, input().split())
    t.append(ti)
    c.append(ci)
print(dp(n, s, c, t))
