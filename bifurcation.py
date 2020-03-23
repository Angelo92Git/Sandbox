import matplotlib.pyplot as plt
import time


def logistic(r, x):
    y = x*r*(1-x)
    return y


xstart = 0
xend = 1000
tc = 0.0000000005
plt.figure(1)
plt.clf()
axes = plt.gca()
axes.set_xlim(1, 4)
axes.set_ylim(0, 1)

ytrail = [None]*32

xdata = []
ydata = []
line, = axes.plot(xdata, ydata, 'rx', markersize=0.5)

for r in range(10000, 40000):
    y0 = 0.8
    for x in range(xstart, xend):
        y = logistic(r/10000, y0)
        y0 = y
        ytrail[x % 32] = y
    xdata.extend([r/10000]*32)
    ydata.extend(ytrail)
    # print(ytrail)
    line.set_xdata(xdata)
    line.set_ydata(ydata)
    if r % 100 == 0:
        plt.draw()
        plt.pause(tc/2)
        time.sleep(tc)


plt.show()
