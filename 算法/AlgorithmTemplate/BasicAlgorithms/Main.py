'''  ---用于实验算法模板---  '''

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

# 二分实验（整数二分）
'''
n, q = map(int, input().split())
lst = list(map(int, input().split()))
for i in range(q):
    num = int(input())
    l = BasicAlgorithms.dichotomize_left(lst, num)
    r = BasicAlgorithms.dichotomize_right(lst, num)
    if lst[l] != num or lst[r] != num:
        print("-1 -1")
    else:
        print(str(r) + " " + str(l))
'''

# 二分实验（小数二分）
'''
n = float(input())
ans = BasicAlgorithms.dichotomize_float(n,3,6)
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
'''
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
'''

# 位运算实验（暴力版）
'''
n = int(input())
num = list(map(int, input().split()))
ans = [0] * n
for i in range(n):
    x = num[i]
    while x != 0:
        if x & 1 == 1: ans[i] += 1
        x = x >> 1
print(*ans)
'''

# 位运算实验（loebit 版）
'''
n = int(input())
num = list(map(int, input().split()))
ans = [0] * n
for i in range(n):
    x = num[i]
    while x != 0:
        x = x - BasicAlgorithms.lowbit(x)
        ans[i] += 1
print(*ans)
'''

# 离散化实验
'''
n, m = map(int, input().split())
point = []
add = []
lr = []
for i in range(n):
    x, c = map(int, input().split())
    add.append([x, c])
    point.append(x)
for i in range(m):
    l, r = map(int, input().split())
    lr.append([l, r])
    point.append(l)
    point.append(r)
new_point = BasicAlgorithms.discretization(point)
lst = [0] * (len(new_point))
for i in range(n):
    x = BasicAlgorithms.dichotomize_right(new_point, add[i][0])
    lst[x] += add[i][1]
lst = BasicAlgorithms.prefix_sum_1D(lst)
for i in range(m):
    l = BasicAlgorithms.dichotomize_right(new_point, lr[i][0]) + 1
    r = BasicAlgorithms.dichotomize_right(new_point, lr[i][1]) + 1
    print(lst[r] - lst[l - 1])
'''

# 区间合并实验

n = int(input())
lst = []
for i in range(n):
    x = list(map(int, input().split()))
    lst.append(x)
ans = BasicAlgorithms.interval_merge(lst)
print(len(ans))
