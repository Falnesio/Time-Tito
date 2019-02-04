# Anotações - Fal - Aula 9 - Python Orientado a Objeto - Python Básico Solyd.md

* Programação Orietada por Objetos - oo
	* Programação de forma modular
	* Organização dos problemas por núcleos lógicos
	* Java força a programar dessa forma
	* Python é mais aberto e seguir esse paradigma não é necessário

###### main.py
```

import veiculo #ou veiculo.py
ou
from veiculo import Veiculo # from aquivo import classe

caminhão_rosa = Veiculo("rosa", 10, "ford")
print(caminhão_rose.cor)
print(type(caminhão_rosa))

```

###### veiculo.py
```
class Veiculo: # ou Veiculo() # a classe descreve o objeto
    def __init__(self, cor, rodas, marca):
        self.cor = cor
        self.rodas = rodas
        self.marca = marca    

    def abastecer(self, litros):
	self.tanque += litros

```

###### puxando do mesmo lugar
```
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

###### herança -> Carro filho de Veiculo
```
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


# #fim