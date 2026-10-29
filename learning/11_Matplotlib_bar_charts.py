import matplotlib.pyplot as plt

labels = ["A","B","C"]
values = [1,4,2]

bars = plt.bar(labels, values)

bars[0].set_hatch("*") # fill the bar with stars 

plt.show() # show the graph 