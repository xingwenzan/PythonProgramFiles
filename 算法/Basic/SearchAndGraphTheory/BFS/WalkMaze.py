# 走迷宫 https://www.acwing.com/problem/content/846/

from queue import Queue


def bfs(mazeMap, height, width):
    nextHeightNum = [-1, 0, 1, 0]
    nextWidthNum = [0, 1, 0, -1]
    schedule = [[-1 for i in range(width)] for i in range(height)]
    schedule[0][0] = 0
    point = Queue(maxsize=0)
    point.put((0, 0))
    while not point.empty():
        currentPoint = point.get()
        for i in range(4):
            newHeightNum = currentPoint[0] + nextHeightNum[i]
            newWidthNum = currentPoint[1] + nextWidthNum[i]
            if newHeightNum >= 0 and newHeightNum < height and newWidthNum >= 0 and newWidthNum < width and mazeMap[newHeightNum][newWidthNum] == 0 and schedule[newHeightNum][newWidthNum] == -1:
                schedule[newHeightNum][newWidthNum] = schedule[currentPoint[0]][currentPoint[1]] + 1
                point.put((newHeightNum, newWidthNum))
    return schedule[height - 1][width - 1]


n, m = map(int, input().split())
mazeMap = []
for i in range(n):
    mazeMap.append(list(map(int, input().split())))
print(bfs(mazeMap, n, m))
