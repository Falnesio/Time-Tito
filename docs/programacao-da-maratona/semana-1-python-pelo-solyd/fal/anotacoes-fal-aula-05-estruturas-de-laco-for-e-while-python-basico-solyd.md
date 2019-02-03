# Anotações - Fal - Aula 5 - Estruturas de Laço (For e While) - Python Básico Solyd.md

* Programação

###### for
```

nomes = ["Fal", "Bob", "Luis", "Gabby", "Clarice", "Douglas"]

# Estrutura de laço para iterações

for nome in nomes:
    print(nome)

# Criar lista de números

lista_de_numeros = range(5) # são 0,1,2,3,4

# Criar lista de um número a outro de tant em tanto

lista_de_numeros = range(0, 20, 3) # de 0 a 20 de 3 em 3

#para imprimir cada

for número in lista_de_numeros:
    print(números)

# Imprimir os nomes dentro de 0 a 3 usando range; 
# já tendo lista certinha não precisa dessa complicação
for i in range(4):
    print(nomes[i])
# isso pode dar erro quando range é maior que tamanho da lista
for i in range(len(nomes)):
    print(nomes[i])


```

###### while

```

i = 0
while i < 10: # enquanto i for menor que 10 roda isso
    print("i ainda é menor que 10", i)
    i += 1 # adciona 1 a i
print("fin", i)

i = 0
i += 10 # i é igual a 10
i += 10 # //  //  //  20

# len manual
lista_frutas = ["pera", "uva", "maçã", "manga", "goiaba"]

contador

for fruta in lista_frutas:
    contador += 1

print(contador)

# break sai do while

numero = 0
while True:
    print(numero)
    if numero == 20:
        break
    numero += 1
print("Saiu do while com break")

```

# #fim
