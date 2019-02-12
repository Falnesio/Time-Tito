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

r = 3.6#float(input("Insert r value: "))
x = 0.2#float(input("Insert starting x value: "))
n = 100000#float(input("Insert number of iterations: "))
i = 0
lista_x = []
lista_y = []

def func(x):
    return r * x * (1 - x)

def doublefunc(x):
    return func(func(x))

while i < n:
    xn2 = x
    x = doublefunc(x)
    print(xn2, x)
    i += 1
    lista_x.append(xn2)
    lista_y.append(x)
    print(i)


scatter(lista_x,lista_y, s=10 )
show()