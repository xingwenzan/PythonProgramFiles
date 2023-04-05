# 高斯消元解线性方程组 https://www.acwing.com/problem/content/885/

N = 110
equationSet = [[0.0 for _ in range(N)] for _ in range(N)]
eps = 1e-8


def gauss(n):
    row = 0
    for col in range(n):
        tmp = row
        for i in range(row + 1, n):
            if abs(equationSet[i][col]) > abs(equationSet[tmp][col]):
                tmp = i
        if abs(equationSet[tmp][col]) < eps: continue
        equationSet[row], equationSet[tmp] = equationSet[tmp], equationSet[row]
        '''
        for i in range(col, n + 1):
            equationSet[row][i], equationSet[tmp][i] = equationSet[tmp][i], equationSet[row][i]
        '''
        for i in range(n, col - 1, -1):
            equationSet[row][i] /= equationSet[row][col]
        for r in range(row + 1, n):
            if abs(equationSet[r][col]) > eps:
                for c in range(n, col - 1, -1):
                    equationSet[r][c] -= equationSet[r][col] * equationSet[row][c]
        row += 1
    if row < n:
        for i in range(row, n):
            if abs(equationSet[i][n]) > eps: return 2  # 无解
        return 1  # 无数解
    for r in range(n - 2, -1, -1):
        for c in range(r + 1, n):
            equationSet[r][n] -= equationSet[r][c] * equationSet[c][n]
    return 0  # 唯一解


n = int(input())
for i in range(n):
    tmp = list(map(float, input().split()))
    for j in range(n + 1):
        equationSet[i][j] = tmp[j]

judge = gauss(n)
if judge == 0:  # 唯一解
    for i in range(n):
        if abs(equationSet[i][n]) < eps: equationSet[i][n] = 0
        print("{:.2f}".format(equationSet[i][n]))
elif judge == 1:  # 无数解
    print("Infinite group solutions")
elif judge == 2:  # 无解
    print("No solution")
