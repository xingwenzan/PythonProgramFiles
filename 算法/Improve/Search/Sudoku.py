# 数独 https://www.acwing.com/problem/content/168/
# 数据爆炸，TLE

s = ['0'] * 81
N, M = 9, 1 << 9
one_num, one_point = [0] * M, {}
row, col, cell = [M - 1] * N, [M - 1] * N, [[M - 1] * 3 for _ in range(3)]
# 预处理
# 获取所有状态的 1 的数量
for i in range(M):
    for j in range(N):
        one_num[i] += (i >> j) & 1
# 获取二进制数 1、10、100…… 中 1 的位置
for i in range(N):
    one_point[1 << i] = i


# 得到 x,y 位置上可以填的数有几个
def get(x, y): return row[x] & col[y] & cell[x // 3][y // 3]


def lowbit(x): return x & (-x)


# x 行 y 列位置填入/去掉 t (T:填入 F:去掉) t in [0,8]
def draw(x, y, t, st):
    if st:
        s[x * N + y] = str(t + 1)
    else:
        s[x * N + y] = '.'

    p = 1 << t
    if not st: p = -p
    row[x] -= p
    col[y] -= p
    cell[x // 3][y // 3] -= p
    return


# 初始化，顺便求出还有多少空要填
def init():
    for i in range(N): row[i] = col[i] = M - 1
    for i in range(3):
        for j in range(3):
            cell[i][j] = M - 1

    cnt = 0
    k = 0  # s 的下标
    for i in range(N):
        for j in range(N):
            if s[k] == '.':
                cnt += 1
            else:
                draw(i, j, int(s[k]) - 1, True)
            cnt += 1
    return cnt


def dfs(u):
    if u == 0: return True
    # 获取可以放入数字最少的位置
    minv, mx, my = 10, -1, -1
    k = 0
    for i in range(N):
        for j in range(N):
            if s[k] == '.':
                tmp = get(i, j)
                if one_num[tmp] < minv:
                    minv = one_num[tmp]
                    mx = i
                    my = j
            k += 1
    st = get(mx, my)
    while st:
        tmp = lowbit(st)

        num = one_point[tmp]
        draw(mx, my, num, True)
        if dfs(u - 1): return True
        draw(mx, my, num, False)

        st -= tmp

    return False


while True:
    tmp = input()
    if tmp == 'end': break
    s = list(tmp)

    cnt = init()
    dfs(cnt)
    print(''.join(s))
