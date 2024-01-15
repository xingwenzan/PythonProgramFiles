# 动态中位数 https://www.acwing.com/problem/content/108/
# 开两个堆，一个是大根堆，一个是小根堆，然后小于中位数的都放在大根堆，大于中位数的都放在小根堆
# py 无大根堆，使用 *(-1) 的方法实现
import heapq
import math

N = int(input())
for i in range(N):
    m, n = map(int, input().split())
    print("{} {}".format(m, (n + 1) // 2))
    tmp = math.ceil(n / 10)
    lst = []
    for j in range(tmp):
        lst.extend(list(map(int, input().split())))
    h_up, h_down, out = [], [], []
    for j in range(n):
        heapq.heappush(h_up, lst[j])

        if len(h_down) != 0 and h_down[0] * (-1) > h_up[0]:
            a = heapq.heappop(h_down) * (-1)
            b = heapq.heappop(h_up)
            heapq.heappush(h_up, a), heapq.heappush(h_down, -1 * b)

        if len(h_up) > len(h_down) + 1:
            a = heapq.heappop(h_up)
            heapq.heappush(h_down, -1 * a)

        if (j & 1) == 0:
            out.append(h_up[0])
        if len(out) == 10 or j == n - 1:
            print(" ".join(map(str, out)))
            out = []
