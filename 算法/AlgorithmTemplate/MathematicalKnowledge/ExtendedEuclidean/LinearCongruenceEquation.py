# 线性同余方程 https://www.acwing.com/problem/content/880/
# ax ≡ b(mod m)   等价于   ax%m = b   等价于   ax = my+b   等价于   ax+(my') = b

def exgcd(a, b):
    if b == 0:
        return a, 1, 0
    gcd, y, x = exgcd(b, a % b)
    y -= a // b * x
    return gcd, x, y


n = int(input())
for i in range(n):
    a, b, m = map(int, input().split())
    gcd, x, y = exgcd(a, m)
    if b % gcd:
        print("impossible")
    else:
        print(int(b // gcd * x % m))
