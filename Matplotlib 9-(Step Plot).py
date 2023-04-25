# Step Plot                 
# SYNTAx:-import matplotlib.pyplot as plt
        # x=[],   y=[]
        # plt.step(x,y)
        # plt.show()

import matplotlib.pyplot as plt
x=[1,2,3,4,5]
y=[2,4,5,3,2]

plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title("Python")

#marker="o"/"*"/"+"/"#".....
#ms(markersize)=10
#mfc(marker face color)="g"

plt.step(x,y,color="r",marker="o",ms=10,mfc="g",label="Python")
plt.legend(loc=2)                                # for showing lavel and location of label
plt.grid()
plt.show()
