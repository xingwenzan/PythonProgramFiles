# 超快速排序 https://www.acwing.com/problem/content/109/
# 归并求逆序对

N = 500005
lst = [0] * N
tmp = [0] * N


def merge_sort(l, r):
    if l >= r: return 0
    mid = (l + r) // 2
    ans = merge_sort(l, mid) + merge_sort(mid + 1, r)

    i, j, k = l, mid + 1, 0
    while i <= mid and j <= r:
        if lst[i] <= lst[j]:
            tmp[k] = lst[i]
            k += 1
            i += 1
        else:
            tmp[k] = lst[j]
            k += 1
            j += 1
            ans += mid - i + 1
    while i <= mid:
        tmp[k] = lst[i]
        k += 1
        i += 1
    while j <= r:
        tmp[k] = lst[j]
        k += 1
        j += 1

    a = 0
    for b in range(l, r + 1):
        lst[b] = tmp[a]
        a += 1

    return ans


while True:
    n = int(input())
    if n == 0: break
    for i in range(n): lst[i] = int(input())
    print(merge_sort(0, n - 1))
