# 区间分组 https://www.acwing.com/problem/content/908/

import heapq as hq

n = int(input())
ranges = []

for i in range(n):
    l, r = map(int, input().split())
    ranges.append([l, r])

ranges.sort(key=lambda x: x[0])
h = []

for l, r in ranges:
    if len(h) == 0 or l <= h[0]:
        hq.heappush(h, r)
    else:
        hq.heappop(h)
        hq.heappush(h, r)
print(len(h))
