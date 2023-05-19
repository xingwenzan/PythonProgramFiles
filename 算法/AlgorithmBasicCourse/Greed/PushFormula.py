# 耍杂技的牛 https://www.acwing.com/problem/content/127/
# https://www.acwing.com/video/122/

lst = []
n = int(input())
for i in range(n):
    lst.append(list(map(int, input().split())))
lst.sort(key=lambda x: x[0] + x[1])
ans = -lst[0][1]
for i in range(1, n):
    lst[i][0] += lst[i - 1][0]
    ans = max(ans, lst[i - 1][0] - lst[i][1])
print(ans)
