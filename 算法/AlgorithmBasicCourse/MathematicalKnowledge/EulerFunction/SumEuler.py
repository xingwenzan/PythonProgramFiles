# 筛法求欧拉函数 https://www.acwing.com/problem/content/876/

N = 10 ** 6 + 10
euler = [1] * N
state = [False] * N
prime = []


def sumEuler(x):
    for i in range(2, x + 1):
        if not state[i]:
            prime.append(i)
            euler[i] = i - 1
        j = 0
        while prime[j] <= x / i:
            tmp = prime[j] * i
            state[tmp] = True
            if i % prime[j] == 0:
                euler[tmp] = prime[j] * euler[i]
                break
            euler[tmp] = euler[i] * (prime[j] - 1)
            j += 1
    ans = 0
    for i in range(1, x + 1):
        ans += euler[i]
    return ans


x = int(input())
print(sumEuler(x))
