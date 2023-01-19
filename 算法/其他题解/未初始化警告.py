# https://www.acwing.com/problem/content/4457/

'''
# 一个一个加 - 超时
n,k = list(map(int,input().split()))
num = 0
x = [0]

while k:
    k-=1
    xi,yi = list(map(int,input().split()))
    # if yi == 0:continue
    if yi not in x: num+=1
    x.append(xi)

print(num)
'''

# 一个一个比

n,k = list(map(int,input().split()))
num = 0
x = [False]*(n+1)
x[0]=True

while k:
    k-=1
    xi, yi = list(map(int, input().split()))
    if x[yi]==False:num+=1
    if x[xi]==False:x[xi]=True
print(num)