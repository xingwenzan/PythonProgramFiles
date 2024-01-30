# 畜栏预定 https://www.acwing.com/problem/content/113/
import heapq

n = int(input())
cow = []
for i in range(n): cow.append(list(map(int, input().split())) + [i])
cow = sorted(cow)
heap = []
heapq.heapify(heap)
ans = [-1] * n

''' TLE
for i in range(n):
    if len(lst) == 0 or min(lst) >= cow[i][0]:
        lst.append(cow[i][1])
        ans[i] = [cow[i][2], len(lst)]
    else:
        tmp = lst.index(min(lst))
        lst[tmp] = cow[i][1]
        ans[i] = [cow[i][2], tmp + 1]'''

for i in range(n):
    if len(heap) == 0 or heap[0][0] >= cow[i][0]:
        heapq.heappush(heap, [cow[i][1], len(heap) + 1])
        ans[cow[i][2]] = len(heap)
    else:
        tmp = heapq.heappop(heap)
        heapq.heappush(heap, [cow[i][1], tmp[1]])
        ans[cow[i][2]] = tmp[1]
print(len(heap))
print(*ans, sep='\n')
