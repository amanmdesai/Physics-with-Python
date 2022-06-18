# Trapezoid 

N =1000

def f(x):
    return x

class Trapezoid:
    
    def __init__(self,A,B):
        self.A = A
        self.B = B
    
    def weight(i, h):
        if i==0 or i==N:
            return h/2
        return h
    
    def main(A,B):
        h = (B-A)/(N-1)
        sum=0.0
        for i in range(N):
            t = A + (i-1)*h
            w=Trapezoid.weight(i,h)
            sum = sum + (w * f(t))
        print(sum)

Trapezoid.main(0,1)