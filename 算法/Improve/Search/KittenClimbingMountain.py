# 小猫爬山 https://www.acwing.com/problem/content/167/

n, w = map(int, input().split())
lst = []
for _ in range(n):
    lst.append(int(input()))
lst.sort(reverse=True)

ans = n  # 初始默认一只猫一车
s = [0] * n  # 单量车载重


# 当前上车 u 只猫，用车 k 量
def dfs(u, k):
    global ans
    if k >= ans: return
    if u == n:
        ans = k
        return
    for i in range(k):
        if s[i] + lst[u] <= w:
            s[i] += lst[u]
            dfs(u + 1, k)
            s[i] -= lst[u]
    # 单开一辆车
    s[k] = lst[u]
    dfs(u + 1, k + 1)
    s[k] = 0
    return


dfs(0, 0)
print(ans)
