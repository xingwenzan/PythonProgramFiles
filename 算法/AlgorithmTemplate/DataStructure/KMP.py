# KMP字符串 https://www.acwing.com/problem/content/833/

N = int(input())
P = input()
M = int(input())
S = input()
nextSuperscript = [-1] * N

j = -1
for i in range(1, N, 1):
    while j != -1 and P[i] != P[j + 1]:
        j = nextSuperscript[j]
    if P[i] == P[j + 1]:
        j += 1
    nextSuperscript[i] = j

ans = []
j = -1
for i in range(M):
    while j != -1 and S[i] != P[j + 1]:
        j = nextSuperscript[j]
    if S[i] == P[j + 1]:
        j += 1
    if j == N - 1:
        ans.append(i-N+1)
        j = nextSuperscript[j]
print(" ".join(map(str, ans)))