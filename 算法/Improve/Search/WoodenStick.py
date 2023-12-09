# 木棒 https://www.acwing.com/problem/content/169/

# u 号大棍长度为 cur,下一个要放的小棍从 start 开始
def dfs(u, cur, start):
    if u * cur == L_sum: return True  # 必须用 dfs(1, 0, 0)
    # if u * L_one == L_sum: return True  # 同 y，使用 dfs(0, 0, 0) 即可
    if cur == L_one: return dfs(u + 1, 0, 0)

    i = start
    while i < n:
        if st[i] or cur + lst[i] > L_one:
            i += 1
            continue

        st[i] = True
        if dfs(u, cur + lst[i], i + 1): return True
        st[i] = False

        if cur == 0 or cur + lst[i] == L_one: return False

        while i + 1 < n and lst[i + 1] == lst[i]: i += 1
        i += 1

    return False


while True:
    n = int(input())
    if n == 0: break
    st = [False] * n
    lst = list(map(int, input().split()))
    lst.sort(reverse=True)
    L_sum, L_one = sum(lst), lst[0]

    while True:
        if L_sum % L_one == 0 and dfs(1, 0, 0): break
        # if L_sum % L_one == 0 and dfs(0, 0, 0): break
        L_one += 1
    print(L_one)
