# -*- coding: utf-8 -*-
"""Softmax Regression.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1XA6QWSVlJ1O4K3OqPPYeH57XHMqoCAWN
"""

import torch
import torch.nn as nn
import torch.nn.functional as F
import torchvision
import torchvision.transforms as transforms
from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split
from torch.utils.data import DataLoader
import os
import pandas as pd
from torchvision.io import read_image
from torch.utils.data import Dataset
from tensorflow.keras.utils import to_categorical

a,b=load_data_fashion_mnist(30)

for x,y in a:
  print(y)

def load_data_fashion_mnist(batch_size, resize=None): 
    trans = [transforms.ToTensor()]
    if resize:
        trans.insert(0, transforms.Resize(resize))
    trans = transforms.Compose(trans)
    mnist_train = torchvision.datasets.FashionMNIST(root="../data",
                                                    train=True,
                                                    transform=trans,
                                                    download=True)
    mnist_test = torchvision.datasets.FashionMNIST(root="../data",
                                                   train=False,
                                                   transform=trans,
                                                   download=True)

    return (DataLoader(mnist_train, batch_size, shuffle=True,
                            num_workers=4),
            DataLoader(mnist_test, batch_size, shuffle=False,
                            num_workers=4))

a,b=load_data_fashion_mnist(30,False)
for x,y in a:
  print(len(y))
  break

def train_ch3(net, train_iter, test_iter, loss, num_epochs, updater):
    for epoch in range(num_epochs):
        train_metrics = train_epoch_ch3(net, train_iter, loss, updater)
        test_acc = evaluate_accuracy(net, test_iter)
        animator.add(epoch + 1, train_metrics + (test_acc,))
    train_loss, train_acc = train_metrics
    assert train_loss < 0.5, train_loss
    assert train_acc <= 1 and train_acc > 0.7, train_acc
    assert test_acc <= 1 and test_acc > 0.7, test_acc



class LinearRegression():
  def __init__(self):
    from torch import nn
    self.model = nn.Sequential(nn.Flatten(), nn.Linear(784, 10))
    def init_weights(m):
      if type(m) == nn.Linear:
        nn.init.normal_(m.weight, std=0.01)
    self.model.apply(init_weights)
    self.lossHis=[]
    #Model

    
    
  def train(self,batch,lr,num_epocs):
    trainData,_=load_data_fashion_mnist(30,False)
    trainer=torch.optim.SGD(self.model.parameters(), lr=lr)
    self.model.train()
    #SGD
    for epoc in range(num_epocs):
      for x,y in trainData:
        y_hat=self.model(x)
        loss=nn.CrossEntropyLoss()(y_hat,y)
        trainer.zero_grad()
        
        loss.backward()
        trainer.step()
        train_loss=self.accuracy(y_hat,y)
        self.lossHis.append(float(train_loss))
        print(f'epoch {epoc + 1}, Accuracy {float(train_loss/len(y)):f}')
      
      
  def loss(self,y_hat,y):
    return -torch.log(y_hat[range(len(y_hat)), y])
  def accuracy(self,y_hat, y):
    if len(y_hat.shape) > 1 and y_hat.shape[1] > 1:
        y_hat = y_hat.argmax(axis=1)
    cmp = y_hat.type(y.dtype) == y
    return float(cmp.type(y.dtype).sum())
    with torch.no_grad():
        for X, y in data_iter:
            metric.add(accuracy(net(X), y), y.numel())
    return metric[0] / metric[1]
model=LinearRegression()
model.train(batch=4,lr=0.001,num_epocs=20)

model.lossHist=[x/30 for x in model.lossHis]

import matplotlib.pyplot as plt
plt.plot(model.lossHist)
plt.show()

def get_fashion_mnist_labels(labels):
    text_labels = [
        't-shirt', 'trouser', 'pullover', 'dress', 'coat', 'sandal', 'shirt',
        'sneaker', 'bag', 'ankle boot']
    return [text_labels[int(i)] for i in labels]
def show_images(imgs, num_rows, num_cols, titles=None, scale=1.5):
    figsize = (num_cols * scale, num_rows * scale)
    _, axes = plt.subplots(num_rows, num_cols, figsize=figsize)
    axes = axes.flatten()
    for i, (ax, img) in enumerate(zip(axes, imgs)):
        ax.imshow(img.numpy())
        ax.axes.get_xaxis().set_visible(False)
        ax.axes.get_yaxis().set_visible(False)
        if titles:
            ax.set_title(titles[i])
    return axes
def predict_ch3(net, test_iter, n=30): 
    for X, y in test_iter:
        break
    trues = get_fashion_mnist_labels(y)
    preds = get_fashion_mnist_labels(net(X).argmax(axis=1))
    titles = [true + '\n' + pred for true, pred in zip(trues, preds)]
    show_images(X[0:n].reshape((n, 28, 28)), 1, n, titles=titles[0:n])
a,b=load_data_fashion_mnist(30,False)
predict_ch3(model.model, b)