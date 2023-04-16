# 拆分-Nim游戏 https://www.acwing.com/problem/content/896/

N = 110
sg_a = [-1] * N


def SG(x):
    if sg_a[x] != -1: return sg_a[x]
    tmp = []
    for i in range(x):
        for j in range(i + 1):
            tmp.append(SG(i) ^ SG(j))
    i = 0
    while True:
        if i not in tmp:
            sg_a[x] = i
            return sg_a[x]
        i += 1


n = int(input())
ai = list(map(int, input().split()))
ans = 0
for i in ai:
    ans ^= SG(i)
if ans:
    print("Yes")
else:
    print("No")
