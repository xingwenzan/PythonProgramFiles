# https://www.acwing.com/problem/content/4659/

'''
# 暴力法
n,m = list(map(int,input().split()))
upgrade = []

for i in range(n):
    lst = list(map(int,input().split()))
    up = [lst[0]-j*lst[1] for j in range(int(lst[0]/lst[1])+1)]
    upgrade.extend(up)

upgrade.sort(reverse=True)
print(sum(upgrade[0:m]))
'''

'''
n,m = list(map(int,input().split()))
upgrade = []

for i in range(n):
    lst = list(map(int,input().split()))
    up = [lst[0]-j*lst[1] for j in range(int(lst[0]/lst[1])+1 if int(lst[0]/lst[1])+1<m else m)]
    upgrade.extend(up)

upgrade.sort(reverse=True)
print(sum(upgrade[0:m]))
'''

# 二分

n, m = list(map(int, input().split()))

aAndb = []
amax = 0


def decide(mid):
    num = 0
    for i in aAndb:
        if mid <= i[0]:
            num += (i[0] - mid) // i[1] + 1
    return num >= m


while n:
    n -= 1
    ai, bi = list(map(int, input().split()))
    aAndb.append([ai, bi])
    amax = max(ai, amax)

l, r = 0, amax
while l < r:
    mid = (l + r + 1) >> 1  # +1 防止死循环; >> 是右移运算，相当于除以 2 并向下取整，或 (l+r+1)//2
    if decide(mid):
        l = mid
    else:
        l = mid - 1

cnt = 0
res = 0
for i in aAndb:
    if i[0] > l:
        c = (i[0] - l) // i[1] + 1
        cnt += c
        end = i[0] - (c - 1) * i[1]
        res += (i[0] + end) * c >> 1

print(res - (cnt - m) * l)
