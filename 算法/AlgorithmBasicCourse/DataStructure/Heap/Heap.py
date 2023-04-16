# 模拟堆 https://www.acwing.com/problem/content/841/

N = 10 ** 5 + 10
heap = [0] * N  # 堆，0 号位存堆大小
position = [0] * N  # 第 k 个输入的元素在堆中的位置，0 号位无意义
number = [0] * N  # 堆中 k 号位置对应的第几个插入，0 号位无意义


def heap_swap(pointerA, pointerB):
    position[number[pointerA]], position[number[pointerB]] = position[number[pointerB]], position[number[pointerA]]
    number[pointerA], number[pointerB] = number[pointerB], number[pointerA]
    heap[pointerA], heap[pointerB] = heap[pointerB], heap[pointerA]


def down(pointer):
    tmpPointer = pointer
    if pointer * 2 <= heap[0] and heap[pointer * 2] < heap[tmpPointer]:
        tmpPointer = pointer * 2
    if pointer * 2 + 1 <= heap[0] and heap[pointer * 2 + 1] < heap[tmpPointer]:
        tmpPointer = pointer * 2 + 1
    if tmpPointer != pointer:
        heap_swap(tmpPointer, pointer)
        down(tmpPointer)


def up(pointer):
    while (pointer <= heap[0]) and ((pointer >> 1) > 0) and (heap[pointer >> 1] > heap[pointer]):
        heap_swap(pointer, pointer >> 1)
        pointer = (pointer >> 1)


operation = int(input())
k = 0  # 第 k 个数
for i in range(operation):
    lst = input().split()
    if lst[0] == "I":
        heap[0] += 1
        k += 1
        position[k] = heap[0]
        number[heap[0]] = k
        heap[heap[0]] = int(lst[1])
        up(heap[0])
    elif lst[0] == "PM":
        print(heap[1])
    elif lst[0] == "DM":
        heap_swap(1, heap[0])
        heap[0] -= 1
        down(1)
    elif lst[0] == "D":
        tmpK = position[int(lst[1])]
        heap_swap(tmpK, heap[0])
        heap[0] -= 1
        down(tmpK)
        up(tmpK)
    else:
        tmpK = position[int(lst[1])]
        heap[tmpK] = int(lst[2])
        down(tmpK)
        up(tmpK)
