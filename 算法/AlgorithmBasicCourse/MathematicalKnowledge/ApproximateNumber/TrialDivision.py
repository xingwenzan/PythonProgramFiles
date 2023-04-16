# 试除法求约数 https://www.acwing.com/problem/content/871/

import heapq


def approximationI(x): # 966ms
    ans = []
    num = 1
    while num <= x / num:
        if x % num == 0:
            ans.append(num)
            if num != x / num:
                ans.append(int(x / num))
        num += 1
    return sorted(ans)


def approximationII(x): # 1157ms
    heap = []
    num = 1
    while num <= x / num:
        if x % num == 0:
            heapq.heappush(heap, num)
            if num != x / num:
                heapq.heappush(heap, int(x / num))
        num += 1
    ans = []
    for i in range(len(heap)):
        ans.append(heapq.heappop(heap))
    return ans


n = int(input())
for i in range(n):
    x = int(input())
    outI = approximationI(x)
    outII = approximationII(x)
    print(" ".join(map(str, outI)))
    print(" ".join(map(str, outII)))
