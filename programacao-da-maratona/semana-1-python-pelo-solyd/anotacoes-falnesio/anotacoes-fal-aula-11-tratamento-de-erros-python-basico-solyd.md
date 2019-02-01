# Anotações - Fal - Aula 11 - Tratamento de Erros - Python Básico Solyd

\# Anotações - Fal - Aula 11 - Tratamento de Erros - Python Básico Solyd.md

```text
try:
    a = 1200 / 0
except:
   print("ERRO!")

try:
    a = 1200 / 0
except Exception: #qualquer excessão
   print("ERRO!")

try:
    a = 1200 / 0
except ZeroDivisionError:
    print("Erro, divisão por zero")
except NameError:
    print("Erro de nomeamento)

try:
    a = 1200 / 0
except Exception as erro: #qualquer excessão
   print("ERRO:", erro)
```

## tentar depois de um tempo

```text
import time
def abre_arquivo():
    try:
        open("olha.txt")
        return arquivo
    except Exception as erro:
        print("ERRO:", erro)
        return False

while not abre_arquivo():
    try:
        print("Tentando abrir o arquivo")
        time.sleep(5)
print("Arquivo abriu")
```

## \#fim

