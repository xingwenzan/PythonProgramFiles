# 热浪 https://www.acwing.com/problem/content/1131/

t, c, start, end = map(int, input().split())
N, M = t + 10, c * 2 + 10
h, e, ne, w, idx = [-1] * N, [0] * M, [0] * M, [0] * M, 0
dist, st = [float('inf')] * N, [False] * N
dist[start] = 0


def add(a, b, c):
    global idx
    e[idx] = b
    w[idx] = c
    ne[idx] = h[a]
    h[a] = idx
    idx += 1
    return


def spfa():
    q = [0] * 25100
    hh, tt = 0, 1
    q[0] = start
    st[start] = True
    while hh < tt:
        fa = q[hh]
        st[fa] = False
        hh += 1

        i = h[fa]
        while i != -1:
            son = e[i]
            if dist[son] > dist[fa] + w[i]:
                dist[son] = dist[fa] + w[i]
                if not st[son]:
                    q[tt] = son
                    st[son] = True
                    tt += 1
            i = ne[i]
    return


for i in range(c):
    a, b, c = map(int, input().split())
    add(a, b, c)
    add(b, a, c)
spfa()
print(dist[end])
