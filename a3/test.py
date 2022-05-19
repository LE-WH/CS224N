import numpy as np
import torch
import torch.nn as nn

class Net(torch.nn.Module):  # 继承torch的module

    # min (Ax-b)
    def __init__(self,tar):
        super(Net, self).__init__()  # 继承__init__功能
        # 定义每一层用什么样的样式
        self.A = nn.Parameter(torch.tensor([[1.,2,3,4],[4,3,1,5]]),requires_grad=False)
        self.b = nn.Parameter(torch.tensor(tar),requires_grad=False)
        self.x = nn.Parameter(torch.tensor([[1.0],[1],[1],[1]]))

    def forward(self):
        r = self.A @ self.x
        return r


a = np.array([[0.5,0.5]])

net = Net(a)


loss_func = nn.CrossEntropyLoss()

# loss = loss_func(out.T, net.b)

# loss.backward()



optimizer = torch.optim.Adam(net.parameters(), lr = 0.01)

for i in range(1000):
    optimizer.zero_grad()
    output = net().T
    loss = loss_func(output,net.b)
    loss.backward()
    optimizer.step()



# 


# print(out)
# print(loss)
# print(net.A.grad)
# print(net.b.grad)
# print(net.x.grad)
print(list(net.parameters()))

# inputt = torch.randn(1, 2, requires_grad=True)
# target = torch.randn(1, 2).softmax(dim=1)
# loss = nn.CrossEntropyLoss()
# output = loss(inputt, target)
# output.backward()


# print(inputt)
# print(target)
# print(output)