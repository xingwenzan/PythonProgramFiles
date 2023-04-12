# 容斥原理 能被整除的数 https://www.acwing.com/problem/content/892/

n, m = map(int, input().split())
pi = list(map(int, input().split()))

ans = 0
for i in range(1, 1 << m):
    t, s = 1, 0  # t: s 个 pi 的乘积; s: 相乘 pi 的个数，根据其奇偶性判断加减
    for j in range(m):
        if i >> j & 1:
            t *= pi[j]
            if t > n:
                t = -1
                break
            else:
                s += 1
    if t != -1:
        if s % 2:
            ans += n // t
        else:
            ans -= n // t

print(ans)
