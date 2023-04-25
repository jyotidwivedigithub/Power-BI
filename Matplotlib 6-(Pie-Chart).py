# Pie Plot...
# SYNTAX:-import matplotlib.pyplot as plt  
        # x=[] 
        # plt.scatter(x)  
        # plt.show(x)

import matplotlib.pyplot as plt
x=[10,20,40,30]
y=["c","c++","java","python"]
ex=[0.2, 0.0, 0.0, 0.0]
c=["r","y","b","g"]

#explode= separately show the specific value
#autopct("%0.1f%%")= showing % in given parameters..(0.1=0, 0.2=00, 0.3=000)
#shadow=True
#radius(1,2) for increasing or deceasing the size of chart
#labeldistance(1.2) for the distance of label(here-y) from the chart
#startangle(0,90,180,45,..) for to set the starting position
#textprops={"fontsize": 15}...for fixing the size of font..it always should be in list form
#counterclock(true/false)...for rotating the chart
#wedgeprops={"linewidth": 6, "edgecolor": :"r"}..to set the width of line and color..edgecolor is optional
#center(1,2) for changing the cente
#rotatelabels(True/False)


#print(plt.pie(x,labels=y,explode=ex,colors=c,shadow=True))
#print(plt.pie(x,labels=y,colors=c,autopct="%0.1f%%",radius=0.8,labeldistance=1.4,startangle=90
 #    ,textprops={"fontsize": 15},wedgeprops={"linewidth": 2,"edgecolor":"m"},center=(1,0),rotatelabels=False
 #    ))
#plt.title("WSCube Tech")
#plt.legend(loc=2)            #for giving the label in chart  loc=location
#print(plt.show())



#Dot pie chart
#plt.pie([1])
#print(plt.show())


#Donut / multiple pie chart
import matplotlib.pyplot as plt
x=[10,20,40,30]
x1=[30,40,20,10]
y=["c","c++","java","python"]
c=["r","y","b","g"]

plt.pie(x,labels=y,radius=1.5,colors=c)
#plt.pie(x1,radius=0.5)
plt.pie([1],colors="w")                    #[1]=1 radius plot
print(plt.show())



import matplotlib.pyplot as plt
x=[10,20,40,30]
x1=[30,40,20,10]
y=["c","c++","java","python"]
c=["r","y","b","g"]

plt.pie(x,labels=y,radius=1.5)
cr=plt.Circle(xy=(0,0),radius=1,facecolor="w")
plt.gca().add_artist(cr)
plt.show()