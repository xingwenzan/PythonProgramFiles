# 环形石子合并 https://www.acwing.com/problem/content/1070/

INF = float('inf')
N = 200 * 2 + 10  # 因为是环形，故开双倍大小的数组
f_max = [[-INF for _ in range(N)] for _ in range(N)]
f_min = [[INF for _ in range(N)] for _ in range(N)]


def prefixSum(lst, length):
    ans = [0]
    for i in range(length):
        ans.append(ans[i] + lst[i])
    return ans


def dp(lst, num):
    lst.extend(lst)
    s = prefixSum(lst, 2 * num)
    for length in range(1, num + 1):
        l = 1
        while l + length - 1 <= num * 2:
            r = l + length - 1
            if l == r:
                f_max[l][r] = f_min[l][r] = 0
            else:
                for k in range(l, r):
                    f_max[l][r] = max(f_max[l][r], f_max[l][k] + f_max[k + 1][r] + s[r] - s[l - 1])
                    f_min[l][r] = min(f_min[l][r], f_min[l][k] + f_min[k + 1][r] + s[r] - s[l - 1])
            l += 1
    M, m = -INF, INF
    for i in range(1, num + 1):
        M = max(M, f_max[i][i + num - 1])
        m = min(m, f_min[i][i + num - 1])
    return M, m


n = int(input())
w = list(map(int, input().split()))
Mw, mw = dp(w, n)
print(mw)
print(Mw)
