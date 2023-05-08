# 没有上司的舞会 https://www.acwing.com/problem/content/287/

import sys

sys.setrecursionlimit(1000000)  # 设置递归深度，因为 python 递归深度有限，大概 900 多

N = 6010
head, value, pointer, idx = [-1] * N, [0] * N, [0] * N, 0
happy = [0] * N
f = [[0, 0] for _ in range(N)]
hasFather = [False] * N


def add(son, father):
    global idx
    value[idx] = son
    pointer[idx] = head[father]
    head[father] = idx
    idx += 1


def dfs(root):
    f[root][1] = happy[root]
    nextPointer = head[root]
    while nextPointer != -1:
        nextValue = value[nextPointer]
        dfs(nextValue)
        f[root][0] += max(f[nextValue][0], f[nextValue][1])
        f[root][1] += f[nextValue][0]
        nextPointer = pointer[nextPointer]


n = int(input())
for i in range(1, n + 1):
    happy[i] = int(input())
for i in range(n - 1):
    son, father = map(int, input().split())
    add(son, father)
    hasFather[son] = True
root = 1
while hasFather[root]:
    root += 1
dfs(root)
print(max(f[root][0], f[root][1]))
