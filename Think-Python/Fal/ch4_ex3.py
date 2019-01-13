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
length = 500

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
    for i in range(sides):
        t.fd(length3)
        t.lt(360/sides)

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

five_3d(length)

turtle.mainloop()
