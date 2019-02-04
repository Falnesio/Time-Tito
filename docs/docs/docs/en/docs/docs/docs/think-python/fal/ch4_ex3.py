'''
Wanagashikakerareteru
1. Write a function called square that takes a parameter named t,
which is a turtle. It should use the turtle to draw a square. Write
a function call that passes bob as an argument to square, and then
run the program again.
'''

import turtle
import math


bob = turtle.Turtle()
length = 250

bob.penup()
bob.lt(227)
bob.fd(length/ 2)
bob.rt(227)
bob.pendown()

def square(t, length2):
    for i in range(4):
        t.fd(length2)
        t.lt(90)
def polygon(t, length3, sides):
    #add angle = 360/n here akes code easier to read
    for i in range(sides):
        t.fd(length3)
        t.lt(360/sides)

def this(length):
    polygon(bob, length, 5)
    polygon(bob, length/2, 5)
    polygon(bob, length/4, 5)
    polygon(bob, length/8, 5)
    polygon(bob, length/16, 5)
    polygon(bob, length/32, 5)
    polygon(bob, length/64, 5)
    polygon(bob, length/128, 5)
    polygon(bob, length/256, 5)
    polygon(bob, length/512, 5)

def five_3d(length1):
    bob.lt(36)
    bob.fd((length1/math.sin(math.radians(36))) * math.sin(math.radians(108)))
    bob.lt(108)
    bob.fd(length)
    bob.lt(108)
    bob.fd((length1/math.sin(math.radians(36))) * math.sin(math.radians(108)))
    bob.lt(108)
def now():
    for i in range(4):
        this(length)
        five_3d(length)
        bob.rt(90)

def circle(t, r):
    s = ( 2 * math.pi * r) / 100
    polygon(t, s, 100)
    #bob.lt(90)
    #bob.fd(r * 2)

def arc(t, r, angle):
    s = ( 2 * math.pi * r) / 100
    the_arc = round((angle / 360) * s) * 100
    for i in range(the_arc ):
        t.fd(s)
        t.lt(360/s)
    t.lt(angle)
    t.fd(r)
    t.lt(angle)
    t.fd(r)

#arc(bob, 100, 90)
#circle(bob, 100)

def true_arc(t, r, sides, angle):
    """
    Pede uma tartaruga para desenhar um poligano ou segmento de poligano.
    :param t: (turtle) tartaruga
    :param r: (int/float) tamanho aproximado do centro à borda
    :param sides: (int) quantidade de lados do poligano
    :param angle: (int/float) graus do ângulo do segmento do poligano
    :return:
    """
    length5 = (2 * math.pi * r) / sides
    arc_angle = round((angle/360) * sides)
    t.lt(360/(sides * 2))
    for i in range(arc_angle):
        t.fd(length5)
        t.lt(360/sides)
    t.rt(360 / (sides * 2))

true_arc(bob, 50, 14, 360)
true_arc(bob, 50, 4, 360)


# Accessing docstring
help(true_arc)
print(true_arc.__doc__)


turtle.mainloop()
