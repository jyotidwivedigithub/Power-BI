# Data Visualization:- is a Quick, easy way toconvey concepts in a universal manner.it is the graphical representaton og information and data'
# Plotting Libraries:-
   # 1-Matplotlib:- low level,provides lots of freedom
   # 2-Pandas Visualisation:- easy to use interface,built on Matplotlib
   # 3-Seaborn:- high-level interface,great default styles
   # 4-ggplot:- based on R's ggplot2,uses Grammar of Graphics
   # 5-Plotly:- can create interactive plots

#Matplot:- is a plotting library for the python programming language and its numerical mathematics extension NumPy.
#Matplotlib is a python library used for data visualisation.
#Matplotlib is 2D and 3D plottting python library.
#It wasintroduced by John Hunter in the year 2002.
  #Matplotlib Graphs:- 1-Linear Plot,   2-Scatter Plot,   3-Bar Plot,   4-Stem Plot,   5-Step Plot,    6-Hist Plot,
  #                    7-Box Plot,   8-Pie Plot,   9-Fill_Between Plot.

#Importing Matplotlib:-(import matplotlib.pyplot as plt).....(from matplotlib import pyplot as plt)


import matplotlib.pyplot as plt
x=[2,4,5,6]
y=[2,4,6,3]
print(plt.plot(x,y))
print(plt.show())

x=[2,4,6,8]
y=[3,5,8,6]
c=['r','g','b','p']
#print(plt.bar(x,y,color="c"))
print(plt.bar(x,y))
#print(plt.show())