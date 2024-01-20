# 双向DFS 送礼物 https://www.acwing.com/problem/content/173/
# dfs 里 u-当前算到第u个数，s-到第u个数可能出现的重量

w, n = map(int, input().split())
k = n // 2
g, weight = [], []
cnt = 0
for i in range(n): g.append(int(input()))
g = sorted(g, reverse=True)
ans = 0


# 前半部分遍历
def dfs1(u, s):
    if u == k:
        weight.append(s)
        return
    if s + g[u] <= w: dfs1(u + 1, s + g[u])
    dfs1(u + 1, s)
    return


def dfs2(u, s):
    global ans
    if u == n:
        l, r = 0, cnt - 1
        while l < r:
            mid = (l + r + 1) // 2
            if weight[mid] + s <= w:
                l = mid
            else:
                r = mid - 1
        if s + weight[l] <= w: ans = max(ans, s + weight[l])
        return
    if s + g[u] <= w: dfs2(u + 1, s + g[u])
    dfs2(u + 1, s)
    return


dfs1(0, 0)
weight = sorted(list(set(weight)))
cnt = len(weight)
dfs2(k, 0)
print(ans)
