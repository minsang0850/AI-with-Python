import numpy as np

def step_function(n):
    return np.array(n>0, dtype=np.int)

def sigmoid_function(n):
    return 1/(1+np.exp(-n))

def relu_function(n):
    return np.maximum(0,n)

def compute(X,W,B):
    A=np.dot(X,W)+B
    Z=sigmoid_function(A)
    return A,Z

def softmax(X):
    exp_X=np.exp(X)
    sum_exp_X=np.sum(exp_X)
    y=exp_X/sum_exp_X
    return y