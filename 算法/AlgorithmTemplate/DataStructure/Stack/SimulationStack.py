# 模拟栈 https://www.acwing.com/problem/content/830/

values = [0] * 100010
num = 0


def push(x):
    global num
    num += 1
    values[num] = x


def pop():
    global num
    num -= 1


def empty():
    global num
    if num == 0:
        print("YES")
    else:
        print("NO")


def query():
    global num
    print(values[num])


M = int(input())
for i in range(M):
    lst = input().split()
    if lst[0] == "push":
        push(lst[1])
    elif lst[0] == "query":
        query()
    elif lst[0] == "pop":
        pop()
    else:
        empty()
