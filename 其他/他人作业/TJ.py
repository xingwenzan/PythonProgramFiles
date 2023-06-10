"""
某公司以一定的策略投资一支股票，每天都会投入一定的资金用于购买股票，
其策略为：在周一的时候投入1 万块钱。从周二到周日，每天都比前一天多投入 1 万块钱。在接下来每一个周一，都会比前一个周一多投入1 万块钱。

要求：

1、使用函数，实现对于任意输入的正整数n，能够得到在第 n 天结束的时候该公司在该股票上总共投入了多少钱。
"""


# 投入钱计算函数
# 周一是第一天，假设第 n 天也投了再计算，到第 n 天一共追投 n-1 天
def useMoney(n):
    # 最开始的一万
    sumMoney = 10000
    monday = 10000
    tmp = 10000  # 每次追投的钱
    for i in range(n - 1):
        if n % 7 == 6:  # 周一
            monday += 10000
            tmp = monday
        else:
            tmp += 10000
        sumMoney += tmp
    return sumMoney


n = int(input())
print(useMoney(n))
