import random
import numpy as np

def f(x1,x2,x3,x4,x5,x6,x7,x8,x9,x10): 
    return ((x1 + x2 + x3 + x4 + x5 + x6 + x7 + x8 + x9 + x10)**2)

def MC_gen():
    r = np.zeros(10)
    for i in range(10):
        r[i] = random.random()
    N_avg = 0
    for exper in range(100):
        N_passed = 0
        N_total = 0
        for i in range(100):
            for i in range(10):
                r[i] = random.random()
            u = random.random()*100
            if u < f(r[0],r[1],r[2],r[3],r[4],r[5],r[6],r[7],r[8],r[9]):
                N_passed = N_passed + 1
            N_total = N_total + 1
        N_avg += N_passed/N_total
    print(N_avg*6)
MC_gen()