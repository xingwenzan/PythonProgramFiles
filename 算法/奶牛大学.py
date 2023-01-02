# https://www.acwing.com/problem/content/4821/
'''
# 暴力枚举法

allnum = int(input())
money = []

for i in range(allnum):
    money.append(int(input()))

total_price = {} # 单价:总价
for j in money:
    n = 0
    for i in money:
        if j<=i: n += 1
    total_price[j] = j * n

print("最多赚")
print(max(total_price.values()))

univalent = []
for n in total_price.keys():
    if total_price[n]==max(total_price.values()):univalent.append(n)

print("最少单价")
print(min(univalent))
'''

'''
# 排序法

allnum = int(input())
money = []

for i in range(allnum):
    money.append(int(input()))

total_price = {} # 单价:总价
money.sort(reverse=True)
for j in range(len(money)):
    total_price[money[j]] = money[j]*(j+1)

print("最多赚")
print(max(total_price.values()))

univalent = []
for n in total_price.keys():
    if total_price[n]==max(total_price.values()):univalent.append(n)

print("最少单价")
print(min(univalent))
'''

# 替换法

allnum = int(input())
money = list(map(int, input().split()))
money.sort(reverse=True)
maxMoney,totleMoney = 0, 0
for i in range(allnum):
    ans = money[i]*(i+1)
    if totleMoney<=ans:
        totleMoney = ans
        maxMoney = money[i]

print(totleMoney,maxMoney)