# 模拟队列 https://www.acwing.com/problem/content/831/

values = []
pointer = 0


def push(x):
    values.append(x)


def pop():
    global pointer
    pointer += 1


def empty():
    return pointer >= len(values)


def query():
    global pointer
    return values[pointer]


M = int(input())
for i in range(M):
    lst = input().split()
    if lst[0] == "push":
        push(int(lst[1]))
    elif lst[0] == "pop":
        pop()
    elif lst[0] == "empty":
        if empty():
            print("YES")
        else:
            print("NO")
    else:
        print(query())