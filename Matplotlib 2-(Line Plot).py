# Line Plot...

import matplotlib.pyplot as plt
x=[2,4,5,6]
y=[2,4,6,3]

plt.xlabel("wscube",fontsize=10)
plt.ylabel("student",fontsize=10)
plt.title("Good",fontsize=15)

print(plt.plot(x,y))
print(plt.show())