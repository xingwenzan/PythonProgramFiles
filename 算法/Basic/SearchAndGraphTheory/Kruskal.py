# Kruskal算法求最小生成树 https://www.acwing.com/problem/content/861/

N = 10 ** 5 + 10
inf = 1e9 + 10
fatherNode = [i for i in range(N)]
edge = []


def find(x):
    if fatherNode[x] != x: fatherNode[x] = find(fatherNode[x])
    return fatherNode[x]


def kruskal(num):
    tmp = sorted(edge)
    ans, cnt = 0, 0
    for i in range(len(tmp)):
        a = tmp[i][1]
        b = tmp[i][2]
        weight = tmp[i][0]
        aFather = find(a)
        bFather = find(b)
        if aFather != bFather:
            fatherNode[aFather] = bFather
            ans += weight
            cnt += 1
    if cnt < num - 1:
        return inf
    else:
        return ans


n, m = map(int, input().split())
for i in range(m):
    a, b, weight = map(int, input().split())
    edge.append((weight, a, b))

out = kruskal(n)
if out == inf:
    print("impossible")
else:
    print(out)
