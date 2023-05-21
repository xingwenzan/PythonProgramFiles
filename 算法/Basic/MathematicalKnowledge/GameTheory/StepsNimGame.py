# 台阶-Nim游戏 https://www.acwing.com/problem/content/894/
# a1 ^ a3 ^ a5 ^ …… ^ an(n 是奇数) = 0   先手必败

n = int(input())
lst = list(map(int, input().split()))
ans = 0
for i in range(0, len(lst), 2):
    ans ^= lst[i]
if ans:
    print("Yes")
else:
    print("No")
