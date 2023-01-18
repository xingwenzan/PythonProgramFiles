'''  ---用于实验算法模板---  '''

# 快排实验/归并实验/逆序对计数实验
'''
from 算法.AlgorithmTemplate import BasicAlgorithms

n = int(input())
lst1 = list(map(int, input().split()))

#BasicAlgorithms.quick_sort(lst1, 0, n - 1) # 快排实验
#BasicAlgorithms.merge_sort(lst1, 0, n - 1) # 归并实验
res = BasicAlgorithms.Number_of_reversed_pairs(lst1, 0, n - 1) # 逆序对计数实验

#print(" ".join(map(str,lst1)))
print(res)
'''


# 快选实验
'''
from 算法.AlgorithmTemplate import BasicAlgorithms

nk = list(map(int, input().split()))
n = nk[0]
k = nk[1]
lst = list(map(int, input().split()))
ans = BasicAlgorithms.quick_choose(lst,0,n-1,k)
print(ans)
'''


# 二分实验
n, q = map(int, input().split())
lst = list(map(int, input().split()))

def dichotomize_left(lst, l, r, num):
    while l < r:
        mid = l + r + 1 >> 1
        if lst[mid] <= num:
            l = mid
        else:
            r = mid - 1
    return l

def dichotomize_right(lst, l, r, num):
    while l < r:
        mid = l + r >> 1
        if lst[mid] >= num:
            r = mid
        else:
            l = mid + 1
    return r

for i in range(q):
    num = int(input())
    l = dichotomize_left(lst,0,n-1,num)
    r = dichotomize_right(lst,0,n-1,num)
    if lst[l]!=num or lst[r]!=num:print("-1 -1")
    else:print(str(r)+" "+str(l))
