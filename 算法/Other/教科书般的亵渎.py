# https://ac.nowcoder.com/acm/contest/66651/A

n = int(input())
lst = list(map(int, input().split()))
lst.sort()
cnt = 0
for i in range(len(lst) - 1):
    if lst[i + 1] - lst[i] <= 1:
        cnt += 1
    else:
        break
if cnt < n - 1:
    print("NO")
else:
    print("Yes")
