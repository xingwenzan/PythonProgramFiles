# 双链表 https://www.acwing.com/problem/content/829/

values = ["0","0"] # 头、尾节点无值，0 号位为头，1 号位为尾
left_pointers = [-1,0] # 指向左的指针，指针指向 -1 意为该指针为头节点，不能更左了
right_pointers = [1,-1] # 指向右的指针，指针指向 -1 意为该指针为尾节点，不能更右了
idx = 2

def add(k,x):
    global idx
    values.append(x)
    left_pointers.append(k)
    right_pointers.append(right_pointers[k])
    left_pointers[right_pointers[k]] = idx
    right_pointers[k] = idx
    idx += 1

def drop(k):
    right_pointers[left_pointers[k]] = right_pointers[k]
    left_pointers[right_pointers[k]] = left_pointers[k]

M = int(input())
for i in range(M):
    lst = input().split()
    if lst[0] == "L":
        k = 0
        x = int(lst[1])
        add(k,x)
    elif lst[0] == "R":
        k = left_pointers[1]
        x = int(lst[1])
        add(k,x)
    elif lst[0] == "IR":
        k = int(lst[1])+1
        x = int(lst[2])
        add(k,x)
    elif lst[0] == "IL":
        k = left_pointers[int(lst[1])+1]
        x = int(lst[2])
        add(k, x)
    else:
        k = int(lst[1])+1
        drop(k)

pointer = right_pointers[0]
res = []
while right_pointers[pointer] != -1:
    res.append(values[pointer])
    pointer = right_pointers[pointer]
print(" ".join(map(str, res)))