'''
Logistic Regression
'''
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
LIL = []
PIP = []
with open('x.dat', 'r') as xd:
    with open('y.dat', 'r') as yd:
        DATA = xd.readlines()
        CHECK = yd.readlines()
        for i in DATA:
            LIL.append(i.strip().split())
        for j in CHECK:
            PIP.append(float(j.strip()))

        X, XR, YR, XB, YB = [], [], [], [], []
        for i, j in enumerate(LIL):
            X.append([float(j[0]), float(j[1])])

            if PIP[i] == 0:
                XR.append(float(j[0]))
                YR.append(float(j[1]))

            else:
                XB.append(float(j[0]))
                YB.append(float(j[1]))

        plt.scatter(XR, YR, color="red")
        plt.scatter(XB, YB)

        U = (np.array(X))

        V = np.array(PIP)

        LOGREG = LogisticRegression()
        LOGREG.fit(U, V)

        # t = logreg.predict(np.array([[0.34792627, 0.8625731]]))

        M = LOGREG.coef_[0][0]
        C = LOGREG.coef_[0][1]

        X2 = max(max(XB), max(XR))
        X1 = min(min(XR), min(XB))
        Y1 = X1 * M + C
        Y2 = X2 * M + C
        XP = [X1, X2]
        YP = [Y1, Y2]
        plt.plot(XP, YP)
        plt.show()
