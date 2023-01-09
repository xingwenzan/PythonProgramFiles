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
n,m = list(map(int,input().split()))
a = []
b = []

def decide(mid):
    num = 0
    for i in range(n):
        if mid <= a[i]:
            num += (a[i]-mid)/b[i]+1
    return num>=m

for i in range(n):
    lst = list(map(int,input().split()))
    a.append(lst[0])
    b.append(lst[1])

l = 0
r = 1000000

while(l<r):
    mid = int((l+r+1)/2) # +1 防止死循环
    if decide(mid):l = mid
    else: r -= 1

cnt = 0
res = 0
for i in range(n):
    if a[i]>l:
        c = int((a[i]-l)/b[i]+1)
        cnt += c
        end = a[i] - (c-1)*b[i]
        res += (a[i]+end)*c/2

print(res-(cnt-m)*r)