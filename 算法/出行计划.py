# https://www.acwing.com/problem/content/4458/

n,m,k = list(map(int,input().split()))
ans = [0]*(10**5+10)*3

for i in range(n):
    t,c = map(int,input().split())
    ans[max(t-c+1,0)]+=1
    ans[max(t+1,0)]-=1
for i in range(1,(10**5+10)*2,1):
    ans[i] += ans[i-1]
for i in range(m):
    q = int(input())
    print(ans[q+k])
