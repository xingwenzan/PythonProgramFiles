# 筛质数 https://www.acwing.com/problem/content/870/

N = 10 ** 6 + 10
prime = [0] * N
state = [False] * N


def EhrlichSieve(x):
    num = 0
    for i in range(2, x + 1):
        if not state[i]:
            prime[num] = i
            num += 1
            j = i + i
            while j <= x:
                state[j] = True
                j += i
    return num


def LinearSieve(x):
    num = 0
    for i in range(2, x + 1):
        if not state[i]:
            prime[num] = i
            num += 1
        j = 0
        while prime[j] <= x / i:   # 除法防溢出
            state[i * prime[j]] = True
            if i % prime[j] == 0: break
            j += 1
    return num


n = int(input())
print(EhrlichSieve(n))
print(LinearSieve(n))
