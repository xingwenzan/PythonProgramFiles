# 货币系统 https://www.acwing.com/problem/content/534/

t = int(input())
for i in range(t):
    n = int(input())
    lst = list(map(int, input().split()))
    lst.sort()
    f = [False] * 25010
    f[0] = True
    ans = 0
    for j in lst:
        if not f[j]: ans += 1
        for k in range(j, lst[-1] + 1, 1):
            f[k] |= f[k - j]
    print(ans)
