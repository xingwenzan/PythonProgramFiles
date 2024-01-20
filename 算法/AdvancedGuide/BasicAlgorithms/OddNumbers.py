# 奇数码问题 https://www.acwing.com/problem/content/110/
# 局面可以转换的条件：逆序对（不考虑 0，即空格）数量的奇偶性不变
tmp = [0] * (501 * 501)


def merge_sort(lst, left, right):
    if left >= right: return 0
    mid = (left + right) // 2
    ans = merge_sort(lst, left, mid) + merge_sort(lst, mid + 1, right)

    i, j, k = left, mid + 1, 0
    while i <= mid and j <= right:
        if lst[i] <= lst[j]:
            tmp[k] = lst[i]
            k += 1
            i += 1
        else:
            tmp[k] = lst[j]
            k += 1
            j += 1
            ans += mid - i + 1
    while i <= mid:
        tmp[k] = lst[i]
        k += 1
        i += 1
    while j <= right:
        tmp[k] = lst[j]
        k += 1
        j += 1

    a, b = left, 0
    while a <= right:
        lst[a] = tmp[b]
        a += 1
        b += 1
    return ans


while True:
    try:
        n = int(input())
    except:
        break
    lst_a, lst_b = [0], [0]
    for i in range(n): lst_a.extend([x for x in map(int, input().split()) if x != 0])
    for i in range(n): lst_b.extend([x for x in map(int, input().split()) if x != 0])
    ans_a = merge_sort(lst_a, 0, n * n - 1)
    ans_b = merge_sort(lst_b, 0, n * n - 1)
    if (ans_a & 1) == (ans_b & 1):
        print("TAK")
    else:
        print("NIE")
