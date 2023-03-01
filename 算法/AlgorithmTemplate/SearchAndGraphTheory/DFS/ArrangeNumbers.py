# 排列数字 https://www.acwing.com/problem/content/844/

N = 10
state = [False] * N
lst = [0] * N


def dfs(currentNum, upperLimitNum):
    if currentNum == upperLimitNum+1:
        ans = []
        for i in range(1, upperLimitNum + 1, 1):
            ans.append(lst[i])
        print(" ".join(map(str, ans)))
    for i in range(1, upperLimitNum + 1, 1):
        if not state[i]:
            lst[currentNum] = i
            state[i] = True
            dfs(currentNum + 1, upperLimitNum)
            state[i] = False


n = int(input())
dfs(1, n)
