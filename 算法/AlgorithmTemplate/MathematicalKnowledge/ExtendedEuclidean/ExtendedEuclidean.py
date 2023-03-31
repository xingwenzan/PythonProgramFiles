# 扩展欧几里得算法 https://www.acwing.com/problem/content/879/
# 扩展辗转相除法、求最大公约数算法扩展
# https://blog.csdn.net/destiny1507/article/details/81750874

def exgcd(a, b):  # a*x+b*y = gcd
    if b == 0:
        gcd, x, y = a, 1, 0  # 此时 y 可以是任何数，gcd 是最大公约数，本题里可有可无
        return gcd, x, y
    gcd, y, x = exgcd(b, a % b)
    y -= a // b * x
    return gcd, x, y


n = int(input())
for i in range(n):
    a, b = map(int, input().split())
    gcd, x, y = exgcd(a, b)
    print("{} {}".format(x, y))
