# Anotações - Fal - Aula 4 - Strings e Listas - Python Básico Solyd

\# Anotações - Fal - Aula 4 - Strings e Listas - Python Básico Solyd.md

* Programação :

```text
# Listas e strings funcionam semelhantemente
# O índice do primeiro item é zero.
    # lista_nomes[0] é "João"
# Quando contando de trás pra frente lista_nomes[-1] é "Fal"

frase = "Oi, tudo bem?"
lista_nomes = ["João", "Maria", "Diego", "Fal"]

print(frase)
print(frase[0])
print(type(frase))
print(type(lista_nomes))
print(lista_nomes[2])

# Tem como selecionar partes de uma lista/string

print(frase[0:2]) # Imprime do zero até o 1
print(frase[0:13:1]) # De zero a treze de um a um
print(frase[0:13:2]) # De zero a treze de dois a dois
print(frase[-1:-4:-1]) # De trás pra frente de um em um
print(frase[::-1]) # Imprime tudo mas de trás pra frente

# Adicionar no final da lista/frase 

lista_nomes.append("qualquer string nova")
print(lista_nomes)

# Inserir em determinada posição

lista_nomes.insert(1, "Ronaldo")
print(lista_nomes)

# Trocar itens

lista_nomes[0] = "Josefino"
print(lista_nomes)

# Remover da lista

lista_nomes.remove("item dentro da lista/frase")
print(lista_nomes)

# Remover tudo na lista

lista_nomes.clear()
print(lista_nomes)

# Contar quantidade de vezes que item aparece em uma lista

print(lista_nomes.count("Fal"))
quantos_fal = lista_nomes.count("Fal")
print(quantos_fal)

# Contar quantidade de itens dentro de uma string ou lista
print(lista_nomes.len[3])

# Imprimir o último item e retirar de lista

print(lista_nomes.pop())
print(lista_nomes)

# etc. tipo split e juntar frases

print(frase.lower()) # não é permanente
print(frase)
frase = frase.lower() # é permanente
# não precisa transformar a variável original, guarda frase alterada em outra variável
frase_low = frase.lower()
print(frase)
```

## \#fim

