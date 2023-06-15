# 买书 https://www.acwing.com/problem/content/1025/

lst = [10, 20, 50, 100]
n = int(input())
f = [0] * (n + 10)
f[0] = 1
for i in range(4):
    for j in range(lst[i], n + 1, 1):
        f[j] += f[j - lst[i]]
print(f[n])
