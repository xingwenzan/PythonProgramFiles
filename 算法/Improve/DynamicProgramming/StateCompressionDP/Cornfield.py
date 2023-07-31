# 玉米田 https://www.acwing.com/problem/content/329/

N, M, mod = 14, 1 << 12, int(1e8)
f = [[0 for _ in range(M)] for _ in range(N)]
w = [0] * N  # 田
state = []  # 所有合法状态
head = {}  # 各状态可以转移到的状态（a 可转移到 b，b 亦可转移到 a）


def check(x):
    return ((x << 1) & x) == 0


n, m = map(int, input().split())
# 获取田地的二进制表示状态
# （题中 1 可种 0 不可种，下面则相反，不可种的地方种了 & 后就不为 0，方便 DP 中的判断）
for i in range(1, n + 1):
    lst = list(map(int, input().split()))
    for j in range(m):
        w[i] += (1 - lst[j]) * (1 << j)
# 获取合法状态
for i in range(1 << m):
    if check(i):
        state.append(i)
# 获取可（被）转移状态
for i in state:
    for j in state:
        if (i & j) == 0:
            if i in head:
                head[i].append(j)
            else:
                head[i] = [j]
# DP
f[0][0] = 1
for i in range(1, n + 2):
    for j in state:
        if (j & w[i]) == 0:
            for k in head[j]:
                f[i][j] = (f[i][j] + f[i - 1][k]) % mod
print(f[n + 1][0])
