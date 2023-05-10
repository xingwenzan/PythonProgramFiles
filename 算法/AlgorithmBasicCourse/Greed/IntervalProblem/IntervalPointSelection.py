# 区间选点 https://www.acwing.com/problem/content/907/

lst = []
n = int(input())
for i in range(n):
    lst.append(list(map(int, input().split())))
# sorted(lst, key=lambda x: x[1])   # 不好使，没替换
lst.sort(key=lambda x: x[1])
tmp = lst[0][1]
ans = 1
for i in lst:
    if i[0] > tmp:
        ans += 1
        tmp = i[1]
print(ans)
