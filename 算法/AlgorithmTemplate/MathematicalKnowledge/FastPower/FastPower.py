# 快速幂 https://www.acwing.com/problem/content/877/

'''
    a^b mod p
    所谓快速幂的快速在于将指数b分解成了二进制数表示，b= x_k ... x_1 x_0，而代码实现的核心则是反复平方
    a^b = a^(2^x_k+...2^x_1+2^x_0) = a^(2^x_k) * ... * a^(2^x_1) * a^(2^x_0)
    这样就把a^b分解成logb个数相乘了，其中相邻两项中后一项是前一项的平方
'''


def fastPower(base, index, mod):
    ans = 1 % mod
    while index:
        if index & 1:
            ans = ans * base % mod
        base = base * base % mod
        index >>= 1
    return ans


n = int(input())
for i in range(n):
    a, b, p = map(int, input().split())
    print(fastPower(a, b, p))
