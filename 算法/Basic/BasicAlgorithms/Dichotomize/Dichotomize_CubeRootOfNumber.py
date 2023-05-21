# 二分实验 数的三次方跟 https://www.acwing.com/problem/content/792/

n = float(input())

l = -100
r = 100
while r-l>10**(-8):
    mid = (l+r)/2
    if mid**3<=n:l=mid
    else:r = mid

print("{:.6f}".format(l))