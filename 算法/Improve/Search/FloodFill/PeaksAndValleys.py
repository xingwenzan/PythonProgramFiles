# 山峰和山谷 https://www.acwing.com/problem/content/1108/

n = int(input())
lst = []

st = [[False] * (n + 10) for _ in range(n + 10)]  # 是否走过
q = [[0, 0] for _ in range((n + 10) * (n + 10))]  # bfs 队列
peaks, valleys = 0, 0  # 山峰数、山谷数

for _ in range(n):
    lst.append(list(map(int, input().split())))


def bfs(x, y):
    has_high, has_low = False, False

    hh, tt = 0, 0
    q[0] = [x, y]
    while hh <= tt:
        tmp = q[hh]
        hh += 1
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == 0 and j == 0: continue
                x, y = tmp[0] + i, tmp[1] + j
                if x < 0 or y < 0 or x >= n or y >= n: continue
                if lst[x][y] != lst[tmp[0]][tmp[1]]:
                    if lst[x][y] > lst[tmp[0]][tmp[1]]:
                        has_high = True
                    else:
                        has_low = True
                elif not st[x][y]:
                    tt += 1
                    q[tt] = [x, y]
                    st[x][y] = True

    return (has_high, has_low)


for i in range(n):
    for j in range(n):
        if not st[i][j]:
            has_high, has_low = bfs(i, j)
            if not has_high: peaks += 1
            if not has_low: valleys += 1
print("{} {}".format(peaks, valleys))
