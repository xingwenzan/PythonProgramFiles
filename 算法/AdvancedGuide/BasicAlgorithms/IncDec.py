# 增减序列 https://www.acwing.com/problem/content/102/

n = int(input())
lst = [0]
for _ in range(n):
    lst.append(int(input()))
for i in range(n, 0, -1):
    lst[i] -= lst[i - 1]
inc, dec = 0, 0
for i in range(2, n + 1):
    if lst[i] > 0:
        inc += lst[i]
    else:
        dec -= lst[i]
print(max(inc, dec))  # min(inc, dec) + abs(inc - dec)
print(abs(inc - dec) + 1)
