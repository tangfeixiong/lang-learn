#!/usr/bin/env phthon3

import torch # for all things PyTorch
import torch.nn as nn # for torch.nn.Module, the parent object for PyTorch models
import torch.nn.functional as F # for the activation function

# Introduction to PyTorch
def introyt1_pytorchTensors():
    """ https://pytorch.org/tutorials/beginner/introyt/introyt1_tutorial.html#pytorch-tensors """
    
    print('# First, just a few of the ways to create tensors')
    z = torch.zeros(5, 3)
    print(z)
    print(z.dtype)

    print('# You can always override the default float32 data type')
    i = torch.ones((5, 3), dtype=torch.int16)
    print(i)

    print("# It's common to initialize learning weights randomly")
    torch.manual_seed(1729)
    r1 = torch.rand(2, 2)
    print('A random tensor:', r1, sep='\n')

    r2 = torch.rand(2, 2) # new values
    print('\nA different random tensor:', r2, sep='\n')

    torch.manual_seed(1729)
    r3 = torch.rand(2, 2) # repeats values of r1 because of re-seed
    print(f'\nShould match r1: {torch.equal(r1, r3)}', r3, sep='\n')

    print('PyTorch tensors perform arithmetic operations intuitively')
    ones = torch.ones(2, 3)
    print(ones)
    
    twos = torch.ones(2, 3) * 2 # every element is mutiplized by 2
    print(twos)

    three = ones + twos # addition allowed because shapes are similar
    print(three)        # tensors are added element-wise
    print(three.shape)  # this hase the same dimensions as input tensors

    r1 = torch.rand(2, 3)
    r2 = torch.rand(3, 2)
    try:
        r3 = r1 + r2 # get a runtime error
    except:
        pass

    print("# Here's small sample of the mathmetical operations available")
    #r = (torch.rand(2, 2) - 0,5) * 2 # values between -1 and 1
    r = torch.rand(2, 2); r -= 0.5; r *= 2
    print('A random matrix, r:', r, sep='\n')

    # Common mathematical operations are supported
    print('\nAbsolute value of r:', torch.abs(r), sep='\n')

    # ...as are trigonometric functions:
    print('\nInverse sine of r:', torch.asin(r), sep='\n')

    # ...and linear algebra operations like determinant and singular value decomposition
    print('\nDeterminant of r:', torch.det(r), sep='\n')
    print('\nSingular value decomposition of r:', torch.svd(r), sep='\n')

    # ...and statistical and aggregate operations:
    print('\nAverage and standard deviation of r:', torch.std_mean(r), sep='\n')
    print('\nMaximum value of r:', torch.max(r), sep='\n')


class LeNet(nn.Module):
    """ https://pytorch.org/tutorials/beginner/introyt/introyt1_tutorial.html#pytorch-models """

    def __init__(self):
        super(LeNet, self).__init__()
        # 1 input image channel (black & white), 6 output channels, 5x5 square convolution
        # kernel
        self.conv1 = nn.Conv2d(1, 6, 5)
        self.conv2 = nn.Conv2d(6, 16, 5)
        # an affine operation: y = Wx + b
        self.fc1 = nn.Linear(16 * 5 * 5, 120) # 5*5 from image dimension
        self.fc2 = nn.Linear(120, 84)
        self.fc3 = nn.Linear(84, 10)

    def forward(self, x):
        # Max pooling over a (2, 2) window
        x = F.max_pool2d(F.relu(self.conv1(x)), (2, 2))
        # If the size is a square you can onlly specify a single number
        x = F.max_pool2d(F.relu(self.conv2(x)), 2)
        x = x.view(-1, self.num_flat_features(x))
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = self.fc3(x)
        return x

    def num_flat_features(self, x):
        size = x.size()[1:] # all dimensions except the batch dimention
        num_features = 1
        for s in size:
            num_features *= s
        return num_features
    
def introyt1_pytorchModels():
    """ https://pytorch.org/tutorials/beginner/introyt/introyt1_tutorial.html#pytorch-models """

    net = LeNet()
    print(net) # what does the object tell us about itself?

    input = torch.rand(1, 1, 32, 32) # stand-in for a 32*32 black & white image
    print('\nImage batch shape:', input.shape, '\n')

    output = net(input)
    print('\nRaw output:', output, output.shape, sep='\n')


#%matplotlib inline

import torchvision
import torchvision.transforms as transforms
import matplotlib.pyplot as plt
import numpy as np

def introyt1_pytorchData(dataPath=None):
    """ https://pytorch.org/tutorials/beginner/introyt/introyt1_tutorial.html#datasets-and-dataloaders """

    transform = transforms.Compose(
        [transforms.ToTensor(),
         transforms.Normalize((0.4914, 0.4822, 0.4465), (0.2470, 0.2435, 0.2616))])
    
    if dataPath is None:
        trainset = torchvision.datasets.CIFAR10(root='./data', train=True, download=True, transform=transform) 
    else:
        trainset = torchvision.datasets.CIFAR10(root=dataPath, train=True, download=True, transform=transform)

    trainloader = torch.utils.data.DataLoader(trainset, batch_size=4, shuffle=True, num_workers=2)

    classes = ('plane', 'car', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck')

    def imshow(img):
        img = img / 2 + 0.5 # unnormalize
        npimg = img.numpy()
        plt.imshow(np.transpose(npimg, (1, 2, 0)))

    # get some random training images
    dataiter = iter(trainloader)
    images, labels = next(dataiter)

    # show images
    imshow(torchvision.utils.make_grid(images))
    # print labels
    print(' '.join('%5s' % classes[labels[j]] for j in range(4)))

#%matplotlib inline

import torch.optim as optim
import matplotlib
    
def introyt1_pytorchTrain(dataPath=None):
    """ https://pytorch.org/tutorials/beginner/introyt/introyt1_tutorial.html#training-your-pytorch-model """

    transform = transforms.Compose([transforms.ToTensor(), transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))])
    
    root = './data'
    if dataPath is not None:
        root = dataPath

    trainset = torchvision.datasets.CIFAR10(root=root, train=True, download=True, transform=transform)
    trainloader = torch.utils.data.DataLoader(trainset, batch_size=4, shuffle=True, num_workers=2)    

    testset = torchvision.datasets.CIFAR10(root=root, train=False, download=True, transform=transform)
    testloader = torch.utils.data.DataLoader(testset, batch_size=4, shuffle=False, num_workers=2)
    
    classes = ('plane', 'car', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck')

    # functions to show an image

    def imshow(img):
        img = img /2 + 0.5 #unnormalize
        npimg = img.numpy()
        plt.imshow(np.transpose(npimg, (1, 2, 0)))

    # get some random training images
    dataiter = iter(trainloader)
    images, labels = next(dataiter)

    # show images
    imshow(torchvision.utils.make_grid(images))
    # print labels
    print(' '.join('%5s' % classes[labels[j]] for j in range(4)))

    class Net(nn.Module):
        def __init__(self):
            super(Net, self).__init__()
            self.conv1 = nn.Conv2d(3, 6, 5)
            self.pool = nn.MaxPool2d(2, 2)
            self.conv2 = nn.Conv2d(6, 16, 5)
            self.fc1 = nn.Linear(16 * 5 * 5, 120)
            self.fc2 = nn.Linear(120, 84)
            self.fc3 = nn.Linear(84, 10)

        def forward(self, x):
            x = self.pool(F.relu(self.conv1(x)))
            x = self.pool(F.relu(self.conv2(x)))
            x = x.view(-1, 16 * 5 *5)
            x = F.relu(self.fc1(x))
            x = F.relu(self.fc2(x))
            x = self.fc3(x)
            return x

    net = Net()

    criterion = nn.CrossEntropyLoss()
    optimizer = optim.SGD(net.parameters(), lr=0.001, momentum=0.9)

    for epoch in range(2): # loop over the dataset multiple times
        
        running_loss = 0.0
        for i, data in enumerate(trainloader, 0):
            # get the inputs
            inputs, labels = data

            # zero the paramete gradients
            optimizer.zero_grad()

            # forward + backward + optimize
            outputs = net(inputs)
            loss = criterion(outputs, labels)
            loss.backward()
            optimizer.step()

            # print statistics
            running_loss += loss.item()
            if i % 2000 == 1999: # print every 2000 mini-batches
                print('[%d, %5d] loss: %.3f' %
                      (epoch + 1, i + 1, running_loss / 2000))
                running_loss = 0.0
    
    print('Finished Training')

    correct = 0
    total = 0
    with torch.no_grad():
        for data in testloader:
            images, labels = data
            outputs = net(images)
            _, predicted = torch.max(outputs.data, 1)
            total += labels.size(0)
            correct += (predicted == labels).sum().item()

    print('Accuracy of the network on the 10000 test images: %d %%' % (
        100 * correct / total))


import os
if  __name__ == "__main__":
    #introyt1_pytorchTensors()
    #introyt1_pytorchModels()

    dir_path = os.path.dirname(os.path.realpath(__file__))
    print(__file__, dir_path)
    dataPath = os.path.join(dir_path, "data")
    #introyt1_pytorchData(dataPath)
    #plt.show()

    introyt1_pytorchTrain(dataPath)
    #plt.show()

