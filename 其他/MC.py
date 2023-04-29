import matplotlib.pyplot as plt
import numpy as np

# 原始数据序列
x0 = np.array([43746323, 43685558, 43622347, 43580021, 43538934, 43506963,
               43429862, 43374914, 43316755, 43178759, 42591407])
# 累加生成
x1 = np.cumsum(x0)
# 数据长度
n = len(x0)
# 矩阵运算
B = np.zeros((n - 1, 2))
Y = np.zeros((n - 1, 1))
for i in range(n - 1):
    B[i][0] = -0.5 * (x1[i] + x1[i + 1])
    B[i][1] = 1
    Y[i][0] = x0[i + 1]
BT = B.T
A = np.dot(np.dot(np.linalg.inv(np.dot(BT, B)), BT), Y)
# 模型参数
a = A[0][0]
u = A[1][0]
# 原始数据序列的预测值
x0_hat = np.zeros(n)
for i in range(n):
    x0_hat[i] = (x1[0] - u / a) * np.exp(-a * i) + u / a
# 预测精度
epsilon = np.abs(x0 - x0_hat) / x0  # 相对误差
C = np.sum(np.square(x0 - x0_hat)) / np.sum(np.square(x0 - np.mean(x0)))
# 后验差比
# 模型可靠性判断
if C < 0.35:
    print("模型是良好的")
elif C < 0.5:
    print("模型是合格的")
else:
    print("模型是不合格的")
# 预测未来10年的人口数量
x_future = np.zeros(10)
for i in range(10):
    x_future[i] = (x1[0] - u / a) * np.exp(-a * (n + i)) + u / a
# 输出预测结果
print("未来10年的人口数量为:")
print(x_future)
# 画出人口变化的曲线图
plt.plot(range(2010, 2021), x0, label="实际值")
plt.plot(range(2010, 2021), x0_hat, label="预测值")
plt.plot(range(2021, 2031), x_future, label="未来值")
plt.xlabel("年份")
plt.ylabel("人口数量")
plt.title("辽宁省人口变化曲线图")
plt.legend()
plt.show()
