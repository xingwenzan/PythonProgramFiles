# 欧拉函数 https://www.acwing.com/problem/content/875/

def eulerFunction(x):
    ans = x
    num = 2
    while num <= x / num:
        if x % num == 0:
            ans = ans / num * (num - 1)  # 先除后乘，避免溢出
            while x % num == 0:
                x /= num
        num += 1
    if x > 1: ans = ans / x * (x - 1)  # 先除后乘，避免溢出
    return int(ans)


n = int(input())
for _ in range(n):
    x = int(input())
    print(eulerFunction(x))
