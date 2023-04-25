# 1.-rand()...is used to generate a random value between 0-1. (+ve)
import numpy as np
var=np.random.rand(4)
print(var)

# 2.-randn()..is used to generate a random value close to zero.(+ve.-ve)
var1=np.random.randn(5)
print(var1)

# 3.-ranf()..returns an array of specified shape & fills it with random floats (0.0-1.0)
var2=np.random.ranf(4)
print(var2)

# 4.-randint()..returns random no. between range
#var3=np.random.randint(min,max,"total_values")
var3=np.random.randint(5,20,5)
print(var3)
