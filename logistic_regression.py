import matplotlib.pyplot as plt
li = []
with open('x.dat', 'r') as f:
    data = f.readlines()
    for i in data:
        li.append(i.strip().split())
    x, y = [], []
    for i in li:
        x.append(float(i[0]))
        y.append(float(i[1]))
    plt.scatter(x, y)
    plt.show()
