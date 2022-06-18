import random
import math
import numpy as np


DeltaN = 0
N = 100
time = round(math.log(2) * 1000)
lambda_ = .001
for j in range(time):
    if N ==0:
        break
    for i in range(N):
        decay = random.random()
        if (decay < lambda_):
            N = N - 1

print(N)