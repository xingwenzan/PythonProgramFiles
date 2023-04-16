# Dijkstra求最短路 I https://www.acwing.com/problem/content/851/
# 朴素方法

N = 510
inf = 10 ** 4 + 10
adjacencyMatrix = [[inf for i in range(N)] for i in range(N)]
distance = [inf for i in range(N)]
state = [False] * N


def dijkstra(num):
    distance[1] = 0
    for i in range(1, num):
        start = -1
        for j in range(1, num + 1):
            if (state[j] == False) and (start == -1 or distance[start] > distance[j]):
                start = j
        state[start] = True
        for end in range(1, num + 1):
            distance[end] = min(distance[end], distance[start] + adjacencyMatrix[start][end])
    if distance[num] > 10 ** 4: return -1
    return distance[num]


n, m = map(int, input().split())
for i in range(m):
    start, end, long = map(int, input().split())
    adjacencyMatrix[start][end] = min(adjacencyMatrix[start][end], long)
print(dijkstra(n))
