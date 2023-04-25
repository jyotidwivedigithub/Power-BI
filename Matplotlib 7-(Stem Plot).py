# Stem Plot
# SYNTAX= import matplotlib.pyploy as plt
        # x=[],   y=[]
        # plt.stem(x,y)
        # plt.show()

import matplotlib.pyplot as plt
x=[1,2,3,4,5]
y=[2,3,4,5,6]

#linefmt=":" for linestyle
#markerfmt="+r"/"*g"/"#y".....for marker design and color
#basefmt="g"..for changing baseline color
#bottom=1/2/3...starting point of baseline
#label="Python"
#orientation+"horizontal"/"vertical" 
#use_line_collection=True/False...for changing line color

plt.stem(x,y,linefmt=":",markerfmt="*r",basefmt="g",bottom=1,label="Python",
        use_line_collection=False,orientation="vertical")

plt.legend()
plt.show()