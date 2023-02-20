# 合并集合 https://www.acwing.com/problem/content/838/

N = 10 ** 5 + 10
fatherNode = [i for i in range(N)]


def quickForeatherNode(x):
    if fatherNode[x] != x: fatherNode[x] = quickForeatherNode(fatherNode[x])
    return fatherNode[x]


n, m = map(int, input().split())
for i in range(m):
    lst = input().split()
    if lst[0] == "M":
        fatherNode[quickForeatherNode(int(lst[1]))] = quickForeatherNode(int(lst[2]))
    else:
        if quickForeatherNode(int(lst[1])) == quickForeatherNode(int(lst[2])):
            print("Yes")
        else:
            print("No")
