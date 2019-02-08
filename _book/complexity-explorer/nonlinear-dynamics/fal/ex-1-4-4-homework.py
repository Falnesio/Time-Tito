import matplotlib.pyplot as plt
import numpy

'''
rplot = numpy.arange(2.999999, 3, 0.0000001)
x = 0.2
n = 10000000
mapas = []


for r in rplot:
    i = 0
    print(r)
    lista_x = []
    while i < n:
        x = r * x * (1 - x)
        lista_x.append(x)
        i += 1
        if i == n:
            mapas.append(lista_x)
    #plt.show()

for lista in mapas:
    #plt.subplot(len(mapas), 1, mapas.index(lista) + 1)
    plt.plot(range(n), lista, 'o')
    plt.show()
'''
n = 100
r = 2.999999
i = 0
x = 0.2
print(r)
lista_x = []
while i < n:
    x = r * x * (1 - x)
    lista_x.append(x)
    i += 1

plt.plot(range(n), lista_x, 'o')
plt.show()