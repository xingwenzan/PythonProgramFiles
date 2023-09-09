# 修剪草坪 https://www.acwing.com/problem/content/1089/
# 单调递减队列，q[hh] 对应的就是最大值

def prefixSum(lst):
    s = [0]
    for i in range(len(lst)):
        s.append(s[i] + lst[i])
    return s


def dp(lst, length):
    def g(x):
        if x == 0: return 0
        return f[x - 1] - s[x]

    s = prefixSum(lst)
    N = len(s)
    f = [0] * N
    q = [0] * N
    hh = tt = 0
    for i in range(1, N):
        if q[hh] < i - length: hh += 1
        f[i] = max(f[i - 1], g(q[hh]) + s[i])
        while hh <= tt and g(q[tt]) <= g(i): tt -= 1
        tt += 1
        q[tt] = i
    return f[N - 1]


n, k = map(int, input().split())
lst = []
for _ in range(n):
    lst.append(int(input()))
print(dp(lst, k))
