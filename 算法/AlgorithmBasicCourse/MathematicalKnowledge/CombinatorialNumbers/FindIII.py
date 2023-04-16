# 求组合数 III https://www.acwing.com/problem/content/889/
# 组合数 C_a^b 四种方法区别在于适合的数据范围不同
# C_a^b ≡ C_{a%p}^{b%p} * C_{a//p}^{b//p}

def qmi(base, index, mod):  # 快速幂求逆元
    ans = 1 % mod
    while index:
        if index & 1: ans = ans * base % mod
        base = base * base % mod
        index >>= 1
    return ans


def Cab(a, b, mod):
    if b > a: return 0
    i, j, ans = 1, a, 1
    while i <= b:
        ans = ans * j % mod
        ans = ans * qmi(i, mod - 2, mod) % mod
        i += 1
        j -= 1
    return ans


def lucas(a, b, mod):
    if a < mod and b < mod: return Cab(a, b, mod)
    return Cab(a % mod, b % mod, mod) * lucas(a // mod, b // mod, mod) % mod


n = int(input())
for i in range(n):
    a, b, p = map(int, input().split())
    print(lucas(a, b, p))
