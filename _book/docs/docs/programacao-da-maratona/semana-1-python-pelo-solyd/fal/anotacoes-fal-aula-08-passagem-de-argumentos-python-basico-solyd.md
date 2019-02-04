# Anotações - Fal - Aula 8 - Passagem de Argumentos - Python Básico Solyd.md 

* Importar Biblioteca

* Abrir programa pelo cmd do winddows

```

import sys

argumentos = sys.argv


def soma(a,b):
    return a + b

def sub(a,b):
    return a - b

if argumentos[1] == "soma":
    resp = soma(float(argumentos[2]), float(argumentos[3]))
elif argumentos[1] == "sub":
    resp = sub(float(argumentos[2]), float(argumentos[3]))
elif argumentos[1] == "help":
    resp ="fnsaofeijaeifjawiejfawiejfoçiaiwjefoçiaweçifoaweçfoiajweoiifjçaowefi"
    
print(resp)

```

# #fim
