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


# 前缀和实验/差分实验 (一维)
'''
n,m = map(int,input().split())
lst = list(map(int,input().split()))
add = [0]*(n+1)
#s = BasicAlgorithms.prefix_sum_1D(lst) # 前缀和
for i in range(m):
    l,r,c = map(int,input().split())
    #print(s[r]-s[l-1]) # 前缀和
    add = BasicAlgorithms.finite_difference_1D(add,l-1,r-1,c)
t = 0
for i in range(n):
    t += add[i]
    lst[i] += t
print(*lst)#,sep=" ")
'''


# 前缀和实验/差分实验 (二维)

n,m,q = map(int,input().split())
lst = []
for i in range(n):
    lst.append(list(map(int,input().split())))
#ans = BasicAlgorithms.prefix_sum_2D(lst,n,m) # 前缀和
add = [[0 for i in range(m+1)] for i in range(n+1)]
for i in range(q):
    x1,y1,x2,y2,c = map(int,input().split())
    #out = ans[x2][y2] - ans[x1-1][y2] - ans[x2][y1-1] + ans[x1-1][y1-1] # 前缀和
    #print(out) # 前缀和
    add = BasicAlgorithms.finite_difference_2D(add,x1-1,y1-1,x2-1,y2-1,c) # 差分
add = BasicAlgorithms.prefix_sum_2D(add,n+1,m+1) # 差分实验（前缀和函数）
for i in range(n): # 差分
    for j in range(m):
        lst[i][j] += add[i+1][j+1] # （add 使用的前缀和，左上两边各多一条）
    print(*lst[i])