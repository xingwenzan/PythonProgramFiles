# 区间覆盖 https://www.acwing.com/problem/content/909/

ranges = []


def cover(start, end):
    ans = 0
    length = len(ranges)
    for i in range(length):
        j = i
        mid = -2e9
        while j < length and ranges[j][0] <= start:
            mid = max(mid, ranges[j][1])
            j += 1
        if mid < start:
            return -1
        ans += 1
        start = mid
        if mid >= end:
            return ans
        i = j - 1
    if start < end:
        return -1


st, ed = map(int, input().split())
n = int(input())
for i in range(n):
    ranges.append(list(map(int, input().split())))
ranges.sort(key=lambda x: x[0])
print(cover(st, ed))
