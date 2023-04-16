# Prim算法求最小生成树 https://www.acwing.com/problem/content/860/

N, inf = 510, 1e9 + 10
adjacencyMatrix = [[inf for i in range(N)] for i in range(N)]
distance, state = [inf] * N, [False] * N


def add(start, end, length):
    adjacencyMatrix[start][end] = adjacencyMatrix[end][start] = min(adjacencyMatrix[start][end], length)


def prim(num):
    distance[1] = 0
    ans = 0
    for i in range(num):
        start = -1
        for j in range(1, num + 1):
            if (not state[j]) and (start == -1 or distance[start] > distance[j]):
                start = j
        if distance[start] == inf: return inf
        ans += distance[start]
        state[start] = True
        for end in range(1, num + 1):
            distance[end] = min(distance[end], adjacencyMatrix[start][end])
    return ans


n, m = map(int, input().split())
for i in range(m):
    start, end, length = map(int, input().split())
    add(start, end, length)

out = prim(n)
if out == inf:
    print("impossible")
else:
    print(out)
