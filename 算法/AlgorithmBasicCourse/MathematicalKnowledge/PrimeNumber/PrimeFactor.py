# 分解质因数 https://www.acwing.com/problem/content/869/
# https://zhuanlan.zhihu.com/p/351002242

def divide(x):
    tmp = 2
    while tmp <= x / tmp:
        if x % tmp == 0:
            num = 0
            while x % tmp == 0:
                x /= tmp
                num += 1
            print("{} {}".format(tmp, num))
        tmp += 1
    if x > 1: print("{} 1".format(int(x)))
    print()


n = int(input())
for i in range(n):
    x = int(input())
    divide(x)
