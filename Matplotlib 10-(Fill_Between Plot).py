# Fill_Between Plot
# SYNTAX:-import matplotlib.pyplot as plt
        # x=[],  y=[]
        # plt.plot(x,y)
        # plt.fill_between()
        # plt.show()

import matplotlib.pyplot as plt
x=[1,2,3,4,5]
y=[1,2,4,3,5,]

plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title("Python")

plt.plot(x,y,color="g")
#plt.fill_between(x=[2,3],y1=2,y2=3)
#plt.show()



import matplotlib.pyplot as plt
import numpy as np
x=np.array([1,2,3,4,5])
y=np.array([2,4,3,5,6])

plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title("Python")

#where..for compress the area between x and y
#alpha=0.4  for transparency 
plt.fill_between(x,y,color="g",where=(x>=2) & (x<4),alpha=0.4)    
plt.show() 

