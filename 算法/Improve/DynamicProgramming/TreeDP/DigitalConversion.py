# 数字转换 https://www.acwing.com/problem/content/1077/
# 树的最长路径的应用
# 树的建立   反向枚举，枚举 i 是哪些数的约数，而非枚举 i 的约数有哪些，以减小复杂度
# 树的遍历   一个约数和可以对应多个数，但一个数只会对应一个约数和，且约数和小于每一个对应它的数，故可建立以约数和为父的有向图，从小到大无重复的遍历，获取最长次长路径后相加比较

N = int(1e4 + 10) * 5
h, e, ne, idx = [-1] * N, [0] * (2 * N), [0] * (2 * N), 0
ans = 0
st = [False] * N  # 是否遍历过
sum = [0] * N  # sum[i] 为 i 对应的约数和


def dfs(u):
    global ans
    st[u] = True
    dist = 0  # 表示从当前点往下走的最大长度
    d1, d2 = 0, 0  # 最大长度和次大长度
    i = h[u]
    while i != -1:
        son = e[i]
        if not st[son]:
            d = dfs(son) + 1
            dist = max(dist, d)
            if d >= d1:
                d2, d1 = d1, d
            elif d > d2:
                d2 = d
        i = ne[i]
    ans = max(ans, d1 + d2)
    return dist


def add(father, son):
    global idx
    e[idx] = son
    ne[idx] = h[father]
    h[father] = idx
    idx += 1
    return


n = int(input())
for i in range(1, n + 1):
    j = 2
    while i * j <= n:
        sum[i * j] += i
        j += 1

for i in range(2, n + 1):  # sum[1] = 0，本题数据无 0，故无须遍历 1
    if sum[i] < i: add(sum[i], i)

for i in range(1, n + 1):
    if not st[i]:
        dfs(i)

print(ans)
