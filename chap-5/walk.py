# random walk

import random
import math
from matplotlib.pyplot import cm
import matplotlib.pyplot as plt 
import numpy as np
#print(random.random())


def steps(x,y):
    delta_x = (random.random()-.5)*2
    delta_y= (random.random() -.5)*2
    norm = math.sqrt(delta_x**2 + delta_y**2)
    x += delta_x/norm 
    y += delta_y/norm 
    return x,y

size = 10000
num_walk = 10
#color=['r','b','g','c','m','y','k']

color = cm.rainbow(np.linspace(0, 1, num_walk))

fig, ax = plt.subplots(figsize=(20,20))
for  j in range(num_walk):
    x, y= 0,0
    array_x, array_y = np.zeros(size), np.zeros(size)
    for i in range(size):
        x, y = steps(x,y)
        array_x[i], array_y[i] = x, y
    ax.plot(array_x,array_y,color=color[j],label=j+1)
    ax.plot()
plt.Circle(( 0 , 0 ), 100 )
ax.add_artist( plt.Circle(( 0 , 0 ), math.sqrt(size),fill=False ) )
plt.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.savefig("walks.pdf")
