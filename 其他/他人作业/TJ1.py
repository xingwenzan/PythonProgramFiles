goods = {}  # 存货物
haed = []  # 存货物编号对应的货物名字
goodsNum = 0  # 货物数量
money = 0  # 总营业额


def addGood():
    global goodsNum
    print("请依次输入货物编号、货物名称、货物金额")
    new = list(input().split())
    tmp = 0
    for i in range(len(new[0])):
        tmp = tmp * 10 + int(new[0][i])
    # 货物放入库存
    goods[(tmp, new[1])] = int(new[2])
    # 记录货物名字
    while len(haed) <= tmp: haed.append(-1)
    haed[tmp] = new[1]
    # 货物数加一
    goodsNum += 1
    print("添加完成")
    return


def findName(idx):  # 查询货物名字
    return haed[idx]


def findIdx(string):  # 查询货物编号
    try:
        ans = haed.index(string)
    except ValueError:
        return -1
    else:
        return ans


def findMoney(obj):
    if obj.isdigit():
        idx = int(obj)
        name = findName(idx)
    else:
        idx = findIdx(obj)
        name = obj
    return goods[(idx, name)]


def delectGood():
    global goodsNum
    print("请输入删除货物名称或编号")
    tmp = input()
    if tmp.isdigit():
        name = findName(int(tmp))
        if name != -1:
            del goods[(int(tmp), name)]
            goodsNum -= 1
        else:
            print("该货物不存在")
    else:
        idx = findIdx(tmp)
        if idx != -1:
            del goods[(idx, tmp)]
            goodsNum -= 1
        else:
            print("该货物不存在")
    print("删除成功,还剩 {} 种货物".format(goodsNum))
    return


def findGoos():
    print("请输入查询的货物名称或编号")
    tmp = input()
    if tmp.isdigit():
        name = findName(int(tmp))
        if name != -1:
            print("货物编号：", tmp)
            print("货物名字：", name)
            print("货物金额：", findMoney(name))
        else:
            print("该货物不存在")
    else:
        idx = findIdx(tmp)
        if idx != -1:
            print("货物编号：", idx)
            print("货物名字：", tmp)
            print("货物金额：", findMoney(tmp))
        else:
            print("该货物不存在")
    print("查询完成")
    return


def sumMoney():
    global money
    print("请问顾客购买了几种商品")
    n = int(input())
    print("请输入商品名称/编号和商品购买数量")
    tmp = 0
    for i in range(n):
        lst = list(input().split())
        tmp += findMoney(lst[0]) * int(lst[1])
    money += tmp
    return tmp


while (1):
    # 目录
    print("您可以进行以下操作:\n1. 增加货物\n2. 删除货物\n3. 查询货物\n4. 顾客总额结算\n5. 当前总营业额查询")
    op = int(input())
    if (op == 1):
        addGood()
        # print(goods)
    elif op == 2:
        delectGood()
    elif op == 3:
        findGoos()
    elif op == 4:
        print("顾客花费 {} 元".format(sumMoney()))
    elif op == 5:
        print("当前营业额：", money)

    # 离开操作
    print("是否离开超市,离开则输入 y 或 Y 或 1 或 是")
    out = input()
    if out in ["y", "Y", "1", "是"]:
        print("操作结束")
        break
