
import torch
from torch import nn

def docExample_StandardNormalDistribution():
    tensor1 = torch.randn(4)
    print(tensor1)

    tensor2 = torch.randn(2, 3)
    print(tensor2)

def docExample_RectifiedLinearUnit():
    m = nn.ReLU()
    input = torch.randn(2)
    print(input)
    output = m(input)
    print(output)

    m = nn.ReLU()
    input = torch.randn(2).unsqueeze(0)
    print(input)
    output = torch.cat((m(input),m(-input)))
    print(output)
    
def docExample_CrossEntropyLoss():
    """https://pytorch.org/docs/stable/generated/torch.nn.CrossEntropyLoss.html"""
    
    print("# Example of target with class indics")
    loss = nn.CrossEntropyLoss()
    input = torch.randn(3, 6, requires_grad=True)
    print(input)
    target = torch.empty(3, dtype=torch.long).random_(5)
    print(target)
    output = loss(input, target)
    print(output)
    output.backward()
    print()

    print("# Example of target with class probabilities")
    input = torch.randn(3, 5, requires_grad=True)
    target = torch.randn(3, 5).softmax(dim=1)
    try:
        output = loss(input, target)
    except:
        print(f'This Torch (v{torch.__version__}) not supported')
    else:
        outpu.backward()
        print(input, target, output)
    

if __name__ == "__main__":
    #docExample_StandardNormalDistribution()
    #docExample_RectifiedLinearUnit()
    docExample_CrossEntropyLoss()



