# https://www.acwing.com/problem/content/description/4647/

n = int(input())
a = list(map(int,input().split()))

ans = sum(a)**2
for i in a:
    ans -= i**2
ans /= 2
print(int(ans))