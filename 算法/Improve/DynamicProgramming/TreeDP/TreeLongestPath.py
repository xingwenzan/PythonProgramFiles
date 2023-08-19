# 树的最长路径 https://www.acwing.com/problem/content/1074/
# 解析 https://blog.csdn.net/weixin_72060925/article/details/128791893

N = int(1e4 + 10)
h, e, ne, idx = [-1] * N, [0] * (2 * N), [0] * (2 * N), 0
w = [0] * (2 * N)
ans = 0


def add1(father, son, length):
    global idx
    w[idx] = length
    e[idx] = son
    ne[idx] = h[father]
    h[father] = idx
    idx += 1
    return


def add2(p1, p2, length):
    add1(p1, p2, length)
    add1(p2, p1, length)
    return


def dfs(u, father):
    global ans
    dist = 0  # 表示从当前点往下走的最大长度
    d1, d2 = 0, 0  # 最大长度和次大长度
    i = h[u]
    while i != -1:
        son = e[i]
        if son != father:
            d = dfs(son, u) + w[i]
            dist = max(dist, d)
            if d >= d1:
                d2, d1 = d1, d
            elif d > d2:
                d2 = d
        i = ne[i]
    ans = max(ans, d1 + d2)
    return dist


n = int(input())
for _ in range(n - 1):
    a, b, c = map(int, input().split())
    add2(a, b, c)
dfs(1, -1)
print(ans)
