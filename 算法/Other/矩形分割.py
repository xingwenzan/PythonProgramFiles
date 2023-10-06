# https://ac.nowcoder.com/acm/contest/66651/K

n, m = map(int, input().split())
if m > n: n, m = m, n
ans = 0
while n % m:
    ans += (n // m) * m
    n, m = m, n % m
ans += (n // m) * m
print(ans)
