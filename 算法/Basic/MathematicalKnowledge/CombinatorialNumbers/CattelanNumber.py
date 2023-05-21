# 满足条件的01序列 https://www.acwing.com/problem/content/891/
# n 的卡特兰数 C_2n^n -C_2n^{n-1} = (C_2n^n)/(n+1)

mod = int(1e9 + 7)


def qmi(base, index, mod):  # 快速幂求逆元
    ans = 1 % mod
    while index:
        if index & 1: ans = ans * base % mod
        base = base * base % mod
        index >>= 1
    return ans


def Cab(a, b, mod):
    ans = 1
    i, j = 1, a
    while i <= b:
        ans = ans * j % mod
        ans = ans * qmi(i, mod - 2, mod) % mod
        i += 1
        j -= 1
    return ans


def cattelan(num):
    return Cab(2 * num, num, mod) * qmi(num + 1, mod - 2, mod) % mod


n = int(input())
print(cattelan(n))
