# 采药 https://www.acwing.com/activity/content/problem/content/1267/

f = [0] * 1010
t, m = map(int, input().split())
for i in range(m):
    v, w = map(int, input().split())
    for j in range(t, v - 1, -1):
        f[j] = max(f[j], f[j - v] + w)
print(f[t])
