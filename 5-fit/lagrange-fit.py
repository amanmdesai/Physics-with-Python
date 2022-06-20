#fitting using lagrange fit
import math
import numpy as np
import matplotlib.pyplot as plt

x_i = np.array([1,2,3,4,5,6,7,8,9])
Ei = np.array([0,25,50,75,100,125,150,175,200])
g_i = np.array([10.6,16.0,45.0,83.5,52.8,19.9,10.8,8.25,4.7])
error = np.array([9.34,17.9,41.5,85.5,51.5,21.5,10.8,6.29,4.14])

assert x_i.size == Ei.size 
assert x_i.size == g_i.size 
assert g_i.size == error.size

def lagrange_fit(x,x_i,g_i):


x = np.arange(0,201,1)
function = lagrange_fit(x,Ei,g_i)
function_BW = 8400./((x-74)**2 + (55**2)/4)
print("Resonance Energy",function.max())
print("Decay width:",2*np.sqrt(2*(math.log(2)))*function.std()) #Full Width at Half Maximum or 
plt.scatter(Ei,g_i,label="Data",marker="o",color='black')
plt.plot(x, function,label="Langrage-Fit")
plt.plot(x, function_BW,label="BW fit")
plt.legend()
plt.show()


#plt.errorbar(Ei,g_i,yerr=error, fmt="o")
#x_test = np.array([0,1,2,3])
#g_test = np.array([-12, -12, -24, -60])
#x = np.arange(0,3.1,0.05)
#function = lagrange_fit(x_test,g_test)
#plt.scatter(x_test,g_test,label="data",marker="o")
#plt.plot(x, x**3-9*(x**2) + 8*x -12,label="Hand")