# 抓住那头牛 https://www.acwing.com/problem/content/1102/

N = int(1e5 + 10)
dis = [-1] * N

n, k = map(int, input().split())


def bfs():
    q = [-1] * N
    q[0] = n
    hh = tt = 0

    dis[n] = 0
    while hh <= tt:
        tmp = q[hh]
        hh += 1
        for i in [tmp + 1, tmp - 1, tmp * 2]:
            if i < 0 or i > 1e5: continue
            if dis[i] != -1: continue
            if i == k: return dis[tmp] + 1

            dis[i] = dis[tmp] + 1

            tt += 1
            q[tt] = i


if n == k:
    print(0)
else:
    print(bfs())
