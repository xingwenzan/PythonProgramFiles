# 最长上升子序列 https://www.acwing.com/problem/content/897/

n = int(input())
lst = list(map(int, input().split()))
length = [1] * n
for i in range(n):
    for j in range(i):
        if lst[i] > lst[j]:
            length[i] = max(length[i], length[j] + 1)
ans = 0
for i in range(n):
    ans = max(ans, length[i])
print(ans)
