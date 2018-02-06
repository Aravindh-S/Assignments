import matplotlib.pyplot as plt
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

        xr, yr, xb, yb = [], [], [], []
        for i, j in enumerate(li):
            if(pi[i] == 0):
                xr.append(float(j[0]))
                yr.append(float(j[1]))
            else:
                xb.append(float(j[0]))
                yb.append(float(j[1]))
        plt.scatter(xr, yr, color="red")
        plt.scatter(xb, yb)
        plt.show()
