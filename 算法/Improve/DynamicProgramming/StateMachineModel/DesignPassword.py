# 设计密码 https://www.acwing.com/problem/content/1054/
# 状态机 + KMP
# python 写法不太好理解

import string

mod = int(1e9 + 7)
n = int(input())
s = input()
m = len(s)
ne = [0] * (m + 10)
f = [[0 for _ in range(m + 10)] for _ in range(n + 10)]

p = 0
for i in range(2, m + 1):
    while p and s[i - 1] != s[p]: p = ne[p]
    if s[i - 1] == s[p]: p += 1
    ne[i] = p

f[0][0] = 1

for i in range(1, n + 1):
    for j in range(m):
        for letter in string.ascii_lowercase:
            u = j
            while u and letter != s[u]: u = ne[u]
            if letter == s[u]: u += 1
            if u < m: f[i][u] = (f[i][u] + f[i - 1][j]) % mod

ans = 0
for i in range(m): ans = (ans + f[n][i]) % mod
print(ans)
