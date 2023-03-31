# 最大公约数 https://www.acwing.com/problem/content/874/
# 欧几里得算法、辗转相除法

def gcd(a, b):
    return gcd(b, a % b) if b != 0 else a


n = int(input())
for i in range(n):
    a, b = map(int, input().split())
    print(gcd(a, b))
