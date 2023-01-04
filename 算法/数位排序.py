# 原题链接：https://www.acwing.com/problem/content/4656/

'''
# 直接求解/现求现排

n = int(input())
m = int(input())

d = dict()

for i in range(1,n+1):
    d[i] = sum(list(map(int,str(i))))

lst = list(d.items())
lst.sort(key=lambda x : x[1])
print(lst[m-1][0])
'''

'''
# 快速排序/求好查询排序

from functools import cmp_to_key
import numpy as np

allNum = 10 ** 6 + 10
w = np.zeros(allNum)
s = np.zeros(allNum)

for i in range(allNum):
        w[i] = i+1
        j = i
        while (j > 0):
            s[i] += j % 10
            j = int(j / 10)

n = int(input())
m = int(input())

def cmp(x,y):
    if(s[x] != s[y]):
        if(s[x]<s[y]): return -1
        else: return 1
    if(x<y):return -1
    elif(x>y):return 1
    else:return 0

lst = [i for i in range(1,n+1)]

lst.sort(key=cmp_to_key(cmp))
print(lst[m-1])
# print(lst)
'''

# 快速选择 - 手写
# 思路链接：https://www.acwing.com/activity/content/code/content/5088776/
# 实现：待定……
