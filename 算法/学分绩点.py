# 原题链接：https://www.acwing.com/problem/content/description/3446/

def scoreToGPA(x): # 定义分数转绩点函数
    if x >= 90:
        return 4.0
    elif x >= 85:
        return 3.7
    elif x >= 82:
        return 3.3
    elif x >= 78:
        return 3.0
    elif x >= 75:
        return 2.7
    elif x >= 72:
        return 2.3
    elif x >= 68:
        return 2.0
    elif x >= 64:
        return 1.5
    elif x >= 60:
        return 1.0
    else:
        return 0

num = int(input())
classCredits = list(map(int, input().split())) # 学分
classScores = list(map(int,input().split())) # 得分

creditGPA = 0 # 学分绩点

for x in range(num):
    creditGPA += classCredits[x] * scoreToGPA(classScores[x])

ans = creditGPA / sum(classCredits)

print("%.2lf" % ans)