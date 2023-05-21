# 原题链接：https://www.acwing.com/problem/content/4655/

a = [1189,841]

n = int(input()[1])

if n>0:
    for i in range(n):
        a.append(int(max(a[i],a[i+1])/2))

print(a[n])
print(a[n+1])