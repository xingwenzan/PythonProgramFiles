# 表达整数的奇怪方式 https://www.acwing.com/problem/content/206/
# https://www.acwing.com/solution/content/3539/
# https://www.acwing.com/activity/content/code/content/5425217/
# 正确答案，但没学会，待定

def exgcd(a, b):  # 拿 a、b 最大公约数 gcd，和 ax+by=gcd 的一组解
    if b == 0:
        return a, 1, 0
    gdc, y, x = exgcd(b, a % b)
    y -= a // b * x
    return gdc, x, y


def formulaMerge(a1, m1, a2, m2):  # x ≡ m(mod a)，x 最小是 m
    gcd, k1, k2 = exgcd(a1, a2)
    if (m2 - m1) % gcd: return a1, -1
    k1 *= (m2 - m1) // gcd
    k1 = (k1 % (a2 // gcd) + (a2 // gcd)) % (a2 // gcd)
    m1 = k1 * a1 + m1
    a1 = a1 // gcd * a2
    return a1, m1


n = int(input())
a1, m1 = map(int, input().split())
for i in range(n - 1):
    a2, m2 = map(int, input().split())
    a1, m1 = formulaMerge(a1, m1, a2, m2)
    if m1 == -1: break
if m1 == -1:
    print(-1)
else:
    print((m1 % a1 + a1) % a1)
