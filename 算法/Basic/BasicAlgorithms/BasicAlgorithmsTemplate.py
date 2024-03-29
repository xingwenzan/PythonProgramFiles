# 基础算法模板/快速调用


# 快速排序 O(nlogn) https://www.acwing.com/problem/content/787/
# https://www.acwing.com/activity/content/code/content/5198516/
def quick_sort(lst, l, r):  # 要查的数列，左边界，右边界
    if l >= r: return  # 左边界索引不小于右边界索引，无法进行，不搞
    i = l - 1  # i 指针指向列表的 l 号值
    j = r + 1  # j 指针指向列表的 r 号值
    x = lst[(l + r) >> 1]
    while i < j:
        i += 1
        while lst[i] < x: i += 1
        j -= 1
        while lst[j] > x: j -= 1
        if i < j: lst[i], lst[j] = lst[j], lst[i]
    quick_sort(lst, l, j)
    quick_sort(lst, j + 1, r)


# 快速选择 O(n) https://www.acwing.com/problem/content/description/788/
def quick_choose(lst, l, r, k):  # 要查的数列，左边界索引，右边界索引，第 k 个数
    if l == r:
        # print(lst[l])
        return lst[l]
    i = l - 1
    j = r + 1
    x = lst[(l + r + 1) >> 1]
    while i < j:
        i += 1
        while lst[i] < x: i += 1
        j -= 1
        while lst[j] > x: j -= 1
        if i < j: lst[i], lst[j] = lst[j], lst[i]

    if k <= i - l:
        return quick_choose(lst, l, i - 1, k)
    else:
        return quick_choose(lst, i, r, k - (i - l))


# 归并排序 O(nlogn) #https://www.acwing.com/problem/content/789/
def merge_sort(lst, l, r):
    if l >= r: return
    mid = l + r >> 1
    merge_sort(lst, l, mid)
    merge_sort(lst, mid + 1, r)

    i = l
    j = mid + 1
    tmp = [0] * (r - l + 1)
    k = 0

    while i <= mid and j <= r:
        if lst[i] <= lst[j]:
            tmp[k] = lst[i]
            i += 1
            k += 1
        else:
            tmp[k] = lst[j]
            j += 1
            k += 1
    while i <= mid:
        tmp[k] = lst[i]
        i += 1
        k += 1
    while j <= r:
        tmp[k] = lst[j]
        j += 1
        k += 1

    q = 0
    for p in range(l, r + 1, 1):
        lst[p] = tmp[q]
        q += 1


# 逆序对计数 - 归并排序应用 O(nlogn) https://www.acwing.com/problem/content/790/
def number_of_reversed_pairs(lst, l, r):
    if l >= r: return 0
    mid = l + r >> 1
    res = number_of_reversed_pairs(lst, l, mid) + number_of_reversed_pairs(lst, mid + 1, r)
    i, j, k = l, mid + 1, 0
    tmp = [0] * (r - l + 1)
    while i <= mid and j <= r:
        if lst[i] <= lst[j]:
            tmp[k] = lst[i]
            i += 1
            k += 1
        else:
            tmp[k] = lst[j]
            j += 1
            k += 1
            res += mid - i + 1
    while i <= mid:
        tmp[k] = lst[i]
        i += 1
        k += 1
    while j <= r:
        tmp[k] = lst[j]
        j += 1
        k += 1

    b = 0
    for a in range(l, r + 1, 1):
        lst[a] = tmp[b]
        a += 1
        b += 1

    return res


# 二分 O() https://www.acwing.com/problem/content/791/
# 整数二分
# 模板 1：左半边为 true（mid 在 x 左）
def dichotomize_left(lst, x):
    l, r = 0, len(lst) - 1
    while l < r:
        mid = l + r + 1 >> 1
        if lst[mid] <= x:
            l = mid
        else:
            r = mid - 1
    return r


# 二分 O() https://www.acwing.com/problem/content/791/
# 整数二分
# 模板 2：右半边为 true（mid 在 x 右）
def dichotomize_right(lst, x):
    l, r = 0, len(lst) - 1
    while l < r:
        mid = l + r >> 1
        if lst[mid] >= x:
            r = mid
        else:
            l = mid + 1
    return l


# 二分 O() https://www.acwing.com/activity/content/problem/content/824/
# 小数二分
def dichotomize_float(num, root, digit):  # digit 是保留的位数，root 是开几次方根
    l = -100
    r = 100
    while r - l > 10 ** (-digit - 2):
        mid = (l + r) / 2
        if mid ** root <= num:
            l = mid
        else:
            r = mid
    return "{:.6f}".format(l)  # round(l,digit)，round 不好使


# 高精度算法
# 判断大小
def ratio_str_HighPrecisionAlgorithm(a, b):
    if len(a) != len(b): return len(a) > len(b)
    for i in range(len(a)):
        if a[i] != b[i]:
            return int(a[i]) > int(b[i])
    return True


# 高精度算法
# 加法 O() https://www.acwing.com/problem/content/793/
def high_precision_addition(a, b):
    if len(a) < len(b): return high_precision_addition(b, a)
    a = a[::-1]
    b = b[::-1]
    c = [0] * (len(a) + 1)
    t = 0
    for i in range(len(b)):
        t += int(a[i]) + int(b[i])
        c[i] = str(t % 10)
        t //= 10
    if len(a) > len(b):
        for i in range(len(b), len(a)):
            t += int(a[i])
            c[i] = str(t % 10)
            t //= 10
    c[len(a)] = str(t)
    # c.reverse()
    ans = ''.join(reversed(c))
    return int(ans)


# 高精度算法
# 减法 O() https://www.acwing.com/problem/content/794/
def high_precision_subtraction(a, b):
    if not ratio_str_HighPrecisionAlgorithm(a, b):
        return -high_precision_subtraction(b, a)
    a = a[::-1]
    b = b[::-1]
    c = [0] * (len(a))
    t = 0
    for i in range(len(b)):
        if int(a[i]) - t >= int(b[i]):
            c[i] = str(int(a[i]) - int(b[i]) - t)
            t = 0
        else:
            c[i] = str(int(a[i]) - int(b[i]) - t + 10)
            t = 1
    if len(a) > len(b):
        for i in range(len(b), len(a)):
            if int(a[i]) - t >= 0:
                c[i] = str(int(a[i]) - t)
                t = 0
            else:
                c[i] = str(int(a[i]) - t + 10)
                t = 1
    # c.reverse()
    ans = ''.join(reversed(c))
    return int(ans)


# 高精度算法
# 乘法 O() https://www.acwing.com/problem/content/795/
# (高精度*高精度 or 高精度*低精度)
def high_precision_multiplication(a, b):
    if len(a) < len(b): return high_precision_multiplication(b, a)
    a = a[::-1]
    b = b[::-1]
    c = ["0"] * (len(a) + len(b))
    for i in range(len(b)):
        t = 0
        for j in range(len(a)):
            t += int(a[j]) * int(b[i]) + int(c[i + j])
            c[i + j] = str(t % 10)
            t //= 10
        t += int(c[i + len(a)])
        c[i + len(a)] = str(t % 10)
    # c.reverse()
    ans = ''.join(reversed(c))
    return int(ans)


# 高精度算法
# 除法 O() https://www.acwing.com/problem/content/796/
# (高精度/低精度)
def high_precision_division_low(a, b):
    # if len(a) < len(b): return high_precision_division(b,a)
    b = int(b)
    c = ["0"] * (len(a))
    t = 0
    for i in range(len(a)):
        c[i] = str((int(a[i]) + t * 10) // b)
        t = (int(a[i]) + t * 10) % b
    ans = ''.join(c)
    return int(ans), t


# 高精度算法
# 除法 O() https://www.acwing.com/problem/content/796/
# (高精度/高精度) (没通过)
def high_precision_division_high(a, b):
    c = ["0"] * (len(a))
    k = ""
    for i in range(len(a)):
        k += a[i]
        if ratio_str_HighPrecisionAlgorithm(k, b):
            for j in range(9, 0, -1):
                tmp = str(high_precision_multiplication(b, str(j)))
                if ratio_str_HighPrecisionAlgorithm(k, tmp):
                    c[i] = str(j)
                    k = str(high_precision_subtraction(k, tmp))
                    break
                else:
                    continue
        else:
            continue
    ans = ''.join(c)
    return int(ans), k


# 前缀和
# 一维前缀和 O(n) https://www.acwing.com/problem/content/797/
def prefix_sum_1D(lst):
    s = [0]
    t = 0
    for i in range(len(lst)):
        t += lst[i]
        s.append(t)
    return s


# 前缀和
# 二维前缀和 O() https://www.acwing.com/problem/content/798/
def prefix_sum_2D(lst, height, width):
    s = [[0 for i in range(width + 1)] for i in range(height + 1)]
    for i in range(1, height + 1):
        for j in range(1, width + 1):
            s[i][j] = s[i - 1][j] + s[i][j - 1] - s[i - 1][j - 1] + lst[i - 1][j - 1]
    return s


# 差分
# 一维差分 O(n) https://www.acwing.com/problem/content/799/
def finite_difference_1D(lst, l, r, n):
    lst[l] += n
    lst[r + 1] -= n
    return lst


# 差分
# 二维差分 O(n) https://www.acwing.com/problem/content/800/
def finite_difference_2D(lst, x1, y1, x2, y2, n):
    lst[x1][y1] += n
    lst[x1][y2 + 1] -= n
    lst[x2 + 1][y1] -= n
    lst[x2 + 1][y2 + 1] += n
    return lst


# 位运算 https://www.acwing.com/problem/content/803/
# 原码 x=10101…… ; 反码 ~x=01010…… ; 补码 -x=~x+1 ;
# https://www.acwing.com/video/246/
def lowbit(x):  # 取最后(右)一位 1 及之后的所有位(0)
    return x & (-x)


# 离散化 O() https://www.acwing.com/problem/content/804/
# 本体: 排序 + 去重
# 查找: 二分
# 应用: 前缀和（本题）
def discretization(lst):  # 离散化本体
    # 排序部分   最终还是 python 自带的排序快一点   循环去重比 set 快
    # quick_sort(lst, 0, len(lst) - 1) # 3300ms 3740ms
    # merge_sort(lst,0,len(lst)-1) # 3267ms 3316ms
    lst.sort()  # 2977ms 3073ms

    # 去重部分
    out = []
    for i in range(len(lst)):
        if (i == 0 or (i != 0 and lst[i] != lst[i - 1])):
            out.append(lst[i])
    # out = list(set(lst))

    return out


# 区间合并 O() https://www.acwing.com/problem/content/805/
def interval_merge(lst):
    lst.sort(key=lambda x: (x[0], x[1]))
    out = [lst[0]]
    for x in lst:
        if x[0] <= out[-1][1]:
            if x[1] > out[-1][1]:
                out[-1][1] = x[1]
            else:
                continue
        else:
            out.append(x)
    return out
