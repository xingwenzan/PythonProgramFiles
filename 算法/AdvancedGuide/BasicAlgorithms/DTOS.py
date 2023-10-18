# 起床困难综合症 https://www.acwing.com/problem/content/1000/

n, m = map(int, input().split())
op_lst = []
for i in range(n):
    tmp = list(input().split())
    op_lst.append([tmp[0], int(tmp[1])])


def OP(x, bit):
    for op, t in op_lst:
        if op == "AND":
            x &= (t >> bit) & 1
        elif op == "OR":
            x |= (t >> bit) & 1
        elif op == "XOR":
            x ^= (t >> bit) & 1
    return x


num, ans = 0, 0
for i in range(29, -1, -1):
    op1 = OP(1, i)
    op0 = OP(0, i)
    if num + (1 << i) <= m and op1 > op0:
        num += (1 << i)
        ans += (op1 << i)
    else:
        ans += (op0 << i)
print(ans)
