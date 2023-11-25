# 单词接龙 https://www.acwing.com/problem/content/1119/

ans = 0
n = int(input())

g = [[0] * (n + 10) for _ in range(n + 10)]

word = []
used = [0] * n
for _ in range(n):
    word.append(input())
start = input()


def dfs(dragon, idx):
    global ans
    ans = max(ans, len(dragon))

    used[idx] += 1
    for i in range(n):
        if used[i] >= 2: continue
        if g[idx][i] == 0: continue
        dfs(dragon + word[i][g[idx][i]::], i)
    used[idx] -= 1
    return


# 预处理，处理两单词之间最短公共前后缀
for i in range(n):
    for j in range(n):
        a, b = word[i], word[j]
        for k in range(1, min(len(a), len(b))):
            if a[len(a) - k:len(a)] == b[0:k]:
                g[i][j] = k
                break

for i in range(n):
    if word[i][0] == start:
        dfs(word[i], i)

print(ans)
