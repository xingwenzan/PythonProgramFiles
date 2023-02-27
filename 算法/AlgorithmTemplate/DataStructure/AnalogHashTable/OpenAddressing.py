# 模拟散列表 https://www.acwing.com/problem/content/842/
# 开放寻址法

N = 2 * (10 ** 5) + 3
hashTable = ["0"] * N


def queryPosition(num):  # 如果 num 存在于哈希表，返回 num 位置，如果不存在，返回应该在的位置
    position = num % N
    while hashTable[position] != "0" and hashTable[position] != num:
        position += 1
        if position == N:
            position = 0
    return position


def insert(num):
    hashTable[queryPosition(num)] = num


def queryExist(num):
    position = queryPosition(num)
    if hashTable[position] == "0":
        return False
    else:
        return True


n = int(input())
for i in range(n):
    operation, num = input().split()
    if operation == "I":
        insert(int(num))
    else:
        judge = queryExist(int(num))
        if judge:
            print("Yes")
        else:
            print("No")
