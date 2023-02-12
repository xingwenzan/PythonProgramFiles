# 单调栈 https://www.acwing.com/problem/content/832/

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
        return True
    else:
        return False


def query():
    global num
    return values[num]


N = int(input())
lst = list(map(int, input().split()))
ans = []
for i in range(N):
    while (not empty()) and query() >= lst[i]:
        pop()
    if empty():
        ans.append(-1)
    else:
        ans.append(query())
    push(lst[i])
print(" ".join(map(str, ans)))
