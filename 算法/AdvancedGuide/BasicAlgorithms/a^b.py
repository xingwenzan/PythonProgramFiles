# a^b https://www.acwing.com/problem/content/91/

a, b, c = map(int, input().split())
ans = 1 % c
while b:
    if b & 1: ans = ans * a % c
    a = a * a % c
    b >>= 1

print(ans)
