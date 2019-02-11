import cupy as cp
import numpy as np

# Create 2D numpy arrays
a = np.random.random(100000000)
a = a.reshape(10000,10000)

b = np.random.random(100000000)
b = b.reshape(10000,10000)

# Move to GPU
g = cp.asarray(a)
h = cp.asarray(b)

# Matrix Mult
out = cp.matmul(g,h)

