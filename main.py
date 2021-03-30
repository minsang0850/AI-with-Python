import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

iris=load_iris()
X=iris.data[:,:2]
y=iris.target
y_name=iris.target_names

x1_min,x1_max=X[:, 0].min()-.5,X[:, 0].max()+.5
x2_min,x2_max=X[:, 1].min()-.5,X[:, 1].max()+.5

plt.figure(figsize=(8,6))
plt.scatter(X[:, 0],X[:, 1], c=y, cmap=plt.cm.Set1, edgecolor='k')

plt.xlabel('Sepal length')
plt.ylabel('Sepal width')

plt.xlim(x1_min,x1_max)
plt.ylim(x2_min,x2_max)

plt.show()