# 导弹防御系统 https://www.acwing.com/problem/content/description/189/
# 暴搜

up, down = [0] * 55, [0] * 55

"""
    输入：当前位置索引、up 数组分了几组（放了几个防御系统）、down 数组分了几组（放了几个防御系统）
    输出：无输出，直接改 ans 为最小多少个防御系统
    """


def dfs(idx, upLen, downLen):
    global ans
    if upLen + downLen >= ans: return
    if idx == n:
        ans = min(ans, upLen + downLen)
        return
    k = 0
    while k < upLen and lst[idx] <= up[k]: k += 1
    if k == upLen:
        up[upLen] = lst[idx]
        dfs(idx + 1, upLen + 1, downLen)
    else:
        tmp = up[k]
        up[k] = lst[idx]
        dfs(idx + 1, upLen, downLen)
        up[k] = tmp
    k = 0
    while k < downLen and lst[idx] >= down[k]: k += 1
    if k == downLen:
        down[downLen] = lst[idx]
        dfs(idx + 1, upLen, downLen + 1)
    else:
        tmp = down[k]
        down[k] = lst[idx]
        dfs(idx + 1, upLen, downLen)
        down[k] = tmp


n = int(input())
while n:
    lst = list(map(int, input().split()))
    ans = n
    dfs(0, 0, 0)
    print(ans)
    n = int(input())
