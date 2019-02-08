import matplotlib.pyplot as plt

rplot = [3.828, 3.8281, 3.8282, 3.8283, 3.8284, 3.8285]
x = 0.2
n = 2500
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
    plt.plot(range(n), lista_x, c="b", marker="o", linestyle='None')
    #plt.show()

for lista in mapas:
    plt.subplot(6, 1, mapas.index(lista) + 1)
    plt.plot(range(n), lista, 'o')
plt.show()

