# 任务安排1 https://www.acwing.com/problem/content/302/

def prefixSum(lst):
    s = [0]
    for i in range(len(lst)):
        s.append(s[i] + lst[i])
    return s


def dp(n, s, C, T):
    sumC = prefixSum(C)
    sumT = prefixSum(T)
    f = [float('inf')] * (n + 10)
    f[0] = 0
    for i in range(1, n + 1):
        for j in range(i):
            f[i] = min(f[i], f[j] + sumT[i] * (sumC[i] - sumC[j]) + s * (sumC[n] - sumC[j]))
    return f[n]


n = int(input())
s = int(input())
c, t = [], []
for _ in range(n):
    ti, ci = map(int, input().split())
    t.append(ti)
    c.append(ci)
print(dp(n, s, c, t))
