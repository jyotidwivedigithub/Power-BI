# Bar Plot...
# SYNTAX:- import matplotlib.pyplot as plt
        # x=[], y=[]        
        # plt.bar(x,y)      
        # plt.show()
        
import matplotlib.pyplot as plt
x=["c+","c++","python","java"]
y=[54,67,89,74]
z=[32,45,63,45]

plt.xlabel("lnaguage",fontsize=15)
plt.ylabel("No.",fontsize=15)
plt.title("wscube",fontsize=15)
#print(plt.bar(x,y))
#print(plt.bar(x,y,width=0.2,color="r"))

#color=c= ["red","blue","green","yellow"]
#align= "edge"/"center"
#edgecolor= "r",linewidth=5
#linestyle= ":" (dot-dot)  for bar outline design
#alpha= (0.4/0.2) for colour transparency.
#label= "popularity" & "wscube"

print(plt.bar(x,y,width=0.2,color="g",align="edge",edgecolor="r",linewidth=5,linestyle=":",alpha=0.6,label="popularity")) 
print(plt.bar(x,y,width=0.2,color="b",align="edge",edgecolor="r",linewidth=5,linestyle=":",alpha=0.6,label="wecube"))

#print(plt.bar(x,y,width=0.2,color="g",label="popularity"))
#print(plt.bar(x,z,width=0.2,color="y",label="wscube"))
print(plt.legend())
print(plt.show())




import matplotlib.pyplot as plt
import numpy as np
x=["c+","c++","python","java"]
y=[54,67,89,74]
z=[32,45,63,45]

width=0.2
p=np.arange(len(x))                 #p=[0,1,2,3]
p1=[j+width for j in p]

plt.xlabel("language",fontsize=15)
plt.ylabel("No.",fontsize=15)
plt.title("wscube",fontsize=15)

print(plt.bar(p,y,width,color="g",label="popularity"))
print(plt.bar(p1,z,width,color="y",label="wscube"))

#xticks(p+width/2)=for shifting language between data
#rotation=for tilled language name

#print(plt.xticks(p+width/2,x,rotation=10))
print(plt.legend())
print(plt.show())




import matplotlib.pyplot as plt
a=["c+","c++","python","java"]
b=[50,60,55,45]
c=[15,35,30,20]

plt.xlabel("lnaguage",fontsize=15)
plt.ylabel("No.",fontsize=10)
plt.title("wscube",fontsize=15)

#barh= for horizontal bar graph
print(plt.barh(a,b,color="g",label="popularity"))
print(plt.barh(a,c,color="y",label="wscube"))
print(plt.legend())
#print(plt.show())