# 字符串哈希 https://www.acwing.com/problem/content/843/
# 字符串前缀哈希法
# 假定人品够好，没有冲突（一般取 131或13331进制，用 2**64 取模）

n, m = map(int, input().split())
lst = input()

hexadecimal = 131
hexadecimalPower = [1] * (n + 1)
stringValue = [0] * (n + 1)

for i in range(1, n + 1, 1):
    hexadecimalPower[i] = (hexadecimalPower[i - 1] * hexadecimal) % (1 << 64)
    stringValue[i] = (stringValue[i - 1] * hexadecimal + ord(lst[i - 1])) % (1 << 64)


def stringToHashValue(l, r):
    return (stringValue[r] - stringValue[l - 1] * hexadecimalPower[r - l + 1]) % (1 << 64)


for i in range(m):
    l1, r1, l2, r2 = map(int, input().split())
    if stringToHashValue(l1, r1) == stringToHashValue(l2, r2):
        print("Yes")
    else:
        print("No")
