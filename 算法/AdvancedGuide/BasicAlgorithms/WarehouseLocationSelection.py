# 货仓选址 https://www.acwing.com/problem/content/description/106/
# n 奇数-中位数 偶数-中间两数区间内任意值 找中位数

n = int(input())
lst = list(map(int, input().split()))
lst.sort()
ans = 0
for i in range(n):
    ans += abs(lst[i] - lst[n // 2])
print(ans)
