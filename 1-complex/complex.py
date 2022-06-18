# code for creating complex number class


# class for complex numbers
import math
class Complex:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    
    def magnitude(self) -> None:
        mag = self.x**2 + self.y**2
        return mag

    def phase(self):
        theta = math.atan(self.y/self.x)
        return theta
        
    def __add__(self, other):
        x_new = self.x + other.x
        y_new = self.y + other.y
        return x_new, y_new

    def __mul__(self, other):
        x_new = self.x * other.x -  self.y * other.y
        y_new =  self.x * other.y + self.y * other.x
        return x_new, y_new
    




#print(Complex(1,0) + Complex(1,8))        
#print(Complex(1,1) * Complex(1,8))        
#print(Complex.magnitude(Complex(1,1)))