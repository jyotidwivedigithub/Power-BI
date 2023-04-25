# Stack/Area Plot
# SYNTAx:-import matplotlib.pyplot as plt
        # x=[],   y=[]
        # plt.stackplot(x,y)
        # plt.show()


import matplotlib.pyplot as plt
x=[1,2,3,4,5]
area1=[1,3,4,6,5]
area2=[2,3,4,5,2]
area3=[2,4,3,6,5]
l=["area1","area2","area3"]

plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title("Python")

#baseline="zero"/"sym"/"wiggle"..it represent area

#plt.stackplot(x,area1)                              # For single Stack Plot

#for multiple stack plot
plt.stackplot(x,area1,area2,area3,labels=l,colors=["r","g","b"])    
plt.legend(loc=2)                            # for showing lavel and location of label
#plt.grid()
plt.show()