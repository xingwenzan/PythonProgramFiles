# 染色法判定二分图 https://www.acwing.com/problem/content/862/
from queue import Queue

N = 10 ** 5 + 10
head, value, nextPointer = [-1] * N, [0] * (N * 2), [0] * (N * 2)
pointer = 0
color = [0] * N


def add(start, end):
    global pointer
    value[pointer] = end
    nextPointer[pointer] = head[start]
    head[start] = pointer
    pointer += 1


def dfs(father, colour): # 爆栈
    color[father] = colour
    nextSonPointer = head[father]
    while nextSonPointer != -1:
        sonValue = value[nextSonPointer]
        if color[sonValue] == 0:
            if not dfs(sonValue, -colour):
                return False
        elif color[sonValue] == colour:
            return False
        nextSonPointer = nextPointer[nextSonPointer]
    return True


def bfs(father, colour): # TLE
    queue = Queue(maxsize=0)
    queue.put((father, colour))
    while not queue.empty():
        node, nodeColour = queue.get()
        nextNode = head[node]
        color[node] = nodeColour
        while nextNode != -1:
            nextValue = value[nextNode]
            if color[nextValue] == 0:
                queue.put((nextValue, -nodeColour))
            elif color[nextValue] == nodeColour:
                return False
            nextNode = nextPointer[nextNode]
    return True


n, m = map(int, input().split())
for i in range(m):
    a, b = map(int, input().split())
    add(a, b)
    add(b, a)

ans = "Yes"
for i in range(1, n + 1):
    if color[i] == 0:
        # if not dfs(i, 1):
        if not bfs(i, 1):
            ans = "No"
            break
print(ans)
