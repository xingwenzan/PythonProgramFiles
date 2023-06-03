# 拦截导弹 https://www.acwing.com/problem/content/1012/

lst = list(map(int, input().split()))
n = len(lst)
f, g = [1] * n, [1e9] * n  # f 最长上升子序列   q 贪心 各子序列最小的值
lis, cnt = 0, 0  # lis 最长上升子序列长度   cnt 贪心 最小子序列数

for i in range(n):
    for j in range(i):
        if lst[i] <= lst[j]:
            f[i] = max(f[i], f[j] + 1)
    lis = max(lis, f[i])

    tmp = 0
    while tmp < cnt and lst[i] > g[tmp]: tmp += 1
    if tmp == cnt:
        g[cnt] = lst[i]
        cnt += 1
    else:
        g[tmp] = lst[i]

print(lis)
print(cnt)
