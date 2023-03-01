# 最大异或对 https://www.acwing.com/problem/content/145/

M = 31 * (10 ** 5 + 10)
sonNode = [[0] * 2 for i in range(M)]
nodePointer = 0


def insert(num):
    global nodePointer
    rowPoiner = 0
    for i in range(30, -1, -1):
        colPointer = num >> i & 1
        if sonNode[rowPoiner][colPointer] == 0:
            nodePointer += 1
            sonNode[rowPoiner][colPointer] = nodePointer
        rowPoiner = sonNode[rowPoiner][colPointer]


def queryMaximumXorPair(num):
    ans = 0
    rowPoiner = 0
    for i in range(30, -1, -1):
        colPointer = num >> i & 1
        if sonNode[rowPoiner][1 ^ colPointer] != 0:
            ans += (1 << i)
            rowPoiner = sonNode[rowPoiner][1 ^ colPointer]
        else:
            rowPoiner = sonNode[rowPoiner][colPointer]
    return ans


N = int(input())
lst = list(map(int, input().split()))
for i in range(N):
    insert(lst[i])

out = 0
for i in range(N):
    out = max(out, queryMaximumXorPair(lst[i]))
print(out)
