from pylab import *

r = float(input("Insert r value: "))
x1 = 0.3
x2 = 0.300001
n = 500
i = 0
x1_menos_x2 = []
lista_i = []

while i < n:
    x1 = r * x1 * (1 - x1)
    x2 = r * x2 * (1 - x2)
    i += 1
    lista_i.append(i)
    x1_menos_x2.append(abs(x1 - x2))

print("Média da diferença absoluta para tragetória dos valores iniciais: ",
      sum(x1_menos_x2) / n)
print("x1: ", x1)
print("x2: ", x2)
print(x2 == x1)
plt.plot(lista_i, x1_menos_x2, c="b", marker="o", linestyle='None')
plt.show()
