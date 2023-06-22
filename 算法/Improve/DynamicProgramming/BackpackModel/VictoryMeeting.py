# 庆功会 https://www.acwing.com/problem/content/1021/

f = [0] * 6010

n, m = map(int, input().split())
for _ in range(n):
    v, w, s = map(int, input().split())
    for i in range(m, -1, -1):
        j = 0
        while j <= s and j * v <= i:
            f[i] = max(f[i], f[i - j * v] + j * w)
            j += 1
print(f[m])
