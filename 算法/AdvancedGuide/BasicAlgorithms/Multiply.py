# 倍增 天才ACM https://www.acwing.com/problem/content/111/
# 贪心 : 区间校检值 = sum((max-min)^2)
# 解析 https://www.acwing.com/solution/content/15458/
# 倍增 + 归并太麻烦了，不写了

lst, t = [], [0] * (int(5e5 + 5))


def get(l, r, num):
    tmp = lst[l:r]
    tmp.sort()
    i, j, s = 0, len(tmp), 0
    while i < j and i < num:
        s += (tmp[i] - tmp[j - 1]) ** 2
        i += 1
        j -= 1
    return s


def multiply1(n, m, t):
    """
    方法 1: 二分 —— TLE，死在数据 4/11
    :param n: lst 长度
    :param m: 限定最多对数
    :param t: 检验值最大值
    :return: lst 最少需要分成几段
    """
    ans = 0
    start = 0
    while start < n:
        # 二分
        l, r = start, n
        while l < r:
            mid = l + r + 1 >> 1
            if get(start, mid, m) <= t:
                l = mid
            else:
                r = mid - 1
        start = r
        ans += 1
    return ans


def multiply2(n, m, t):
    """
    方法 2: 倍增 —— 30807 ms
    :param n: lst 长度
    :param m: 限定最多对数
    :param t: 检验值最大值
    :return: lst 最少需要分成几段
    """
    start, end = 0, 0
    ans = 0
    while end < n:
        length = 1
        while length > 0:
            if end + length <= n and get(start, end + length, m) <= t:
                end += length
                length <<= 1
            else:
                length >>= 1
        start = end
        ans += 1
    return ans


if __name__ == '__main__':
    N = int(input())
    for i in range(N):
        n, m, t = map(int, input().split())
        lst = list(map(int, input().split()))
        print(multiply1(n, m, t))
        print(multiply2(n, m, t))
