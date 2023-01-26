# 二分实验 数的范围 https://www.acwing.com/problem/content/791/
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