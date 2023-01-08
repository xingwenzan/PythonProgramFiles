# https://www.acwing.com/problem/content/4794/

n = int(input())
first = [0,0]
second = [0,0]

for i in range(n):
    enter = list(map(int,input().split()))
    if enter[0]==1:
        first[0] += enter[1]
        first[1] += enter[2]
    elif enter[0]==2:
        second[0] += enter[1]
        second[1] += enter[2]
    else:print("请对正确的死刑犯处刑")

if first[0]>=first[1]:print("LIVE")
else:print("DEAD")

if second[0]>=second[1]:print("LIVE")
else:print("DEAD")