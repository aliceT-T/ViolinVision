import matplotlib.pyplot as plt
import numpy as np 

x = np.array([1,2,3,5]) # default: 0, 1, 2, ... 
y = np.array([2,4,3,9]) # or just: y=[2,4,3,9] 

plt.figure(figsize=(5,3)) # resize graph 
# have to put this in front!

plt.title("Supply and demand graph", fontdict={"fontname":"Times New Roman", "fontsize":16})
plt.xlabel("Quantity")
plt.ylabel("Price")

plt.plot(x, y, label="Supply", marker="o") # plot the graph 
# the points become circles; or (. for points) or (x) 
# different styles: https://www.w3schools.com/python/matplotlib_markers.asp 

plt.plot(x[:3], x[:3]**2, label="x^2 graph") # can also plot its squared, etc 
# [:3] means to plot the first three points of the x collection 

plt.legend(loc="upper left")  # display labels (ie the label "supply")

plt.savefig("graph.png", dpi=300) # dpi = resolution 

plt.show() # show the graph 