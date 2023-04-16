# 树与图的广度优先遍历 图中点的层次 https://www.acwing.com/problem/content/849/

from queue import Queue

N = 10 ** 5 + 10
head, value, nextPointer = [-1] * N, [0] * N, [0] * N
pointer = 0
distance = [-1] * N
pendingPointer = Queue(maxsize=0)


def add(father, son):
    global pointer
    value[pointer] = son
    nextPointer[pointer] = head[father]
    head[father] = pointer
    pointer += 1


def bfs(start, end):
    pendingPointer.put(start)
    distance[start] = 0
    while not pendingPointer.empty():
        currentFatherValue = pendingPointer.get()
        nextSonPointer = head[currentFatherValue]
        # if currentFatherValue == end: return distance[currentFatherValue] # 可有可无
        while nextSonPointer != -1:
            sonValue = value[nextSonPointer]
            if distance[sonValue] == -1:
                distance[sonValue] = distance[currentFatherValue] + 1
                pendingPointer.put(sonValue)
            nextSonPointer = nextPointer[nextSonPointer]
    return distance[end]


n, m = map(int, input().split())
for i in range(m):
    father, son = map(int, input().split())
    add(father, son)
print(bfs(1, n))
