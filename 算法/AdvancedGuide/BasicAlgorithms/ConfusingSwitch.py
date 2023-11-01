# 费解的开关 https://www.acwing.com/problem/content/97/
# 枚举第一行的操作，确定第一行状态，以确定后面所有行状态，获取结果
import copy

lst = []
tmp = []
dx, dy = [0, -1, 0, 1, 0], [0, 0, -1, 0, 1]


def work(x, y):
    for i in range(5):
        tx, ty = x + dx[i], y + dy[i]
        if tx < 0 or ty < 0 or tx >= 5 or ty >= 5: continue
        if tmp[tx][ty] == '0':
            tmp[tx][ty] = '1'
        else:
            tmp[tx][ty] = '0'
    return


def recursion(op):
    res = 0
    # 获取第一行操作之后的状态
    for i in range(5):
        if (op >> i) & 1:
            work(0, i)
            res += 1
    # 根据第一行操作后状态对后四行操作
    for i in range(4):
        for j in range(5):
            if tmp[i][j] == '0':
                work(i + 1, j)
                res += 1
    # 未变成目标状态，返回‘无穷大’
    for i in range(5):
        if tmp[4][i] == '0': return float('inf')
    return res


n = int(input())
for z in range(n):
    if z != 0: input()  # 跳过矩阵之间的空格
    lst = []
    for _ in range(5): lst.append([i for i in input()])
    ans = float('inf')
    # 枚举操作
    for i in range(1 << 5):
        tmp = copy.deepcopy(lst)
        ans = min(recursion(i), ans)
    if ans > 6:
        print(-1)
    else:
        print(ans)
