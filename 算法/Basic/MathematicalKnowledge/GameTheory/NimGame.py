# Nim游戏 https://www.acwing.com/problem/content/893/
# a1^a2^……^an = 0 先手必败

n = int(input())
lst = map(int, input().split())
ans = 0
for i in lst:
    ans ^= i
if ans:
    print("Yes")
else:
    print("No")
