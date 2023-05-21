# 最长上升子序列 II https://www.acwing.com/problem/content/898/

N = int(1e5) + 10
monotony = [0] * N
# monotony[0] = -2e9   # 第一次 find 结果一定是 1，故可有可无
length = 0;


def findX(x):
    l, r = 0, length
    while l < r:
        mid = (l + r + 1) >> 1
        if monotony[mid] < x:
            l = mid
        else:
            r = mid - 1
    return l


n = int(input())
lst = list(map(int, input().split()))
for i in range(n):
    tmp = findX(lst[i])
    length = max(length, tmp + 1)
    monotony[tmp + 1] = lst[i]
print(length)
