# 基础算法模板/快速调用

# 快速排序 O(nlogn)
def quick_sort(lst, l, r): # 要查的数列，左边界，右边界
    if l >= r: return  # 左边界索引不小于右边界索引，无法进行，不搞
    i = l-1  # i 指针指向列表的 l 号值
    j = r+1  # j 指针指向列表的 r 号值
    x = lst[(l + r) >> 1]
    while i < j:
        i+=1
        while lst[i] < x: i += 1
        j-=1
        while lst[j] > x: j -= 1
        if i < j: lst[i], lst[j] = lst[j], lst[i]
    quick_sort(lst, l, j)
    quick_sort(lst, j+1, r)

# 快速选择 O(n)
def quick_choose(lst, l, r, k): # 要查的数列，左边界索引，右边界索引，第 k 个数
    if l>=r:
        # print(lst[l])
        return lst[l]
    i = l-1
    j = r+1
    x = lst[(l+r+1)>>1]
    while i<j:
        i+=1
        while lst[i]<x:i+=1
        j-=1
        while lst[j]>x:j-=1
        if i<j : lst[i], lst[j] = lst[j], lst[i]

    if k<=i-l: return quick_choose(lst, l, i-1, k)
    else: return quick_choose(lst,i,r,k-(i-l))

    # print(lst(k-1))