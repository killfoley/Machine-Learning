import matplotlib.pyplot as plt

from sklearn import datasets
from sklearn import svm

digits = datasets.load_digits()
clf = svm.SVC(gamma=0.001, C=100)
x,y = digits.data[:-1], digits.target[:-1]
clf.fit(x,y)

print('Prediction:',clf.predict(digits.data[[-6]]))
plt.imshow(digits.images[-6], interpolation='nearest', cmap=plt.cm.gray_r)
plt.show()