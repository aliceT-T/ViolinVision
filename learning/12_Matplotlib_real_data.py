import matplotlib.pyplot as plt
import numpy as np 
import pandas as pd
import scipy.optimize

# read csv
# data (x values) needs to be sorted first! 
column_labels = ["Category", "Price", "Quantity"]
expenses = pd.read_csv("sample_data.csv",header=1, names=column_labels) 

expenses["Total"] = expenses["Price"] * expenses["Quantity"]

# Scatter plot of price to number of purchases 
fig, ax = plt.subplots()
for color in ['tab:blue']:
    n = len(expenses)-1 # number of plots is the number of rows in expenses
    x, y = expenses.Price, expenses.Quantity
    ax.scatter(x, y, c=color, label=color, edgecolors='none')

# line of best fit (linear)
a,b = np.polyfit(x, y, 1)
plt.plot(x, a*x+b, color="red", label=f"line of best fit")

# line of best fit (exponential): https://swharden.com/blog/2020-09-24-python-exponential-fit/  
def monoExp(x, m, t, b):
    return m * np.exp(-t * x) + b

p0 = (2000, .1, 50) # start with values near those we expect
params, cv = scipy.optimize.curve_fit(monoExp, x, y, p0)
m, t, b = params

# plot the results
plt.plot(x, y, '.', label="data")
plt.plot(x, monoExp(x, m, t, b))

plt.show() # show the graph 



# Pie chart of categories of purchases 
# Calculate total spending per purchase
expenses["Total"] = expenses["Price"] * expenses["Quantity"]

# Sum spending by category
category_totals = expenses.groupby("Category")["Total"].sum()

# Pie chart
fig, ax = plt.subplots()
ax.pie(
    category_totals.values,
    labels=category_totals.index,
    autopct="%1.1f%%"
)
ax.set_title("Spending by Category")
plt.show()