# n-皇后问题 https://www.acwing.com/problem/content/845/

n = int(input())
N = 2 * n
col, diagonal, reverseDiagonal = [False] * N, [False] * N, [False] * N
chessBoard = [["." for i in range(n)] for i in range(n)]


def dfs(rowNum, allNum):  # allNum 代表总行数、总列数、总最大棋子数
    if rowNum >= allNum:
        for i in range(n):
            print(" ".join(map(str, chessBoard[i])))
        print()
        return
    for colNum in range(allNum):
        if not (col[colNum] or diagonal[rowNum - colNum + allNum] or reverseDiagonal[rowNum + colNum]):
            chessBoard[rowNum][colNum] = "Q"
            col[colNum] = diagonal[rowNum - colNum + allNum] = reverseDiagonal[rowNum + colNum] = True
            dfs(rowNum + 1, allNum)
            chessBoard[rowNum][colNum] = "."
            col[colNum] = diagonal[rowNum - colNum + allNum] = reverseDiagonal[rowNum + colNum] = False


dfs(0, n)
