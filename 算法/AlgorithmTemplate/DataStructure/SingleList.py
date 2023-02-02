# 单链表 https://www.acwing.com/problem/content/828/
# head -> 头节点（值 value, 下一个节点的指针 pointer）-> …… 尾节点（值 value, 下一个节点的指针 -1）-> 结尾（值 空值）

# head = 0
values = [0]  # 0 号位没有意义
pointers = [0]  # 0 号位代表头节点
idx = 1  # 时间上第几次操作

''' 头节点插入
def add_to_head(x):
    global idx
    values.append(x)
    pointers.append(pointers[0])
    pointers[0] = idx
    idx += 1
'''


def add(x, k=0):
    global idx
    values.append(x)
    pointers.append(pointers[k])
    pointers[k] = idx
    idx += 1


def drop(k):
    pointers[k] = pointers[pointers[k]]


n = int(input())
for i in range(n):
    lst = input().split()
    if lst[0] == "H":
        add(int(lst[1]))
    elif lst[0] == "D":
        drop(int(lst[1]))
    else:
        add(int(lst[2]), int(lst[1]))

i = pointers[0]
res = []
while i != 0:
    res.append(values[i])
    i = pointers[i]
print(" ".join(map(str, res)))
