# 表达式求值 https://www.acwing.com/problem/content/3305/

priority = {'(': 0, '+': 1, '-': 1, '*': 2, '/': 2}
sign = []
nums = []


def new_eval():
    b = nums.pop()
    a = nums.pop()
    c = sign.pop()
    x = 0
    if c == '+':
        x = a + b
    elif c == '-':
        x = a - b
    elif c == '*':
        x = a * b
    else:
        x = int(a / b)
    nums.append(x)


formula = input()
n = len(formula)
i = 0
while i < n:
    c = formula[i]
    if c.isdigit():
        x = 0
        j = i
        while j < n and formula[j].isdigit():
            x = x * 10 + int(formula[j])
            j += 1
        i = j - 1
        nums.append(x)
    elif c == '(':
        sign.append(c)
    elif c == ')':
        while sign[-1] != '(':
            new_eval()
        sign.pop()
    else:
        while len(sign) and priority[sign[-1]] >= priority[c]:
            new_eval()
        sign.append(c)
    i += 1

while len(sign):
    new_eval()
print(nums[-1])
