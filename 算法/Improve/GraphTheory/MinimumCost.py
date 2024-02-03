# 最小花费 https://www.acwing.com/problem/content/1128/

def dijkstra(graph, start, end):
    dist = [0.0] * (n + 10)
    st = [False] * (n + 10)
    dist[start] = 1
    for i in range(1, n + 1):
        tmp = -1
        for j in range(1, n + 1):
            if (not st[j]) and (tmp == -1 or dist[tmp] < dist[j]): tmp = j
        st[tmp] = True
        for j in range(1, n + 1):
            dist[j] = max(dist[tmp] * graph[tmp][j], dist[j])
    return dist[end]


n, m = map(int, input().split())
g = [[float(0)] * (n + 10) for _ in range(n + 10)]
for i in range(m):
    a, b, c = map(int, input().split())
    g[a][b] = g[b][a] = max(g[a][b], (100 - c) / 100)
s, t = map(int, input().split())
print("{:.8f}".format(100.0 / dijkstra(g, s, t)))
