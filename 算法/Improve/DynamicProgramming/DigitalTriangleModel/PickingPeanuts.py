# 摘花生 https://www.acwing.com/problem/content/1017/

T = 110
f = [[0 for _ in range(T)] for _ in range(T)]

n = int(input())
for _ in range(n):
    w = []
    R, C = map(int, input().split())
    for r in range(R):
        w.append(list(map(int, input().split())))
    for r in range(1, R + 1):
        for c in range(1, C + 1):
            f[r][c] = max(f[r - 1][c], f[r][c - 1]) + w[r - 1][c - 1]
    print(f[R][C])
