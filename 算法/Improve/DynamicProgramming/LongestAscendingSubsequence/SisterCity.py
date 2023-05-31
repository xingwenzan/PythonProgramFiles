# 友好城市 https://www.acwing.com/problem/content/1014/

n = int(input())
lst = []
f = [1] * n
for _ in range(n):
    lst.append(list(map(int, input().split())))
lst.sort(key=lambda x: x[0])
ans = 0
for i in range(n):
    for j in range(i):
        if lst[i][1] > lst[j][1]:
            f[i] = max(f[i], f[j] + 1)
    ans = max(ans, f[i])
print(ans)
