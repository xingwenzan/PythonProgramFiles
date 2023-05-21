# 八数码 https://www.acwing.com/problem/content/847/

from queue import Queue

end = "12345678x"
stepCount = {}
horizontalChange = [0, 1, 0, -1]
verticalChange = [-1, 0, 1, 0]
pendingSituation = Queue(maxsize=0)


def bfs(start):
    start = "".join(list(start.split()))
    stepCount[start] = 0
    pendingSituation.put(start)
    while not pendingSituation.empty():
        currentSituation = pendingSituation.get()
        if currentSituation == end:
            return stepCount[currentSituation]
        currentDistance = stepCount[currentSituation]
        xPoint = currentSituation.find("x")
        xRow = xPoint // 3
        xCol = xPoint % 3
        for i in range(4):
            nextRow = xRow + verticalChange[i]
            nextCol = xCol + horizontalChange[i]
            if 0 <= nextCol < 3 and 0 <= nextRow < 3:
                nextPoint = nextRow * 3 + nextCol
                tmp = ""
                for j in range(9):
                    if j == xPoint:
                        tmp += currentSituation[nextPoint]
                    elif j == nextPoint:
                        tmp += currentSituation[xPoint]
                    else:
                        tmp += currentSituation[j]
                if not (tmp in stepCount.keys()):
                    stepCount[tmp] = currentDistance + 1
                    pendingSituation.put(tmp)
    return -1


start = input()
print(bfs(start))
