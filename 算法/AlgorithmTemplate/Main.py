'''  ---用于实验算法模板---  '''
from 算法.AlgorithmTemplate import BasicAlgorithms

# 快排实验/归并实验/逆序对计数实验
'''
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
nk = list(map(int, input().split()))
n = nk[0]
k = nk[1]
lst = list(map(int, input().split()))
ans = BasicAlgorithms.quick_choose(lst,0,n-1,k)
print(ans)
'''


# 高精度算法实验
'''
a = input()
b = input()
#c = BasicAlgorithms.high_precision_addition(a,b) # 加法
#c = BasicAlgorithms.high_precision_subtraction(a,b) # 减法
#c = BasicAlgorithms.high_precision_multiplication(a,b) # 乘法
#c,d = BasicAlgorithms.high_precision_division_low(a,b) # 除法(高精度/低精度)
c,d = BasicAlgorithms.high_precision_division_high(a,b) # 除法(高精度/高精度)
print(c)
print(d)
'''


# 前缀和实验 一维
'''
n,m = map(int,input().split())
lst = list(map(int,input().split()))
s = BasicAlgorithms.prefix_sum_1D(lst)
for i in range(m):
    l,r = map(int,input().split())
    print(s[r]-s[l-1])
'''


# 前缀和实验 二维

n,m,q = map(int,input().split())
lst = []
for i in range(n):
    lst.append(list(map(int,input().split())))
ans = BasicAlgorithms.prefix_sum_2D(lst,n,m)
for i in range(q):
    x1,y1,x2,y2 = map(int,input().split())
    out = ans[x2][y2] - ans[x1-1][y2] - ans[x2][y1-1] + ans[x1-1][y1-1]
    print(out)
