# 股票买卖 II https://www.acwing.com/problem/content/1057/
# 解析 https://www.acwing.com/solution/content/38975/

n = int(input())
lst = list(map(int, input().split()))
ans = 0
for i in range(1, n):
    if lst[i] > lst[i - 1]: ans += lst[i] - lst[i - 1]
print(ans)
