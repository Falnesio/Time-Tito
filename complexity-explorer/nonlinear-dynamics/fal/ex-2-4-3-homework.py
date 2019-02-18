'''
Question 1
    Write a program to construct a bifurcation diagram for the logistic map.  (Hint: this should be a loop that calls your logistic map program from Unit 1.3.)  Your program should take the following arguments:
        An initial condition x0
        An rmin and an rmax that specify a range of r values for the x-axis of your bifurcation plot
        An rstep, which specifies how many "slices" your plot has
        A number n of total iterates to perform
        A number k of total iterates to discard without plotting (i.e., to remove the transient)

    The output should be a plot of the logistic map bifurcation diagram for a range of r.

    Check your program by constructing a bifurcation plot for with a step size of 0.01.  For each r, construct a 1000-iterate trajectory from x0 = 0.2, and discard the first five points -- i.e., plot x5 to x1000 for each r.  The overall structure will look similar to that of Figure 1 below (although not quite identical; we'll get to that later in this quiz).
'''

import matplotlib.pyplot as plt
import numpy as np


# Setup values
r = [0, 4]
steps = 10000
x_initial = 0.2
transiente = 490

def func(x, r):
    n = 500
    new_list = []
    for i in range(n):
        x = r - (x ** 2)
        if i > transiente:
            new_list.append(x)
    return new_list

x_list = []
rvalues = np.linspace(start=r[0], stop=r[1], num=steps)
p = 0

for i in rvalues:
    x_list.append(func(x_initial, i))
    print(p/steps * 100, "%")
    p += 1

plt.plot(rvalues, x_list, 'o', markersize=0.5)
plt.show()