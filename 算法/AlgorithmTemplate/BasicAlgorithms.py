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


# 逆序对计数 - 归并排序应用 O(nlogn) https://www.acwing.com/problem/content/790/
def Number_of_reversed_pairs(lst, l, r):
    if l>=r: return 0
    mid = l+r>>1
    res = Number_of_reversed_pairs(lst, l, mid) + Number_of_reversed_pairs(lst, mid+1, r)
    i,j,k = l,mid+1,0
    tmp = [0]*(r-l+1)
    while i<=mid and j<=r:
        if lst[i]<=lst[j]:
            tmp[k]=lst[i]
            i += 1
            k += 1
        else:
            tmp[k] = lst[j]
            j += 1
            k += 1
            res += mid-i+1
    while i<=mid:
        tmp[k] = lst[i]
        i += 1
        k += 1
    while j <= r:
        tmp[k] = lst[j]
        j += 1
        k += 1

    b = 0
    for a in range(l,r+1,1):
        lst[a] = tmp[b]
        a += 1
        b += 1

    return res


# 二分 O() https://www.acwing.com/problem/content/791/
 # 不可调用，提供思路
 # 模板 1：左半边为 true
def dichotomize_left(l,r,check):
    while l<r:
        mid = l+r+1>>1
        if check==True:l = mid
        else:r = mid-1
    return l
 # 模板 2：右半边为 true
def dichotomize_right(l,r,check):
    while l<r:
        mid = l+r>>1
        if check==True:r = mid
        else:l = mid+1
    return r