# https://www.acwing.com/problem/content/4799/

n = int(input())
a = list(map(int,input().split()))
x = max(a)
value = [0]*(x+1)
score = [0]*(x+1)
for i in a:
    value[i] += i
for i in range(1,x+1,1):
    score[i] = max(score[i-1],score[max(0,i-2)]+value[i])
print(score[x])