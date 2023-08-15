# 能量项链 https://www.acwing.com/problem/content/322/

# INF = float('inf')
N = 100 * 2 + 10  # 因为是环形，故开双倍大小的数组
f = [[0 for _ in range(N)] for _ in range(N)]

n = int(input())
lst = list(map(int, input().split()))
w = [0]
lst.extend(lst)
w.extend(lst)

for length in range(3, n + 2):
    l = 1
    while l + length - 1 <= 2 * n:
        r = l + length - 1
        for k in range(l + 1, r): f[l][r] = max(f[l][r], f[l][k] + f[k][r] + w[l] * w[k] * w[r])
        l += 1

ans = 0
for i in range(1, n + 1): ans = max(ans, f[i][i + n])
print(ans)
