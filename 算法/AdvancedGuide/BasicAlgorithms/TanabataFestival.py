# 七夕祭 https://www.acwing.com/problem/content/description/107/
# 详解 https://www.acwing.com/video/783/

def work(n, lst):
    ans = 0
    s = [0] * (n + 1)
    for i in range(1, n + 1): s[i] = s[i - 1] + lst[i - 1]
    if s[n] % n: return -1

    a = s[n] // n
    del s[n]
    for i in range(n): s[i] -= a * i
    s.sort()
    a = s[n // 2]
    for i in range(n): ans += abs(a - s[i])
    return ans


n, m, t = map(int, input().split())
row, col = [0] * n, [0] * m
for i in range(t):
    a, b = map(int, input().split())
    row[a - 1] += 1
    col[b - 1] += 1
r, c = work(n, row), work(m, col)
if r != -1 and c != -1:
    print("both {}".format(r + c))
elif r != -1:
    print("row {}".format(r))
elif c != -1:
    print("column {}".format(c))
else:
    print("impossible")
