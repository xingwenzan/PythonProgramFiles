# spfa判断负环 https://www.acwing.com/problem/content/854/

from queue import Queue

N = 2010
M = 10**4 + 10
inf = 10 ** 9 + 10
head, value, nextPointer, weight, pointer = [-1] * N, [0] * M, [0] * M, [inf] * M, 0
distance, sizeNum = [0] * N, [0] * N
state = [False] * N  # 在不在队列里
pendingPointer = Queue(maxsize=0) # 会超时，自己手写比较好


def add(father, son, length):
    global pointer
    value[pointer] = son
    weight[pointer] = length
    nextPointer[pointer] = head[father]
    head[father] = pointer
    pointer += 1


def spfa(num):
    for i in range(1, num + 1):
        pendingPointer.put(i)
        state[i] = True
    while not pendingPointer.empty():
        fatherValue = pendingPointer.get()
        state[fatherValue] = False
        nextSonPointer = head[fatherValue]
        while nextSonPointer != -1:
            sonValue = value[nextSonPointer]
            if distance[sonValue] > distance[fatherValue] + weight[nextSonPointer]:
                distance[sonValue] = distance[fatherValue] + weight[nextSonPointer]
                sizeNum[sonValue] = sizeNum[fatherValue] + 1

                if sizeNum[sonValue] >= num: return True
                if not state[sonValue]:
                    pendingPointer.put(sonValue)
                    state[sonValue] = True
            nextSonPointer = nextPointer[nextSonPointer]
    return False


n, m = map(int, input().split())
for i in range(m):
    start, end, long = map(int, input().split())
    add(start, end, long)
if spfa(n):
    print("Yes")
else:
    print("No")
