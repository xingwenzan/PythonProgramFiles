# 滑动窗口 https://www.acwing.com/problem/content/156/

values = [0] * 100010  # 注意：本次该数组存的是实际值在原数组的下标
headPointer = 0
tailPointer = -1


def push(x):
    global tailPointer
    tailPointer += 1
    values[tailPointer] = x


def popHead():
    global headPointer
    headPointer += 1


def popTail():
    global tailPointer
    tailPointer -= 1


def empty():
    global headPointer
    global tailPointer
    return headPointer > tailPointer


def head():
    global headPointer
    return values[headPointer]


def tail():
    global tailPointer
    return values[tailPointer]


def init():
    global headPointer
    global tailPointer
    headPointer = 0
    tailPointer = -1


n, k = map(int, input().split())
lst = list(map(int, input().split()))
lowAns = []
for i in range(n):
    if (not empty()) and head() < i - k + 1: popHead()
    while (not empty()) and lst[tail()] >= lst[i]: popTail()
    push(i)
    if i >= k - 1: lowAns.append(lst[head()])
print(" ".join(map(str, lowAns)))

init()

highAns = []
for i in range(n):
    if (not empty()) and head() < i - k + 1: popHead()
    while (not empty()) and lst[tail()] <= lst[i]: popTail()
    push(i)
    if i >= k - 1: highAns.append(lst[head()])
print(" ".join(map(str, highAns)))
