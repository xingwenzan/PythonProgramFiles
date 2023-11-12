# 分形之城 https://www.acwing.com/problem/content/100/
# 详解 https://www.acwing.com/solution/content/16524/


# n 级别   m n级图下的编号
def get_xy(n, m):
    if n == 0: return (0, 0)
    cnt = 1 << (2 * (n - 1))  # n-1 级图点数
    len = 1 << (n - 1)  # n-1 级图边长
    z = m // cnt  # 点所在 n-1 级图在 n 级图的位置编号
    x, y = get_xy(n - 1, m % cnt)
    if z == 0: return (y, x)
    if z == 1: return (x, y + len)
    if z == 2: return (x + len, y + len)
    return (2 * len - y - 1, len - x - 1)


num = int(input())
for _ in range(num):
    n, a, b = map(int, input().split())
    xa, ya = get_xy(n, a - 1)
    xb, yb = get_xy(n, b - 1)
    ans = ((xa - xb) ** 2 + (ya - yb) ** 2) ** 0.5 * 10
    print(round(ans))
