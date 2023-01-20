# https://www.acwing.com/problem/content/4732/
# 其他人的证明:https://www.acwing.com/solution/content/154360/

"""
e*d=(p-1)*(q-1)+1=p*q-p-q+2   n=p*q   m=n-ed+2=p+q
q=m-p
pq=(m-p)p  =>  n=(m-p)p
p**2-m*p+n=0  反之  q**2-m*q+n=0
韦达定理可求
"""

k = int(input())

for i in range(k):
    n, d, e = list(map(int, input().split()))
    m = n - e * d + 2
    tmp1 = m ** 2 - 4 * n
    if tmp1 < 0:
        print("NO")
        continue
    tmp2 = int(pow(tmp1, 0.5))
    if tmp2 ** 2 != tmp1:
        print("NO")
        continue
    q = m + tmp2 >> 1
    p = m - tmp2 >> 1
    print("{} {}".format(p, q))
