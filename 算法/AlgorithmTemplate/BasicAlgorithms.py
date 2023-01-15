# 基础算法模板/快速调用

# 快速排序 O(nlogn) https://www.acwing.com/problem/content/787/
def quick_sort(lst, l, r):  # 要查的数列，左边界，右边界
    if l >= r: return  # 左边界索引不小于右边界索引，无法进行，不搞
    i = l - 1  # i 指针指向列表的 l 号值
    j = r + 1  # j 指针指向列表的 r 号值
    x = lst[(l + r) >> 1]
    while i < j:
        i += 1
        while lst[i] < x: i += 1
        j -= 1
        while lst[j] > x: j -= 1
        if i < j: lst[i], lst[j] = lst[j], lst[i]
    quick_sort(lst, l, j)
    quick_sort(lst, j + 1, r)


# 快速选择 O(n) https://www.acwing.com/problem/content/description/788/
def quick_choose(lst, l, r, k):  # 要查的数列，左边界索引，右边界索引，第 k 个数
    if l == r:
        # print(lst[l])
        return lst[l]
    i = l - 1
    j = r + 1
    x = lst[(l + r + 1) >> 1]
    while i < j:
        i += 1
        while lst[i] < x: i += 1
        j -= 1
        while lst[j] > x: j -= 1
        if i < j: lst[i], lst[j] = lst[j], lst[i]

    if k <= i - l:
        return quick_choose(lst, l, i - 1, k)
    else:
        return quick_choose(lst, i, r, k - (i - l))


# 归并排序 O(nlogn) #https://www.acwing.com/problem/content/789/
def merge_sort(lst, l, r):
    if l >= r: return
    mid = l + r >> 1
    merge_sort(lst, l, mid)
    merge_sort(lst, mid + 1, r)

    i = l
    j = mid+1
    tmp = [0] * (r - l + 1)
    k = 0

    while i <= mid and j <= r:
        if lst[i] <= lst[j]:
            tmp[k] = lst[i]
            i += 1
            k += 1
        else:
            tmp[k] = lst[j]
            j += 1
            k += 1
    while i <= mid:
        tmp[k]=lst[i]
        i += 1
        k += 1
    while j <= r:
        tmp[k] = lst[j]
        j += 1
        k += 1

    q = 0
    for p in range(l, r + 1, 1):
        lst[p] = tmp[q]
        q += 1
