# 双指针实验 数组元素的目标和 https://www.acwing.com/problem/content/802/

n, m, x = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

j = m - 1
for i in range(n):
    while a[i] + b[j] > x:
        j -= 1
    if j >= 0 and a[i] + b[j] == x:
        print(i,j)
        break
