# Axis Matplotlib Plot....change axis in matplotlib
# Function in Axis Matplotlib
       # xticks(),   yticks(),    xlim(),   y(lim) axis in Matplotlib Python

import matplotlib.pyplot as plt
x=[1,2,3,4,5]
y=[3,1,6,2,4]
l=["c+","c++","python","java","cobol"]

#xticks(), yticks(),...used to change data
#xlim(),   ylim()......increase/decrease axis limit

plt.plot(x,y)

#plt.xticks(x,labels=l)        # change in x-axia
#plt.yticks(x)                 # change in y-axis

#plt.xlim(0,7)                # increase/decrease x-axis limit
#plt.ylim(0,7)                # increase/decrease y-axis limit

plt.axis([0,10,0,7])         # x-axis=10,    y-axis=7.........10 & 7 is the range in x,y axis
plt.show()