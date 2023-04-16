# Floyd求最短路 https://www.acwing.com/problem/content/856/

N = 210
inf = 10 ** 9 + 10

distance = [[inf for i in range(N)] for i in range(N)]


def init():
    for i in range(N):
        for j in range(N):
            if i == j: distance[i][j] = 0


def add(father, son, lenght):
    distance[father][son] = min(lenght, distance[father][son])


def find(father, son):
    return distance[father][son]


def floyd(num):
    for k in range(1, num + 1):
        for i in range(1, num + 1):
            for j in range(1, num + 1):
                distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])


init()
n, m, q = map(int, input().split())
for i in range(m):
    start, end, long = map(int, input().split())
    add(start, end, long)

floyd(n)

for i in range(q):
    start, end = map(int, input().split())
    ans = find(start, end)
    if ans > 10 ** 9 / 2:
        print('impossible')
    else:
        print(ans)
