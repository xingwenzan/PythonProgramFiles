# Trie字符串统计 https://www.acwing.com/problem/content/837/

N = 10 ** 5 + 10  # 代表所有输入的字符串总长度，极限情况为所有输入字符串每个位置的字母都不一样，即代表树的节点总数
sonNode = [[0] * 26 for i in range(N)]
nodeNum = [0] * N
nodePointer = 0


def insert(str):
    global nodePointer
    rowPoiner = 0
    for i in range(len(str)):
        colPointer = ord(str[i]) - ord("a")
        if sonNode[rowPoiner][colPointer] == 0:
            nodePointer += 1
            sonNode[rowPoiner][colPointer] = nodePointer
        rowPoiner = sonNode[rowPoiner][colPointer]
    nodeNum[rowPoiner] += 1


def query(str):
    global nodePointer
    rowPoiner = 0
    for i in range(len(str)):
        colPointer = ord(str[i]) - ord("a")
        if sonNode[rowPoiner][colPointer] == 0:
            return 0
        rowPoiner = sonNode[rowPoiner][colPointer]
    return nodeNum[rowPoiner]


num = int(input())
for i in range(num):
    operation, str = input().split()
    if operation == "I":
        insert(str)
    else:
        ans = query(str)
        print(ans)
