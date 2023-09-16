# 理想的正方形 https://www.acwing.com/problem/content/1093/

N = 1010
ans = float('inf')


def get_max(lst, length, window):
    q = [0] * N
    hh, tt = 0, -1
    ans = []
    for i in range(length):
        if hh <= tt and q[hh] <= i - window: hh += 1
        while hh <= tt and lst[q[tt]] <= lst[i]: tt -= 1
        tt += 1
        q[tt] = i
        ans.append(lst[q[hh]])
    return ans


def get_min(lst, length, window):
    q = [0] * N
    hh, tt = 0, -1
    ans = []
    for i in range(length):
        if hh <= tt and q[hh] <= i - window: hh += 1
        while hh <= tt and lst[q[tt]] >= lst[i]: tt -= 1
        tt += 1
        q[tt] = i
        ans.append(lst[q[hh]])
    return ans


n, m, k = map(int, input().split())
w = []
for _ in range(n):
    w.append(list(map(int, input().split())))
w_max, w_min = [], []
for i in range(n):
    w_max.append(get_max(w[i], m, k))
    w_min.append(get_min(w[i], m, k))
for i in range(k - 1, m):
    a = []
    for j in range(n): a.append(w_max[j][i])
    b = get_max(a, n, k)
    a = []
    for j in range(n): a.append(w_min[j][i])
    c = get_min(a, n, k)
    for j in range(k - 1, n): ans = min(ans, b[j] - c[j])
print(ans)
