# https://www.acwing.com/problem/content/4731/

a,b = map(int,input().split())
ans = 1
for i in range(b):
    ans *= a
    if ans>10**9:
        print(-1)
        break
    if i == b-1:
        print(ans)