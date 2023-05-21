# 堆排序 https://www.acwing.com/problem/content/840/

heap = [0] * (10 ** 5 + 10)  # 0 号位存堆中元素个数


def down(pointer):
    tmpPointer = pointer
    if pointer * 2 <= heap[0] and heap[pointer * 2] < heap[tmpPointer]:
        tmpPointer = pointer * 2
    if pointer * 2 + 1 <= heap[0] and heap[pointer * 2 + 1] < heap[tmpPointer]:
        tmpPointer = pointer * 2 + 1
    if tmpPointer != pointer:
        tmp = heap[pointer]
        heap[pointer] = heap[tmpPointer]
        heap[tmpPointer] = tmp
        down(tmpPointer)


'''
def up(pointer):
    if pointer//2>0 and heap[pointer//2]>heap[pointer]:
        tmp = heap[pointer]
        heap[pointer]=heap[pointer//2]
        heap[pointer//2]=tmp
        up(pointer//2)
'''


def init(lst):
    heap[0] = len(lst)
    for i in range(len(lst)):
        heap[i + 1] = lst[i]
    for i in range(heap[0] // 2, 0, -1):
        down(i)


n, m = map(int, input().split())
lst = list(map(int, input().split()))
init(lst)
ans = []
for i in range(m):
    ans.append(heap[1])
    heap[1] = heap[heap[0]]
    heap[0] -= 1
    down(1)
print(" ".join(map(str, ans)))
