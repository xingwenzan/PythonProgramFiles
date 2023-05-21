# 快速幂求逆元 https://www.acwing.com/problem/content/878/

'''
    逆元公式推导：a/b ≡ a*x (mod m)；等式两边同时乘 b，得：b*a/b ≡ a*b*x (mod m)，化简得：a ≡ a*b*x (mod m)
    所以 b*x ≡ 1 (mod m)，由费马小定理，b^(m-1) ≡ 1 (mod m) 其中 m 为质数。联系本方程 b * b^(m-2) ≡ 1，所以 b 的逆元 x 为 b^(m-2)；
    若 b 是 m 的倍数，则无解的，因为 b 是 m 的倍数，那么 b*x 也必定是 m 的倍数，模 m 的余数为 0，必定不为 1，是无解的情况。
    若 b 不是 m 的倍数，由于 m 是质数，那么 b 与 m 是互质的，由费马小定理可知，b^(m-1) ≡ 1 (mod m)，一定存在逆元，一定有解。
'''


def fastPower(base, index, mod):
    ans = 1 % mod
    while index:
        if index & 1: ans = ans * base % mod
        base = base * base % mod
        index >>= 1
    return ans


n = int(input())
for i in range(n):
    a, p = map(int, input().split())
    if a % p:
        print(fastPower(a, p - 2, p))
    else:
        print("impossible")
