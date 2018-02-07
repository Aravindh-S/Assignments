import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
li = []
pi = []
with open('x.dat', 'r') as xd:
    with open('y.dat', 'r') as yd:
        data = xd.readlines()
        check = yd.readlines()
        for i in data:
            li.append(i.strip().split())
        for j in check:
            pi.append(float(j.strip()))

        X, xr, yr, xb, yb = [], [], [], [], []
        for i, j in enumerate(li):
            X.append([float(j[0]), float(j[1])])

            if(pi[i] == 0):
                xr.append(float(j[0]))
                yr.append(float(j[1]))

            else:
                xb.append(float(j[0]))
                yb.append(float(j[1]))

        plt.scatter(xr, yr, color="red")
        plt.scatter(xb, yb)
        plt.show()

        U = (np.array(X))

        check = np.array([0.02, 0.08])
        ch = np.transpose([check])
        V = np.array(pi)
        print(U)
        print('\n')
        print(V)

        print(ch)

        logreg = LogisticRegression()
        logreg.fit(U, V)

        t = logreg.predict(np.array([[0.34792627, 0.8625731]]))
        print("Here is the output")
        print(t)
