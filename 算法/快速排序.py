# https://www.acwing.com/problem/content/787/
from 算法.AlgorithmTemplate import BasicAlgorithms

n = int(input())
lst1 = list(map(int, input().split()))

'''

def quick_sort(lst, l, r):
    if l >= r: return  # 左边界索引不小于右边界索引，无法进行，不搞
    i = l-1  # i 指针指向列表的 l 号值
    j = r+1  # j 指针指向列表的 r 号值
    x = lst[(l + r ) >> 1]
    while i < j:
        i+=1
        while lst[i] < x: i += 1
        j-=1
        while lst[j] > x: j -= 1
        if i < j: lst[i], lst[j] = lst[j], lst[i]
    
    # 用 j 的时候，x 要向下取整，防止卡死在右边界
    quick_sort(lst, l, j)
    quick_sort(lst, j+1, r)



def quick_sort(lst, l, r):
    if l >= r: return  # 左边界索引不小于右边界索引，无法进行，不搞
    i = l-1  # i 指针指向列表的 l 号值
    j = r+1  # j 指针指向列表的 r 号值
    x = lst[(l + r +1) >> 1]
    while i < j:
        i+=1
        while lst[i] < x: i += 1
        j-=1
        while lst[j] > x: j -= 1
        if i < j: lst[i], lst[j] = lst[j], lst[i]
        
    # 用 i 的时候，x 要向上取整，防止卡死在左边界
    quick_sort(lst, l, i-1)
    quick_sort(lst, i, r)
'''

BasicAlgorithms.quick_sort(lst1, 0, n - 1)

print(" ".join(map(str,lst1)))