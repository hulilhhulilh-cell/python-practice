import torch
X1 = [1.2, 0.4, 2.1, 2.8, 0.8, 0.6, 0.3, 1.9, 0.2, 2.3]     # 读入数据
X2 = [2.5, 0.3, 2.7, 2.1, 0.5, 0.4, 1.4, 3.5, 1.2, 3.1]
Y = [1, 0, 1, 1, 0, 0, 0, 1, 0, 1]                                   # 类标记
X1 = torch.Tensor(X1)
X2 = torch.Tensor(X2)
X  = torch.stack((X1, X2), dim=1)      # 将所有特征数据“组装”为一个张量
                                       # 形状为 torch.Size([10, 2])
Y  = torch.Tensor(Y)                   # 形状为 torch.Size([10])
lr = torch.Tensor([0.1])               # 设置学习率

class Perceptron2():
    def __init__(self):
        self.w1 = torch.Tensor([0.0])  # 定义 3 个待优化参数(属性)
        self.w2 = torch.Tensor([0.0])
        self.b  = torch.Tensor([0.0])
    def f(self, x):                    # 感知器函数的实现代码
        x1, x2 = x[0], x[1]
        t = self.w1 * x1 + self.w2 * x2 + self.b
        z = 1.0 / (1 + torch.exp(-t))  # 运用 sigmoid 函数
        return z
    def forward_compute(self, x):      # 前向计算
        pre_y = self.f(x)
        return pre_y                   # 只有一个实数值输出
# ---------------------------------------------
perceptron2 = Perceptron2()            # 创建实例 perceptron2
for ep in range(100):                  # 迭代代数为 100
    for (x, y) in zip(X, Y):
        pre_y = perceptron2.forward_compute(x)          # 执行前向计算
        x1, x2 = x[0], x[1]
        dw1 = ((1 - y) * pre_y - (1 - pre_y) * y) * x1  # 目标函数关于 w1 的偏导数
        dw2 = ((1 - y) * pre_y - (1 - pre_y) * y) * x2  # 目标函数关于 w2 的偏导数
        db  = ((1 - y) * pre_y - (1 - pre_y) * y) * 1   # 目标函数关于 b 的偏导数
        perceptron2.w1 = perceptron2.w1 - lr * dw1      # 更新 w1
        perceptron2.w2 = perceptron2.w2 - lr * dw2      # 更新 w2
        perceptron2.b  = perceptron2.b  - lr * db       # 更新 b

s = '学习到的感知器: pre_y = sigmoid(%.2f * x1 + %.2f * x2 + %.2f)' \
    % (perceptron2.w1, perceptron2.w2, perceptron2.b)
print(s)
for (x, y) in zip(X, Y):                          # 使用感知器做预测测试
    t = 1 if perceptron2.f(x) > 0.5 else 0          # 阶跃变换
    if t == y.item():
        print('点(%.2f, %.2f)被<正确>分类！' % (x[0], x[1]))
    else:
        print('点(%.2f, %.2f)被<错误>分类！' % (x[0], x[1]))

import matplotlib.pyplot as plt
plt.rcParams["font.family"] = ["SimHei"]
plt.rcParams["axes.unicode_minus"] = False

# 分开绘制两类样本
pos = X[Y==1]
neg = X[Y==0]
plt.scatter(pos[:,0], pos[:,1], c='r', label="办理会员 y=1")
plt.scatter(neg[:,0], neg[:,1], c='b', label="不办理会员 y=0")

# 画决策边界直线
w1 = perceptron2.w1.item()
w2 = perceptron2.w2.item()
b = perceptron2.b.item()
x1_line = torch.linspace(0,3,100)
x2_line = (-w1 * x1_line - b)/w2
plt.plot(x1_line, x2_line, 'g--', label='决策边界')

plt.xlabel("月消费金额(百元)")
plt.ylabel("月浏览次数(百次)")
plt.legend()
plt.grid(alpha=0.3)
plt.show()
