import math

def f(x):
    return math.sin(math.pi*x) - 1

def bisection(xmin=0.,xmax=2.,iter=100):
    for i in range(0,iter):
        x = (xmin + xmax)/2.
        print(x, f(x))
        if(f(x)*f(xmax)>0.):
            xmax = x
        else:
            xmin = x 
        if(abs(f(x)) < 1.0e-6):
            #print(x, i, f(x))
            break

bisection()    

    