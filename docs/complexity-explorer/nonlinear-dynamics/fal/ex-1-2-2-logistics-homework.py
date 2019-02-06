from pylab import *

r = float(input("Insert r value: "))
x = float(input("Insert starting x value: "))
n = float(input("Insert number of iterations: "))
i = 0
lista_i = []
lista_y = []

while i < n:
    x = r * x * (1 - x)
    i += 1
    lista_i.append(i)
    lista_y.append(x)

print(x)
scatter(lista_i, lista_y, s=100, marker='o')
show()
