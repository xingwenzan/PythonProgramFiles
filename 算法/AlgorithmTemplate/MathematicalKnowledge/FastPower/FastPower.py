# 快速幂 https://www.acwing.com/problem/content/877/

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
