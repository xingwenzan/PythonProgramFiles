# 烽火传递 https://www.acwing.com/problem/content/1091/

n, m = map(int, input().split())
lst = [0]
lst.extend(list(map(int, input().split())))
f = [0] * (n + 10)
q = [0] * (n + 10)
hh = tt = 0
for i in range(1, n + 1):
    if q[hh] < i - m: hh += 1
    f[i] = f[q[hh]] + lst[i]
    while hh <= tt and f[q[tt]] >= f[i]: tt -= 1
    tt += 1
    q[tt] = i
ans = float('inf')
for i in range(n, n - m, -1): ans = min(ans, f[i])
print(ans)
