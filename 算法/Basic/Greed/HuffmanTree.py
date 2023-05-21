# 合并果子 https://www.acwing.com/problem/content/150/

import heapq as hq

n = int(input())
lst = list(map(int, input().split()))
ans = 0
hq.heapify(lst)
while len(lst) > 1:
    a = hq.heappop(lst)
    b = hq.heappop(lst)
    ans += (a + b)
    hq.heappush(lst, a + b)

print(ans)
