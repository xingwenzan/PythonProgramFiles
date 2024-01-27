# 防晒 https://www.acwing.com/problem/content/112/

C, L = map(int, input().split())
cows = []
for i in range(C): cows.append(list(map(int, input().split())))
cows = sorted(cows, reverse=True)
spf = [0] * 1005
for i in range(L):
    a, b = map(int, input().split())
    spf[a] += b
ans = 0
for i in range(C):
    for j in range(1000, 0, -1):
        if spf[j] == 0: continue
        if cows[i][1] >= j >= cows[i][0]:
            ans += 1
            spf[j] -= 1
            break
print(ans)
