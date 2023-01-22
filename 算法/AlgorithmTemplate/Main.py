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


# 高精度算法实验

from 算法.AlgorithmTemplate import BasicAlgorithms
a = input()[::-1]
b = input()[::-1]
c = BasicAlgorithms.high_precision_addition(a,b)
print(c)
