# 下面是由chatgpt给出的示例

import torch
import torch.nn as nn


class MyTransform(nn.Module):

    def __init__(self, transform_fn):
        super(MyTransform, self).__init__()
        self.transform_fn = transform_fn

    def forward(self, x):
        return self.transform_fn(x)


def my_transform(x):
    mean = torch.mean(x)
    std = torch.std(x)
    return (x - mean) / std


model = nn.Sequential(nn.Linear(10, 20), nn.ReLU(), nn.Linear(20, 5),
                      MyTransform(my_transform))

# 定义输入数据
input_data = torch.randn(1, 10)

# 执行前向传播
output = model(input_data)
print("out:", output)
