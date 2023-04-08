# 求组合数 II https://www.acwing.com/problem/content/888/
# 组合数 C_a^b 四种方法区别在于适合的数据范围不同
# C_a^b = a!/[(a-b)!*b!] 预处理出 i! 和 (i!)^(-1) (i! 的逆元）

N, mod = int(1e5 + 10), int(1e9 + 7)
fact, infact = [1] * N, [1] * N


def qmi(base, index, mod):  # 快速幂求逆元
    ans = 1 % mod
    while index:
        if index & 1: ans = ans * base % mod
        base = base * base % mod
        index >>= 1
    return ans


for i in range(1, N):
    fact[i] = fact[i - 1] * i % mod
    infact[i] = infact[i - 1] * qmi(i, mod - 2, mod) % mod

n = int(input())
for i in range(n):
    a, b = map(int, input().split())
    print(fact[a] * infact[b] % mod * infact[a - b] % mod)
