# 左孩子右兄弟 https://www.acwing.com/problem/content/3425/
# 不知道为啥不好使

N = 10 ** 5 + 10

head, value, nextPointer = [-1] * N, [0] * N, [0] * N
pointer = 1


def add(father, son):
    global pointer
    value[pointer] = son
    nextPointer[pointer] = head[father]
    head[father] = pointer
    pointer += 1


def dfs(headValue):
    currentPointer = head[headValue]
    maxHeight = 0
    sonNum = 0
    while currentPointer != -1:
        sonValue = value[currentPointer]
        maxHeight = max(maxHeight, dfs(sonValue))
        sonNum += 1
        currentPointer = nextPointer[currentPointer]
    return maxHeight + sonNum


n = int(input())
for i in range(2, n + 1, 1):
    father = int(input())
    add(father, i)

print(dfs(1))
