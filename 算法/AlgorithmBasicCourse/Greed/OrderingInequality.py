# 排队打水 https://www.acwing.com/problem/content/description/915/

n = int(input())
lst = list(map(int, input().split()))
lst.sort(reverse=True)
ans = 0
for i in range(n):
    ans += lst[i] * i
print(ans)
