# Working with text in Matplotlib Python...........add text on plots
  # text:-Add text at an artibitrary location of the Axes.
  # annotate:-Add an annotation, with an optional arrow,at an arbitrary location of Axes.
  # xlabel:-Add a label to the Axes's x-axis.
  # ylabel:-Add a label to the Axes's y-axis.
  # title:-Add title to the axes.

import matplotlib.pyplot as plt
x=[1,2,3,4,5]
y=[2,5,3,6,3]


plt.plot(x,y)

plt.xlabel("Days",fontsize=15)
plt.ylabel("Python",fontsize=15)
plt.title("WSCube")

#style..fontstyle
#bbox={"facecolor":"red"}...always should b in dictionary formate
#xy=(3,2)..to pointout any..position/area
#xytext=(4,4)...is used to fix text position
#arrowprops=dict(facecolor="b",shrink=100).......to add arrow property...always should be in dictionary formate
#legend..it has (0-10 position)..used to represent/show the label/data in text formate.
#framealpha=0.5...for transparency
#shadow(True/False)

#plt.text(2,5,"java",fontsize=10,style="italic",bbox={"facecolor":"red"})     #(2,5) is the position of "jave"
#plt.annotate("Python",xy=(3,2),xytext=(4,4),arrowprops=dict(facecolor="black",shrink=100))

plt.legend(["up"],loc=2,facecolor="red",edgecolor="y",framealpha=0.5,shadow="true")
plt.show()
