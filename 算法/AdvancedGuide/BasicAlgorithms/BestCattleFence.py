# 最佳牛围栏 https://www.acwing.com/problem/content/104/
# 详解 https://www.acwing.com/video/86/
n, m = map(int, input().split())
cow = [0] * (n + 10)
s = [0] * (n + 10)


def check(avg):
    # 前缀和
    for i in range(1, n + 1): s[i] = s[i - 1] + cow[i] - avg
    minv = 0
    i, j = 0, m
    while j <= n:
        minv = min(minv, s[i])
        if s[j] >= minv: return True

        i += 1
        j += 1
    return False


l, r = 0.0, 0.0
for i in range(1, n + 1):
    cow[i] = int(input())
    r = max(r, cow[i])
# 二分
while r - l >= 1e-5:
    mid = (l + r) / 2  # 一定要 /2，而不是 >>1
    if check(mid):
        l = mid
    else:
        r = mid
print(int(r * 1000))
