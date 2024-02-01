# 雷达设备 https://www.acwing.com/problem/content/114/
# 解析 https://www.acwing.com/solution/content/1061/

eps = 1e-6
n, d = map(int, input().split())
lst = []
ans = 0
for i in range(n):
    x, y = map(int, input().split())
    if y > d:
        ans = -1
        break
    else:
        tmp = (d * d - y * y) ** 0.5
        lst.append([x + tmp, x - tmp])

if ans != -1:
    lst = sorted(lst)
    last = -float('inf')
    for i in range(n):
        if lst[i][1] > last + eps:
            ans += 1
            last = lst[i][0]
print(ans)
