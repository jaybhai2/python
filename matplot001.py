import matplotlib.pyplot as pyplot
import matplotlib.animation as animation
from matplotlib import style
import psutil   
import time


fig = pyplot.figure()
ax1 = fig.add_subplot(1,1,1)
fig.show()

x, y = [], []

for time1 in range(0,100,1):
    x.append(time1)
    y.append(psutil.cpu_percent())
    ax1.plot(x,y,color='b')
    fig.canvas.draw()

    ax1.set_xlim(left=max(0, time1-10),right = time1+10)

    time.sleep(0.2)


pyplot.close()




'''  plot from file ----------------
style.use('fivethirtyeight')

fig = pyplot.figure()
ax1 = fig.add_subplot(1,1,1)

def animate(i):
    graph_data = open('data.txt','r').read()
    lines = graph_data.split('\n')
    xaxis = []
    yaxis = []
    for line in lines:
        if len(line) >1:
            x, y = line.split(',')
            xaxis.append(x)
            yaxis.append(y)
    ax1.clear()
    ax1.plot(xaxis,yaxis)


ani = animation.FuncAnimation(fig, animate, interval = 1000)
pyplot.show()
'''