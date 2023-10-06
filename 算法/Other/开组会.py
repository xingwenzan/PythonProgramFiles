# https://ac.nowcoder.com/acm/contest/66651/B

N = int(5e5 + 10)
h, e, ne, idx = [-1] * N, [0] * N, [0] * N, 0
f = []
cnt = 0


def add(father, son):
    global idx
    e[idx] = son
    ne[idx] = h[father]
    h[father] = idx
    idx += 1
    return


n = int(input())
f.append([0] + list(map(int, input().split())))


def dfs(u):
    d = 0
    i = h[u]
    while i != -1:
        s = e[i]
        d = max(d, dfs(s))
        i = ne[i]
    return d + 1


def init(d):
    while d > len(f):
        f.append([0] * (n + 1))
        for father in range(1, n + 1):
            i = h[father]
            f[-1][father] = f[-2][father]
            while i != -1:
                son = e[i]
                f[-1][father] = max(f[-1][father], f[-2][son])
                i = ne[i]
    return


for _ in range(n - 1):
    a, b = map(int, input().split())
    add(a, b)
deep = dfs(1)
# print(deep)
init(deep)

m = int(input())
for _ in range(m):
    a, b = map(int, input().split())
    if a >= deep:
        print(f[-1][b])
    else:
        print(f[a][b])
