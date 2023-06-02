# 最大上升子序列和 https://www.acwing.com/problem/content/1018/

n = int(input())
lst = list(map(int, input().split()))
f = lst.copy()
ans = 0
for i in range(n):
    for j in range(i):
        if lst[i] > lst[j]:
            f[i] = max(f[i], f[j] + lst[i])
    ans = max(ans, f[i])
print(ans)
