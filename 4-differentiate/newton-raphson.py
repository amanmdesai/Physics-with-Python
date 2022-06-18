import math

def f(x):
    return math.sin(math.pi*x) - 1

def nr(x=0.,iter=100,dx=1e-3):
    for i in range(0,iter):
        F = f(x)
        if(abs(f(x)) < 1.0e-6):
            #print(x, i, f(x))
            return x, F
        print(x,F)
        df = (f(x+dx/2) - f(x-dx/2))/dx
        dx = -F/df
        x += dx
    return x, f(x)

print(nr())

    