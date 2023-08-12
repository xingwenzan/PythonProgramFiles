# 愤怒的小鸟 https://www.acwing.com/problem/content/526/
# 视频 https://www.acwing.com/video/405/

N, M = 18, 1 << 18
eps = 1e-8


# 浮点数比较
def cmp(x, y):
    if abs(x - y) < eps: return 0
    if x > y: return 1
    return -1


T = int(input())
for _ in range(T):
    n, m = map(int, input().split())
    pigs = [tuple(map(float, input().split())) for i in range(n)]  # 储存小猪
    # 如果只有一只猪，直接输出
    # 必须在读完小猪位置后，不然影响接下来的循环
    if n == 1:
        print(1)
        continue
    # 储存抛物线/经过小猪的覆盖状态，path[i，j] 为该抛物线经过 i、j 号小猪时的状态，1 为此位上对应的小猪被抛物线经过
    path = [[0 for i in range(N)] for i in range(N)]
    # 预处理，求经过任两只猪（i、j）的抛物线和对应的状态
    for i in range(n):
        path[i][i] = 1 << i
        for j in range(n):
            x1, y1 = pigs[i]
            x2, y2 = pigs[j]
            if cmp(x1, x2) == 0: continue  # 两点在一排，无抛物线
            a = (y1 / x1 - y2 / x2) / (x1 - x2)
            b = y1 / x1 - a * x1
            if cmp(a, 0) >= 0: continue  # a<0，才能继续进行
            state = 0  # 存 path[i,j] 的状态/经过的小猪
            for k in range(n):
                x, y = pigs[k]
                if cmp(y, a * x * x + b * x) == 0: state += (1 << k)
            path[i][j] = state
    # DP
    f = [float('inf')] * M  # f[x] 状态 x 时（覆盖了哪些猪，没覆盖哪些）所需的最小抛物线数
    f[0] = 0
    for i in range((1 << n) - 1):  # 遍历所有未覆盖全部小猪的状态
        x = 0
        for j in range(n):  # 取出任意未覆盖的位
            if (i >> j) & 1 == 0:
                x = j
                break
        for j in range(n):
            f[i | path[x][j]] = min(f[i | path[x][j]], f[i] + 1)
    print(f[(1 << n) - 1])
