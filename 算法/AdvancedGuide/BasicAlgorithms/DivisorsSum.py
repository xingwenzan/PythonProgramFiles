# 约数之和 https://www.acwing.com/problem/content/99/
# 详解 https://www.acwing.com/video/116/

mod = 9901


# 快速幂   qmi(a,b) = a^b%mod
def qmi(a, b):
    ans = 1
    a %= mod
    while b:
        if b & 1: ans = ans * a % mod
        b >>= 1
        a = a * a % mod
    return ans


# work(p,k) = p^0 + p^1 + ... + p^k
def work(p, k):
    if k == 0: return 1
    if k % 2 == 0: return (p % mod * work(p, k - 1) % mod + 1) % mod  # 奇数个（0~k）
    return (1 + qmi(p, k // 2 + 1)) % mod * work(p, k // 2) % mod


A, B = map(int, input().split())
if A:
    ans = 1
    # 分解质因数
    x = 2
    while x <= A / x:
        num = 0
        while A % x == 0:
            num += 1
            A /= x
        if num: ans = ans * work(x, num * B) % mod
        x += 1
    if A > 1: ans = ans * work(A, B) % mod
else:
    ans = 0
print(int(ans))
