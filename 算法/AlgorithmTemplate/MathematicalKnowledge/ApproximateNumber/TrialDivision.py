# 试除法求约数 https://www.acwing.com/problem/content/871/

def approximation(x):
    ans = []
    num = 1
    while num <= x / num:
        if x % num == 0:
            ans.append(num)
            if num != x / num:
                ans.append(int(x / num))
        num += 1
    return sorted(ans)


n = int(input())
for i in range(n):
    x = int(input())
    out = approximation(x)
    print(" ".join(map(str, out)))
