# 电影 https://www.acwing.com/problem/content/105/

n = int(input())
p = list(map(int, input().split()))  # 人
m = int(input())
b = list(map(int, input().split()))  # 语音
c = list(map(int, input().split()))  # 字幕
lst = []

cnt = {}
for i in range(n):
    if p[i] in cnt.keys():
        cnt[p[i]] += 1
    else:
        cnt[p[i]] = 1
for i in range(m):
    lst.append([cnt[b[i]] if b[i] in cnt.keys() else 0, cnt[c[i]] if c[i] in cnt.keys() else 0, i + 1])
lst.sort(reverse=True)
print(lst[0][2])
