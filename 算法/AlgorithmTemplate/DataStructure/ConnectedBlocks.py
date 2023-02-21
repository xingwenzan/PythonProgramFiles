# 连通块中点的数量 https://www.acwing.com/problem/content/839/

N = 10 ** 5 + 10
fatherNode = [i for i in range(N)]
childrenNodeNum = [1] * N


def quickForefatherNode(x):
    if fatherNode[x] != x: fatherNode[x] = quickForefatherNode(fatherNode[x])
    return fatherNode[x]


n, m = map(int, input().split())
for i in range(m):
    lst = input().split()
    if lst[0] == "C":
        forefatherA = quickForefatherNode(int(lst[1]))
        forefatherB = quickForefatherNode(int(lst[2]))
        if forefatherB != forefatherA:
            fatherNode[forefatherA] = fatherNode[forefatherB]
            childrenNodeNum[forefatherB] += childrenNodeNum[forefatherA]
    elif lst[0] == "Q1":
        forefatherA = quickForefatherNode(int(lst[1]))
        forefatherB = quickForefatherNode(int(lst[2]))
        if forefatherB == forefatherA:
            print("Yes")
        else:
            print("No")
    else:
        forefather = quickForefatherNode(int(lst[1]))
        print(childrenNodeNum[forefather])
