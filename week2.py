import numpy as np
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
# iris = np.genfromtxt(url, delimiter=',', dtype='object')
iris_2d = np.genfromtxt(url, delimiter=',', dtype='float', usecols=[0,1,2,3])
A = np.array(np.transpose(iris_2d)[0])
B = np.array(np.transpose(iris_2d)[0:2])
Vertical = np.vstack(A)
Horizontal = np.hstack(B)
Intersection = np.array([x for x in A if x in B])
# A = np.array([float(x.decode('utf-8')) for x in A])
LessThanFive = np.array([x for x in A if 10.0 > x > 5.0])
Filtered = np.array([iris_2d[i] for i in range(150) if iris_2d[i][2] > 1.5 and iris_2d[i][0] < 5.0])
