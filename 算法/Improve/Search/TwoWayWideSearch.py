# 双向广搜 字串变换 https://www.acwing.com/problem/content/192/
import collections
import re
import sys


def do(q, dx, dy, x, y):
    d = dx[q[0]]
    while len(q) > 0 and dx[q[0]] == d:
        fa = q.popleft()
        for i in range(len(x)):
            for j in [substr.start() for substr in re.finditer(x[i], fa)]:
                son = "".join([fa[0:j], y[i], fa[j + len(x[i]):]])
                if son in dy: return dy[son] + dx[fa] + 1
                if son in dx: continue
                dx[son] = dx[fa] + 1
                q.append(son)
    return 11


A, B = input().split()
a, b = [], []
for line in sys.stdin:
    x, y = line.split()
    a.append(x)
    b.append(y)

da, db = {A: 0}, {B: 0}  # 距离
qa, qb = collections.deque([A]), collections.deque([B])  # bfs 队列


def bfs():
    step = 0
    while len(qa) > 0 and len(qb) > 0 and step < 10:  # 某一个为 0 意味着所有情况都遍历了也没有结果
        if len(qb) < len(qa):
            t = do(qb, db, da, b, a)
        else:
            t = do(qa, da, db, a, b)
        if t <= 10: return t
        step += 1
    return -1


if A == B:
    print(0)
else:  # BFS
    ans = bfs()
    if ans == -1:
        print("NO ANSWER!")
    else:
        print(ans)
