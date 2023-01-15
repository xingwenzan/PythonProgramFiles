'''  ---用于实验算法模板---  '''

# 快排实验/归并实验

from 算法.AlgorithmTemplate import BasicAlgorithms

n = int(input())
lst1 = list(map(int, input().split()))

#BasicAlgorithms.quick_sort(lst1, 0, n - 1)
BasicAlgorithms.merge_sort(lst1, 0, n - 1)

print(" ".join(map(str,lst1)))


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

