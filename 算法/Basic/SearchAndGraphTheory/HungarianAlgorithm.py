# 二分图的最大匹配 https://www.acwing.com/problem/content/863/
# https://www.acwing.com/activity/content/code/content/2676803/

N, M = 510, 10 ** 5 + 10
head, value, nextPointer, pointer = [-1] * N, [0] * M, [0] * M, 0  # 存男生看中的或者说可以询问的女生，head 索引是男生编号，其他是女生编号
match = [0] * N  # 存与该女生匹配的男生编号，索引是女生编号
query = [False] * N  # 存本次匹配中该女生是否被询问过，索引是女生编号


def add(man, woman):
    global pointer
    value[pointer] = woman
    nextPointer[pointer] = head[man]
    head[man] = pointer
    pointer += 1


def find(man):  # 询问该男生是否找到对象或询问该男生是否可以换对象
    nextWoman = head[man]
    while nextWoman != -1:
        woman = value[nextWoman]
        if not query[woman]:
            query[woman] = True
            if match[woman] == 0 or find(match[woman]):
                match[woman] = man
                return True
        nextWoman = nextPointer[nextWoman]
    return False


manNum, womanNum, fancy = map(int, input().split())
for i in range(fancy):
    man, woman = map(int, input().split())
    add(man, woman)
ans = 0
for i in range(1, manNum + 1):
    query = [False] * N
    if find(i): ans += 1

print(ans)
