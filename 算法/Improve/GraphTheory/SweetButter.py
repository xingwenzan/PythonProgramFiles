# 香甜的黄油 https://www.acwing.com/problem/content/1129/


n, p, c = map(int, input().split())
N, M = p + 10, c * 2 + 10
cow = []
for i in range(n): cow.append(int(input()))
h, e, ne, w, idx = [-1] * N, [0] * M, [0] * M, [0] * M, 0


def add(a, b, distance):
    global idx
    w[idx] = distance
    e[idx] = b
    ne[idx] = h[a]
    h[a] = idx
    idx += 1
    return


def spfa(start):
    dist = [float('inf')] * N
    dist[start] = 0
    st = [False] * N
    st[start] = True
    q = [0] * (M * 2)
    hh, tt = 0, 1
    q[0] = start

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
                    st[son] = True
                    q[tt] = son
                    tt += 1

            i = ne[i]

    res = 0
    for j in cow:
        if dist[j] == float('inf'): return float('inf')
        res += dist[j]
    return res


for i in range(c):
    p1, p2, d = map(int, input().split())
    add(p1, p2, d)
    add(p2, p1, d)
ans = float('inf')
for i in range(1, p + 1):
    ans = min(ans, spfa(i))
print(ans)
