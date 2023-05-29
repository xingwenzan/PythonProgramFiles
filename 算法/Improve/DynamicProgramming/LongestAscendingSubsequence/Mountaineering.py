# 登山 https://www.acwing.com/problem/content/1016/

n = int(input())
lst = list(map(int, input().split()))
up, down = [1] * n, [1] * n

for i in range(n):
    for j in range(i):
        if lst[i] > lst[j]:
            up[i] = max(up[i], up[j] + 1)
for i in range(n - 1, -1, -1):
    for j in range(n - 1, i, -1):
        if lst[i] > lst[j]:
            down[i] = max(down[i], down[j] + 1)
ans = 0
for i in range(n): ans = max(ans, up[i] + down[i] - 1)
print(ans)
