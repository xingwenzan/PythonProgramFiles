# https://www.acwing.com/problem/content/description/4513/

n, L, S = map(int, input().split())
A = [0] * n
for i in range(n):
    A[i] = list(map(int, input().split()))
B = [0] * (S + 1)
num1 = 0
for i in range(S + 1):
    B[S - i] = list(map(int, input().split()))
    num1 += sum(B[S - i])
num2 = 0
ans = 0
for i in A:
    if L - i[0] >= S and L - i[1] >= S:
        for j in A:
            x = j[0] - i[0]
            y = j[1] - i[1]
            if x > S or y > S or x < 0 or y < 0: continue
            if B[x][y] == 1:
                num2 += 1
            else:
                num2 = 0
                break
        if num2 == num1:
            ans += 1
        num2 = 0
print(ans)
