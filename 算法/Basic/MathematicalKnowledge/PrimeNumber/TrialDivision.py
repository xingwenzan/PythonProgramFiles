# 试除法判定质数 https://www.acwing.com/problem/content/868/

def judge(x):
    if x < 2: return False
    i = 2
    while i <= x / i:
        if x % i == 0:
            return False
        i += 1
    return True


n = int(input())
for i in range(n):
    x = int(input())
    if judge(x):
        print("Yes")
    else:
        print("No")
