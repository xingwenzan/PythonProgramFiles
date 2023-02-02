# 双指针实验 最长连续不重复子序列 https://www.acwing.com/problem/content/801/

n = int(input())
lst = list(map(int,input().split()))

repeat = [0]*(10**5+1)
l = 0
res = 0
for r in range(n):
    repeat[lst[r]] += 1
    while repeat[lst[r]]>1:
        repeat[lst[l]] -= 1
        l += 1
    res = max(res,r-l+1)
print(res)