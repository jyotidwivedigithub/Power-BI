# Histogram Plot...
# SYNTAX:-import matplotlib.pyplot as plt  
        # x=[]
        # plt.hist(x)  
        # plt.show()

import matplotlib.pyplot as plt
import numpy as np
import random
x=np.random.randint(10,60,(50))
print(x)

no=[48,55,33,27,35,12,42,10,46,50,42,38,26,43,32,37,55,56,20,20,11,28,35,
 34,20,12,37,41,55,17,34,19,13,58,32,40,48,11,25,50,18,13,53,34,54,27,58,12,39]
l=[10,20,30,40,50,60]

plt.title("wscube",fontsize=25)
plt.xlabel("python",fontsize=15)
plt.ylabel("No",fontsize=15)
plt.axvline(45,color="r",label="line")             #for drawing line between graph
plt.grid()                                         #for drawing grid

#bins(l) parameter return the binary versions of a specified integer
#range= for range in histogram plot
#cumulative frequency(-1) is used to determine the no. of observation that lie above/below a particular value in a data set. 
#Bottom(left/right/mid) for alignment
#histtype (step/stepfilled/barstacked/bar)
#orientation (vertical and horizontal)
#rwidth for increasing and decreasing the width
#log(true/false)  for converting into log table
#label

#print(plt.hist(no,"auto",(0,100),edgecolor="r"))
print(plt.hist(no,color="r",bins=l,edgecolor="b",linewidth=0.6,cumulative=-1,align="left",histtype="barstacked",orientation="vertical"))
#print(plt.hist(no,"auto",(0,100),edgecolor="b",linewidth=0.8,rwidth=0.8,log="true",label="Python"))

print(plt.legend())                               #for showing line between graph              
print(plt.show())