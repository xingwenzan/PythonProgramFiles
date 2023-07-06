# 金明的预算方案 https://www.acwing.com/problem/content/489/

n, m = map(int, input().split())
master, servent = [0 for _ in range(m + 1)], [[] for _ in range(m + 1)]
for i in range(1, m + 1):
    v, p, q = map(int, input().split())
    if q == 0:
        master[i] = [v, v * p]
    else:
        servent[q].append([v, v * p])

f = [0 for _ in range(n + 1)]
for i in range(1, m + 1):
    if master[i] == 0:
        continue

    for j in range(n, -1, -1):
        # 二进制枚举所有情况
        for k in range(1 << len(servent[i])):
            v, w = master[i][0], master[i][1]
            for u in range(len(servent[i])):
                if k >> u & 1:
                    v += servent[i][u][0]
                    w += servent[i][u][1]
            if j >= v:
                f[j] = max(f[j], f[j - v] + w)
print(f[n])
