# 最高的牛 https://www.acwing.com/problem/content/103/

n, p, h, m = map(int, input().split())
lst = [0] * (n + 1)
s = []
for _ in range(m):
    a, b = map(int, input().split())
    if a > b:
        a, b = b, a
    elif a == b:
        continue
    if (a, b) not in set(s):
        s.append((a, b))
        lst[a + 1] -= 1
        lst[b] += 1
'''
# 用 p
cow = [0] * (n + 1)
cow[p] = h
for i in range(p + 1, n + 1):
    cow[i] = cow[i - 1] + lst[i]
for i in range(p - 1, 0, -1):
    cow[i] = cow[i + 1] - lst[i + 1]
for i in range(1, n + 1):
    print(cow[i])
'''
# 不用 p
lst[1] += h
for i in range(1, n + 1):
    lst[i] += lst[i - 1]
    print(lst[i])
