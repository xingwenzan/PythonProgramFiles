# 集合-Nim游戏 https://www.acwing.com/problem/content/895/
# https://www.acwing.com/video/314/

N = int(1e4 + 10)
sg_h = [-1] * N


def SG(x, set_s):
    if sg_h[x] != -1: return sg_h[x]
    tmp = []
    for i in set_s:
        if x >= i: tmp.append(SG(x - i, set_s))
    i = 0
    while True:
        if i not in tmp:
            sg_h[x] = i
            return i
        i += 1


k = int(input())
s = list(map(int, input().split()))
n = int(input())
h = list(map(int, input().split()))
ans = 0
for i in h:
    ans ^= SG(i, s)
if ans:
    print("Yes")
else:
    print("No")
