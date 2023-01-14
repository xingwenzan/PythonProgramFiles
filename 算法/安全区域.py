# https://www.acwing.com/problem/content/4798/

n,m = list(map(int,input().split()))
xs = [1]*n
ys = [1]*n
out = []
for i in range(m):
    x,y = list(map(int,input().split()))
    xs[x-1] = 0
    ys[y-1] = 0
    out.append(sum(xs)*sum(ys))

print(" ".join(map(str,out)))