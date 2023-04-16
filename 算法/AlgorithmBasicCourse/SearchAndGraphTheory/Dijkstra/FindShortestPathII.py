# Dijkstra求最短路 II https://www.acwing.com/problem/content/852/
# 堆优化版

import heapq

N = 2 * (10 ** 5) + 10
inf = 10 ** 9 + 10
head, value, nextPointer, weight, pointer = [-1] * N, [0] * N, [0] * N, [inf] * N, 0
distance = [inf] * N
state = [False] * N
heap = []


def add(father, son, length):
    global pointer
    value[pointer] = son
    weight[pointer] = length
    nextPointer[pointer] = head[father]
    head[father] = pointer
    pointer += 1


def dijkstra(num):
    distance[1] = 0
    heapq.heappush(heap, (distance[1], 1))
    while len(heap) > 0:
        lenght, fatherValue = heapq.heappop(heap)
        if not state[fatherValue]:
            state[fatherValue] = True
            nextSonPointer = head[fatherValue]
            while nextSonPointer != -1:
                sonValue = value[nextSonPointer]
                if distance[sonValue] > distance[fatherValue] + weight[nextSonPointer]:
                    distance[sonValue] = distance[fatherValue] + weight[nextSonPointer]
                    heapq.heappush(heap, (distance[sonValue], sonValue))
                nextSonPointer = nextPointer[nextSonPointer]
    if distance[num] > 10 ** 9: return -1
    return distance[num]


n, m = map(int, input().split())
for i in range(m):
    start, end, long = map(int, input().split())
    add(start, end, long)
print(dijkstra(n))
