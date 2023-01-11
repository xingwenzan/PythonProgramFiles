# https://www.acwing.com/problem/content/4512/

n = int(input())
a = list(map(int,input().split()))

avg = sum(a)/len(a)
d = 0
for i in a:
    d += (i-avg)**2
d /= n
d = d**0.5
for i in a:
    print((i-avg)/d)
