# https://www.acwing.com/problem/content/3959/

import 算法.AlgorithmBasicCourse.BasicAlgorithms.BasicAlgorithmsTemplate as BA

n = int(input())
lst = list(map(int,input().split()))

prefixAnd = BA.prefix_sum_1D(lst)
cnt,ans = 0,0

if prefixAnd[n]%3!=0 or n<3:
    print(0)
else:
    for i in range(2,n,1):
        if prefixAnd[i-1]==prefixAnd[n]/3:
            cnt+=1
        if prefixAnd[i]==prefixAnd[n]*2/3:
            ans+=cnt
    print(ans)