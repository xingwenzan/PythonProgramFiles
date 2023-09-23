# 运输小猫 https://www.acwing.com/problem/content/305/
# 视频 https://www.acwing.com/video/439/

f = [[float('inf')] * 100010 for _ in range(110)]
for i in range(110): f[i][0] = 0
q = [0] * 100010


def prefixSum(lst):
    ans = [0]
    for i in range(len(lst)):
        ans.append(ans[i] + lst[i])
    return ans


n, m, p = map(int, input().split())
d = [0]
d.extend(list(map(int, input().split())))
d = prefixSum(d)
a = []
for _ in range(m):
    h, t = map(int, input().split())
    a.append(t - d[h])
a.sort()
s = prefixSum(a)
a = [0] + a


def y(j, k):
    return f[j - 1][k] + s[k]


# DP
for j in range(1, p + 1):
    hh = tt = 0
    q[0] = 0
    for i in range(1, m + 1):
        while hh < tt and (y(j, q[hh + 1]) - y(j, q[hh])) <= a[i] * (q[hh + 1] - q[hh]): hh += 1
        k = q[hh]
        f[j][i] = f[j - 1][k] + a[i] * (i - k) - s[i] + s[k]
        while hh < tt and (y(j, q[tt]) - y(j, q[tt - 1])) * (i - q[tt]) >= (y(j, i) - y(j, q[tt])) * (
                q[tt] - q[tt - 1]): tt -= 1
        tt += 1
        q[tt] = i
print(f[p][m])
