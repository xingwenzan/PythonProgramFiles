# 怪盗基德的滑翔翼 https://www.acwing.com/problem/content/1019/

def LIS(array, length):
    ans = 0

    f = [1] * length
    for i in range(length):
        for j in range(i):
            if array[i] < array[j]:
                f[i] = max(f[i], f[j] + 1)
        ans = max(ans, f[i])

    f = [1] * length
    for i in range(length):
        for j in range(i):
            if array[i] > array[j]:
                f[i] = max(f[i], f[j] + 1)
        ans = max(ans, f[i])
    return ans


k = int(input())
for _ in range(k):
    n = int(input())
    lst = list(map(int, input().split()))
    print(LIS(lst, n))
