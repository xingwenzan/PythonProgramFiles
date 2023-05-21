# 树与图的深度优先遍历 树的重心 https://www.acwing.com/problem/content/848/

N = 10 ** 5 + 10
M = N * 2
head, value, nextPointer = [-1] * N, [0] * M, [0] * M
pointer = 0
state = [False] * N
ans = N


def add(father, son):
    global pointer
    value[pointer] = son
    nextPointer[pointer] = head[father]
    head[father] = pointer
    pointer += 1


def dfs(fatherValue, allPointerNum):
    global ans
    state[fatherValue] = True
    maxConnectedBlockSize = 0
    allChildNum = 0
    sonPointer = head[fatherValue]
    while sonPointer != -1:
        sonValue = value[sonPointer]
        if not state[sonValue]:
            childNum = dfs(sonValue, allPointerNum)
            allChildNum += childNum
            maxConnectedBlockSize = max(maxConnectedBlockSize, childNum)
        sonPointer = nextPointer[sonPointer]
    maxConnectedBlockSize = max(maxConnectedBlockSize, allPointerNum - allChildNum - 1)
    ans = min(maxConnectedBlockSize, ans)

    return allChildNum + 1


n = int(input())
for i in range(n - 1):
    father, son = map(int, input().split())
    add(father, son)
    add(son, father)

dfs(1, n)
print(ans)
