# Anotações - Fal - Aula 9 - Python Orientado a Objeto - Python Básico Solyd

## Anota��es - Fal - Aula 9 - Python Orientado a Objeto - Python B�sico Solyd.md

* Programa��o Orietada por Objetos - oo
  * Programa��o de forma modular
  * Organiza��o dos problemas por n�cleos l�gicos
  * Java for�a a programar dessa forma
  * Python � mais aberto e seguir esse paradigma n�o � necess�rio

### main.py

```text
import veiculo #ou veiculo.py
ou
from veiculo import Veiculo # from aquivo import classe

caminh�o_rosa = Veiculo("rosa", 10, "ford")
print(caminh�o_rose.cor)
print(type(caminh�o_rosa))
```

### veiculo.py

```text
class Veiculo: # ou Veiculo() # a classe descreve o objeto
    def __init__(self, cor, rodas, marca):
        self.cor = cor
        self.rodas = rodas
        self.marca = marca    

    def abastecer(self, litros):
    self.tanque += litros
```

### puxando do mesmo lugar

```text
class Person:
    def __init__(self, name, gender, fun):
        self.name = name
        self.gender = gender
        self.fun = fun

    def talking(self, hours):
        self.fun -= hours

Joe = Person("Joe","Girl",10)

print(Joe.fun)
```

### heran�a -&gt; Carro filho de Veiculo

```text
class Carro(Veiculo):
    def __init__(self, cor, marca, tanque):
        Veiculo.__init__(self,cor, 4, marca, tanque)

    def abastecer(self, litros):
        if self.tanque + litros >= 50:
            self.tanque += (50 - self.tanque)
            print("Tanque Cheio,", self.tanque,"litros")
        else:
            self.tanque += litros
            print(self.tanque)

asd = Carro("mod","mod",20)
asd.abastecer(20)
asd.abastecer(20)

print(asd.rodas)
```

## \#fim

