# 有向图的拓扑序列 https://www.acwing.com/problem/content/850/
# 有向图才有拓扑序列
# 入度：多少点指向它；出度：它指向多少点

N = 10 ** 5 + 10
head, value, nextPointer, pointer = [-1] * N, [0] * N, [0] * N, 0
socre = [0] * N  # 入度
queue, headPointer, tailPointer = [0] * N, 0, -1


def add(father, son):
    global pointer
    value[pointer] = son
    nextPointer[pointer] = head[father]
    head[father] = pointer
    pointer += 1
    socre[son] += 1


def topologicalSort(input):
    global headPointer, tailPointer
    for i in range(1, input + 1):
        if socre[i] == 0:
            tailPointer += 1
            queue[tailPointer] = i
    while headPointer <= tailPointer:
        fatherValue = queue[headPointer]
        headPointer += 1
        nextSonPointer = head[fatherValue]
        while nextSonPointer != -1:
            sonValue = value[nextSonPointer]
            socre[sonValue] -= 1
            if socre[sonValue] == 0:
                tailPointer += 1
                queue[tailPointer] = sonValue
            nextSonPointer = nextPointer[nextSonPointer]
    return tailPointer == input - 1


n, m = map(int, input().split())
for i in range(m):
    father, son = map(int, input().split())
    add(father, son)

if topologicalSort(n):
    # print(" ".join(map(str, queue)))
    for i in range(n):
        print(queue[i], end=" ")
else:
    print(-1)
