'''
(for experts) The “second-return map” of the logistic map is defined as

x_{n+2}=(f º f)(x_{n})

Code up your own cobweb diagram using the second-
return map and play around with it.  How is this different than the cobweb plot
in this app?  How do the features of the second-return map align with known
features  of  the  original  logistic  map?   Find  a  period  2  orbit  in  the  original
map and then use that same
r
value in the second-return map?  What kind of
dynamics are these?  Does this make sense?
'''

from pylab import *

r = float(input("Insert r value: "))
x = float(input("Insert starting x value: "))
n = float(input("Insert number of iterations: "))
i = 0
lista_x = []
lista_y = []

while i < n:
    xn2 = x
    x = r*(r*x*(1-x))*(1-(r*x*(1-x)))*x
    i += 1
    lista_x.append(x)
    lista_y.append(xn2)

    scatter(lista_x,lista_y, s=100 ,marker='o')

show()