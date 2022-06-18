
from complex import Complex
import math 
import numpy as np 
def current(t):
    w = 1 
    Vo = 1
    C = 1
    L = 1
    R = 1
    Z = math.sqrt(R**2 + (1/w*C - w*L)**2)
    theta = math.atan((1/w*C -w*L)/R)
    I = Complex((Vo/abs(Z)),0) * (Complex(math.cos(w*t + theta),-math.sin(w*t + theta)))
    I = Complex(I[0],I[1])
    print(I.magnitude(), I.phase())
    return I
t = np.arange(0,5,.01)
print(t)
for i in range(100):
    current(t[i+1])
