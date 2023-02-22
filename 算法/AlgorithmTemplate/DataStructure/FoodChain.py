# 食物链 https://www.acwing.com/problem/content/242/

dataRange = 10 ** 5 + 10
fatherNode = [i for i in range(dataRange)]
childrenToRootDistance = [0] * dataRange


def quickForefatherNode(x):
    if fatherNode[x] != x:
        tmp = quickForefatherNode(fatherNode[x])
        childrenToRootDistance[x] += childrenToRootDistance[fatherNode[x]]
        fatherNode[x] = tmp
    return fatherNode[x]


N, K = map(int, input().split())
wrong = 0
for i in range(K):
    mode, X, Y = map(int, input().split())
    forefatherX = quickForefatherNode(X)
    forefatherY = quickForefatherNode(Y)
    if X > N or Y > N:
        wrong += 1
    elif mode == 1:
        if forefatherX == forefatherY and ((childrenToRootDistance[X] - childrenToRootDistance[Y]) % 3 != 0):
            wrong += 1
        elif forefatherX != forefatherY:
            fatherNode[forefatherX] = forefatherY
            childrenToRootDistance[forefatherX] = childrenToRootDistance[Y] - childrenToRootDistance[X]
    else:
        if forefatherX == forefatherY and ((childrenToRootDistance[X] - childrenToRootDistance[Y] - 1) % 3 != 0):
            wrong += 1
        elif forefatherX != forefatherY:
            fatherNode[forefatherX] = forefatherY
            childrenToRootDistance[forefatherX] = childrenToRootDistance[Y] + 1 - childrenToRootDistance[X]
print(wrong)
