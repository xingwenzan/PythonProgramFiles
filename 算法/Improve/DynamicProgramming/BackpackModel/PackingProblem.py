# 装箱问题 https://www.acwing.com/problem/content/1026/

V = int(input())
n = int(input())
f = [V] * (V + 1)
ans = V
for i in range(n):
    v = int(input())
    for j in range(V, v - 1, -1):
        f[j] = min(f[j], f[j - v] - v)
    ans = min(ans, f[V])

print(ans)
