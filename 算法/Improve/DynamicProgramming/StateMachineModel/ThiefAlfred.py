# 大盗阿福 https://www.acwing.com/problem/content/1051/

t = int(input())
for _ in range(t):
    n = int(input())
    lst = list(map(int, input().split()))
    f = [[0, 0] for _ in range(n + 10)]
    for i in range(1, n + 1):
        w = lst[i - 1]
        f[i][0] = max(f[i - 1][0], f[i - 1][1])
        f[i][1] = f[i - 1][0] + w
    print(max(f[n][0], f[n][1]))
