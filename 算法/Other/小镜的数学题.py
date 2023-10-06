# https://ac.nowcoder.com/acm/contest/66651/L

n = int(input())
l = len(bin(n)) - 2
print(1 << l)
