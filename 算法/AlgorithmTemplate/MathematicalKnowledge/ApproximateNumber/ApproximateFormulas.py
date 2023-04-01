# N = p1^a1 * p2^a2 * …… * pk^ak
# 约数个数 https://www.acwing.com/problem/content/872/
# count = (a1+1)*(a2+1)*……*(ak+1)
# 约数之和 https://www.acwing.com/problem/content/873/
# sum = (p1^0+p1^1+……+p1^a1)*(p2^0+p2^1+……+p2^a2)*……*(pk^0+pk^1+……+pk^ak)

N = 110
mod = 10 ** 9 + 7


def primeFactor(lst):
    prime = {}
    for num in lst:
        i = 2
        while i <= num / i:
            while num % i == 0:
                num //= i
                if i in prime:
                    prime[i] += 1
                else:
                    prime[i] = 1
            i += 1
        if num > 1:
            if num in prime:
                prime[num] += 1
            else:
                prime[num] = 1
    return prime


def approxmateCount(lst):  # 约数个数
    ans = 1
    for i in primeFactor(lst).values():
        ans = int(ans * (i + 1) % mod)
    return ans


def approxmateSum(lst):  # 约数之和
    ans = 1
    for base, index in primeFactor(lst).items():
        tmp = 1
        for i in range(index):
            tmp = (tmp * base + 1) % mod
        ans = ans * tmp % mod
    return ans


n = int(input())
lst = []
for i in range(n):
    x = int(input())
    lst.append(x)

print(approxmateCount(lst))  # 约数个数
print(approxmateSum(lst))  # 约数之和
