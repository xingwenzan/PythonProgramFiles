# 64位整数乘法 https://www.acwing.com/problem/content/92/


a = int(input())
b = int(input())
c = int(input())

ans = 0

while a:
    if a & 1: ans = (ans + b) % c
    a >>= 1
    b = (b + b) % c

print(ans)
