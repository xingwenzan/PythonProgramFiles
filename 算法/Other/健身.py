# https://www.acwing.com/problem/content/4797/

n = int(input())
sport = [0]*3
out = ["chest","biceps","back"]

time = list(map(int, input().split()))
for i in range(n):
    sport[i % 3] += time[i]
ans = max(sport)
for i in range(3):
    if ans==sport[i]:print(out[i])