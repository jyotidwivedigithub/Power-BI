# Subplot
# SYNTAX:-import matplotlib.pyplot as plt
        # x=[],   y=[]
        # plt.subplot(nrows,ncols,index)
        # plt.plot(x,y)
        # plt.show()

import matplotlib.pyplot as plt
x=[1,2,3,4,5]
y=[1,2,3,4,5]

plt.subplot(2,2,1)                                            # graph position 1
plt.plot(x,y,color="r")                                       # line plot

plt.subplot(2,2,2)                                            # graph position 2
plt.pie([1],colors="g")                                       # [1]=1 radius plot...simple pie chart

x1=[10,15,20,25,30]                                           # pie chart
plt.subplot(2,2,3)                                            # graph position 3
plt.pie(x1,y)

x2=["a","b","c","d","f"]                                      # bar plot
y2=[10,20,30,40,50]
plt.subplot(2,2,4)                                            # graph position 4
plt.bar(x2,y2)

plt.show()