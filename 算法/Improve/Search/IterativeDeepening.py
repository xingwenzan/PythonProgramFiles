# 迭代加深 加成序列 https://www.acwing.com/problem/content/172/

N = 110
lst = [0] * N
lst[0] = 1

'''
u:当前所在层数
m:限定最大层数
'''


def dfs(u, m):
    global n
    if u == m: return lst[m - 1] == n
    st = [False] * N
    for i in range(u - 1, -1, -1):
        for j in range(i, -1, -1):
            s = lst[i] + lst[j]
            if s > n or s < lst[u - 1] or st[s] != False: continue
            st[s] = True
            lst[u] = s
            if dfs(u + 1, m): return True
    return False


while True:
    n = int(input())
    if n == 0: break
    k = 1
    while not dfs(1, k): k += 1
    for i in range(k): print(lst[i], end=" ")
    print()
