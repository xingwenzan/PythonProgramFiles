# 改变数组元素 https://www.acwing.com/problem/content/3732/

T = int(input())
for i in range(T):
    n = int(input())
    lst = [0] * n
    ai = list(map(int, input().split()))
    for j in range(n):
        if ai[j] > 0:
            l = j - ai[j] + 1 if j - ai[j] + 1 >= 0 else 0
            r = j + 1
            lst[l] += 1
            if r < n: lst[r] -= 1
    tmp = 0
    for j in range(1, n):
        lst[j] += lst[j - 1]
    for j in range(n):
        if lst[j] > 0:
            lst[j] = 1
        else:
            lst[j] = 0
    print(" ".join(map(str, lst)))
