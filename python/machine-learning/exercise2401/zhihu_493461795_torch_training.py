#!/usr/bin/env python3

"""
构建一个深度学习模型 <https://zhuanlan.zhihu.com/p/493461795>
"""

def sklearnTrainTestSplitDigits():
    from sklearn.datasets import load_digits
    from sklearn.model_selection import train_test_split
    from sklearn.ensemble import RandomForestClassifier
    X, y = load_digits(return_X_y=True)
    X_train, X_test, y_train, y_test = train_test_split(X, y)
    rf = RandomForestClassifier().fit(X_train, y_train)
    score = rf.score(X_test, y_test)
    
    print(f'---X---\n{X}', f'---y---\n{y}', f'---X_train---\n{X_train}', f'---X_test---\n{X_test}', f'rfc.{score=}', sep='\n\n')
    return X_train, X_test, y_train, y_test


import torch
from torch.utils.data import TensorDataset, DataLoader
from torch import nn, optim

class Model(nn.Module): # 继承Module基类
    def __init__(self, n_input=64, n_hidden=32, n_output=10):
        # 定义一个含有单隐藏层的全连接网络，其中输入64为手写数字数据集的特征数，输出10为类别数，隐藏层神经元数量设置32
        super().__init__()
        # 使用全连接层和ReLU激活函数搭建网络模型
        self.dnn = nn.Sequential(
            nn.Linear(n_input, n_hidden),
            nn.ReLU(),
            nn.Linear(n_hidden, n_output))

    def forward(self, x):
        # 重载forward函数，从输入到输出
        return self.dnn(x)

def torchDatasetUtility():
    pass

def torchTrainingSimple(X_train, X_test, y_train, y_test):
    
    """ Training Torch model with Linear neural network """
    
    # dataset and dataloader
    X_train_tensor = torch.Tensor(X_train)
    y_train_tensor = torch.Tensor(y_train).long() # 主要标签需要用整数形式，否则后续用于计算交叉熵损失时报错
    dataset = TensorDataset(X_train_tensor, y_train_tensor) # 直接调用TensorDataset加以包裹使用
    dataloader = DataLoader(dataset, batch_size=128, shuffle=True) # 每128个样本为一个batch，训练时设为随机

    X_test_tensor = torch.Tensor(X_test) # 测试集只需转化为tensor即可
    y_test_tensor = torch.Tensor(y_test).long()

    print(f'X_train_tensor:\n{X_train_tensor}', f'X_test_tensor:\n{X_test_tensor}', sep='\n')
    
    # Training model
    model = Model() # 初始化模型
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.Adam(model.parameters(), lr=0.001) # 选用Adam优化器，传入模型参数，设置学习率
    for epoch in range(50): # 50个epoch
        for data, label, in dataloader: # DataLoader是一个可迭代对象
            optimizer.zero_grad() # 待优化参数梯度清空
            prob = model(data) # 待优化参数梯度清空
            loss = criterion(prob, label)  # 评估模型损失
            loss.backward() # 损失反向传播，完成对待优化参数的梯度求解
            optimizer.step() # 参数更新
        if (epoch + 1) % 5 == 0: # 每隔5个epoch打印当前模型训练效果
            with torch.no_grad():
                train_prob = model(X_train_tensor)
                train_pred = train_prob.argmax(dim=1)
                acc_train = (train_pred==y_train_tensor).float().mean()
                test_prob = model(X_test_tensor)
                test_pred = test_prob.argmax(dim=1)
                acc_test = (test_pred==y_test_tensor).float().mean()
                print(f"epoch: {epoch}, train_accuracy: {acc_train}, test_accuracy: {acc_test} !")

if __name__ == "__main__":
    X_train, X_test, y_train, y_test = sklearnTrainTestSplitDigits()
    print()
    torchTrainingSimple(X_train, X_test, y_train, y_test)
