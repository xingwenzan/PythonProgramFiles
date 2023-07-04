# 能量石 https://www.acwing.com/problem/content/736/

T = int(input())
for t in range(T):
    Stones = []
    N = int(input())
    M = 0
    for _ in range(N):
        tmp = list(map(int, input().split()))
        Stones.append(tmp)
        M += tmp[0]
    Stones.sort(key=lambda x: x[0] / (x[2] + 1e-10))
    f = [0 for _ in range(M + 10)]
    for s, e, l in Stones:
        for j in range(M, s - 1, -1):
            # 下面两方式效果相同
            f[j] = max(f[j], f[j - s] + max(e - (j - s) * l, 0))
            # f[j] = max(f[j], f[j - s] + e - (j - s) * l)
    print(f"Case #{t + 1}: {max(f)}")
