#Load libraries
import numpy as np
import torch
import glob
import torch.nn as nn
from torchvision.transforms import transforms
from torch.utils.data import DataLoader
from torch.optim import Adam
from torch.autograd import Variable
import torchvision
import pathlib
#checking for device
device=torch.device('cuda' if torch.cuda.is_available() else 'cpu')
print(device)
#Transforms
transformer=transforms.Compose([
    transforms.Resize((150,150)),
    transforms.RandomHorizontalFlip(),
    transforms.ToTensor(),  #0-255 to 0-1, numpy to tensors
    transforms.Normalize([0.5,0.5,0.5], # 0-1 to [-1,1] , formula (x-mean)/std
                        [0.5,0.5,0.5])
])
#Dataloader

#Path for training and testing directory
train_path='C:/Users/hp/OneDrive/Desktop/pytorch_projects/detection/seg_train/seg_train'
test_path='C:/Users/hp/OneDrive/Desktop/pytorch_projects/detection/seg_test/seg_train'

train_loader=DataLoader(
    torchvision.datasets.ImageFolder(train_path,transform=transformer),
    batch_size=256, shuffle=True
)
test_loader=DataLoader(
     torchvision.datasets.ImageFolder(test_path,transform=transformer),
     batch_size=256, shuffle=True
)