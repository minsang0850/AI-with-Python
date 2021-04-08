import numpy as np
import matplotlib.pylab as plt
import AI_function as af

X=np.arange(-5.0,5.0,0.1)
Y=af.step_function(X)
# plt.plot(X,Y)
# plt.ylim(-0.1,1.1)
# plt.show()

X=np.arange(-5.0,5.0,0.1)
Y=af.sigmoid_function(X)
# plt.plot(X,Y)
# plt.ylim(-0.1,1.1)
# plt.show()

X=np.arange(-5.0,5.0,0.1)
Y=af.relu_function(X)
# plt.plot(X,Y)
# plt.ylim(-0.1,5.1)
# plt.show()

X=np.array([1.0,0.5])
W1=np.array([[0.1,0.3,0.5],[0.2,0.4,0.6]])
B1=np.array([0.1,0.2,0.3])
A,Z=af.compute(X,W1,B1)
print(A,Z)
K=af.softmax(X)
print(K)
# print(W1.shape)
# print(X.shape)
# print(B1.shape)

