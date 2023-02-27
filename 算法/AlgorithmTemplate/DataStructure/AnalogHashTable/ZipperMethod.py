# 模拟散列表 https://www.acwing.com/problem/content/842/
# 拉链法

N = 10 ** 5 + 3
hashTable = [-1] * N
value = [0] * N
nextPointer = [-1] * N
pointer = 0


def insert(num):
    global pointer
    position = num % N
    value[pointer] = num
    nextPointer[pointer] = hashTable[position]
    hashTable[position] = pointer
    pointer += 1


def query(num):
    position = hashTable[num % N]
    while position != -1:
        if value[position] == num: return True
        position = nextPointer[position]
    return False


n = int(input())
for i in range(n):
    operation, num = input().split()
    if operation == "I":
        insert(int(num))
    else:
        judge = query(int(num))
        if judge:
            print("Yes")
        else:
            print("No")
