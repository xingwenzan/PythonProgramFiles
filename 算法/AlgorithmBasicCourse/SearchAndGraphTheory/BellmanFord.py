# 有边数限制的最短路 https://www.acwing.com/problem/content/855/
import copy

N, M = 510, 10 ** 4 + 10
inf = 10 ** 9
routes = [(0, 0, inf) for i in range(M)]
distance = [inf] * N


def bellmanFord(pointNum, routeNum, cycleNum):
    distance[1] = 0
    for i in range(cycleNum):
        tmp = copy.deepcopy(distance)
        for j in range(routeNum):
            start = routes[j][0]
            end = routes[j][1]
            lenght = routes[j][2]
            distance[end] = min(distance[end], tmp[start] + lenght)
    if distance[pointNum] > inf / 2: return 'impossible'
    return distance[pointNum]


pointNum, routeNum, cycleNum = map(int, input().split())
for i in range(routeNum):
    start, end, long = map(int, input().split())
    routes[i] = (start, end, long)

print(bellmanFord(pointNum, routeNum, cycleNum))
