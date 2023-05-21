# 求组合数 I https://www.acwing.com/problem/content/887/
# 组合数 C_a^b 四种方法区别在于适合的数据范围不同
# 本模板是先预处理出来所有情况，再直接选

N, mod = 2010, int(1e9 + 7)
Cab = [[0 for _ in range(N)] for _ in range(N)]


def init():
    for a in range(N):
        for b in range(a + 1):
            if b == 0:
                Cab[a][b] = 1
            else:
                Cab[a][b] = (Cab[a - 1][b] + Cab[a - 1][b - 1]) % mod
    return 0


n = int(input())
init()
for i in range(n):
    a, b = map(int, input().split())
    print(Cab[a][b])
