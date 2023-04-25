# SaveFig....how to save graph in external file
# SYNTAX:-import matplotlib.pyplot as plt
        # x=[],   y=[]
        # plt.plot(x,y)
        # plt.savefig(fname)                 fname is the file name to save
        # plt.show() 

import matplotlib.pyplot as plt
x=[1,2,3,4]
y=[2,3,4,5]

plt.plot(x,y,color="r")

#dpi(dot per inch )=(1000/2000/30000...)how many dots we want in line parameter
#facecolor=baundary color of graph
#.pdf/jpg/..for saving file formate
#Transparence...(True/False)
#bbox_inches="tight"...to change boxsize

#plt.savefig("line")                           #file save in .png formate by default
#plt.savefig("line1",dpi=5000)
#plt.savefig("line2",dpi=5000,facecolor="g")
#plt.savefig("line3.pdf",dpi=5000,facecolor="g")
#plt.savefig("line4",dpi=5000,facecolor="g",transparent="True")
plt.savefig("line5",dpi=5000,facecolor="g",transparent="True",bbox_inches="tight")

plt.show()

