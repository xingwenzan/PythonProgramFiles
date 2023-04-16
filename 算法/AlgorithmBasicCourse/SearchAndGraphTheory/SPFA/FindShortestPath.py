# spfa求最短路 https://www.acwing.com/problem/content/853/

from queue import Queue

N = 10 ** 5 + 10
inf = 10 ** 9 + 10
head, value, nextPointer, weight, pointer = [-1] * N, [0] * N, [0] * N, [inf] * N, 0
distance = [inf] * N
state = [False] * N  # 在不在队列里
pendingPointer = Queue(maxsize=0)


def add(father, son, length):
    global pointer
    value[pointer] = son
    weight[pointer] = length
    nextPointer[pointer] = head[father]
    head[father] = pointer
    pointer += 1


def spfa(start, end):
    pendingPointer.put(start)
    distance[start] = 0
    state[start] = True
    while not pendingPointer.empty():
        fatherValue = pendingPointer.get()
        state[fatherValue] = False
        nextSonPointer = head[fatherValue]
        while nextSonPointer != -1:
            sonValue = value[nextSonPointer]
            if distance[sonValue] > distance[fatherValue] + weight[nextSonPointer]:
                distance[sonValue] = distance[fatherValue] + weight[nextSonPointer]
                if not state[sonValue]:
                    pendingPointer.put(sonValue)
                    state[sonValue] = True
            nextSonPointer = nextPointer[nextSonPointer]
    if distance[end] > 10 ** 9: return 'impossible'
    return distance[end]


n, m = map(int, input().split())
for i in range(m):
    start, end, long = map(int, input().split())
    add(start, end, long)
print(spfa(1, n))
