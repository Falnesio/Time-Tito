# Anotações - Fal - Aula 2 - Entrada, saída, variáveis e operações matemáticas - Python Básico Solyd

\# Anotações - Aula 2 - Entrada, saída, variáveis e operações matemáticas - Python Básico Solyd.md

* Primeiro exercício da aula "aula2-entrada-e-saida.py" será "Fal - Aula 2 - Ex.1.py".
* Ensinando como executar do cmd do windows
* Coisas programadas no Python

```text
print ("Hello, World!")
print("Segundo print")

# Print pulando linha
print("Hello, world!\nSegundo print" )
# Print come tab
print("Hello, world!\tSegundo print" )

# Incluir um texto (string) a uma variável e imprimir variável
nome = "Falnésio"
print(nome)

# mostar o tipo da variável
print(type(nome))

# ou 
tipo_nome = type(nome)
print(tipo_nome)

# para um número
idade = 26
tipo_idade = type(idade)
print(idade)
print(tipo_idade)

# Mostrando floating point
altura = 1.78
tipo_altura = type(altura)
print(altura)
print(tipo_altura)

# Contatenar: multiplas coisas no print
print (nome, "tem", idade, "anos e", altura, "de altura")

print (nome + "tem" + str(idade) + "anos e" + str(altura) + "de altura")
print (nome + " tem " + str(idade) + " anos e " + str(altura) + " de altura")

# ou

frase = nome + " tem " + str(idade) + " anos e " + str(altura) + " de altura"
print (frase)

# Input
nome = input("Escreva seu nome: ")
idade = input("Escreva sua idade: ")
altura = input("Escreva sua altura: ")
frase = nome + " tem " + str(idade) + " anos e " + str(altura) + " de altura"
print (frase)

# operações
numero1 = 3
numero2 = 2

resultado = numero1 / numero2 + 4
print(resultado) 

# resultado elevado a 2
resultado **= 2
print(resultado)

# resultado somado 1
resultado += 1
print (resultado)

# ou
resultado = resultado + 1
print(resultado)
```

## \#fim

