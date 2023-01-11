# 快速排序
def quick_sort(lst, l, r):
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