# 高斯消元解异或线性方程组 https://www.acwing.com/problem/content/886/
# 异或 = 不进位加法

N = 110
equationSet = [[0.0 for _ in range(N)] for _ in range(N)]


def gauss(n):
    row = 0
    for col in range(n):
        tmp = row
        for i in range(row, n):
            if equationSet[i][col] == 1:
                tmp = i
                break
        if equationSet[tmp][col] == 0: continue
        equationSet[tmp], equationSet[row] = equationSet[row], equationSet[tmp]
        for r in range(row + 1, n):
            if equationSet[r][col] == 1:
                for c in range(col, n + 1):
                    equationSet[r][c] ^= equationSet[row][c]
        row += 1
    if row < n:
        for i in range(row, n):
            if equationSet[r][n] != 0:
                return 2
        return 1
    for r in range(n - 2, -1, -1):
        for c in range(r + 1, n):
            equationSet[r][n] ^= equationSet[r][c] & equationSet[c][n]
    return 0


n = int(input())
for i in range(n):
    tmp = list(map(int, input().split()))
    for j in range(n + 1):
        equationSet[i][j] = tmp[j]

judge = gauss(n)
if judge == 0:
    for i in range(n):
        print(equationSet[i][n])
elif judge == 1:
    print("Multiple sets of solutions")
else:
    print("No solution")
