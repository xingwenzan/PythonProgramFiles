# 求组合数 IV https://www.acwing.com/problem/content/890/
# 组合数 C_a^b 四种方法区别在于适合的数据范围不同
# 筛质数 - a!分解 - 高精度计算

N = 5010
primes, powers, pointer = [0] * N, [0] * N, 0
state = [False] * N


def getPrime(num):  # 筛出到 num 的质数
    global pointer
    for i in range(2, num + 1):
        if not state[i]:
            primes[pointer] = i
            pointer += 1
        for j in range(pointer):
            if i * primes[j] <= num: state[i * primes[j]] = True
            if i % primes[j] == 0: break
    return 0


def getPower(num, prime):  # 得出 num! 的质因数 prime 次幂数
    cnt = 0
    while num:
        cnt += num // prime
        num //= prime
    return cnt


def mul(string, num):  # 高精度乘法
    tmp = 0
    for i in range(len(string)):
        tmp += num * string[i]
        string[i] = tmp % 10
        tmp //= 10
    while tmp:
        string.append(tmp % 10)
        tmp //= 10
    return string


a, b = map(int, input().split())
getPrime(a)
for i in range(pointer):
    p = primes[i]
    powers[i] = getPower(a, p) - getPower(b, p) - getPower(a - b, p)
ans = [1]
for i in range(pointer):
    for j in range(powers[i]):
        ans = mul(ans, primes[i])
print(''.join(map(str, reversed(ans))))
