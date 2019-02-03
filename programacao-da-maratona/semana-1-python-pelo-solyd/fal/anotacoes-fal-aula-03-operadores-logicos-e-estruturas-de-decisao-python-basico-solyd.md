# Anotações - Aula 3 - Operadores Lógicos e Estruturas de Decisão - Python Básico Solyd

 * Operações lógicas e if/else
 * Dado booleano True/False ou 1/0
 * Programação:
```
var_verdade = True
var_falso = False

print(type(var_verdade), type(var_falso))
print(var_verdade, var_falso)

# Um igual ("=") é para atribuir valor, dois ("==") é para comparações

True == True
True == False
False == False

# Comparação maior que ou menor que
print (1 > 1)
print (3 < 2)

# Comparação maior igua, menor igual
print (1 >= 2)
print (2 <= 3)

# Comparação não igual
print (1 != 1)
print (1 != 2)
print (1 = (not 1))
print (1 != (not 1))
print (1 == (not 2))
print (1 != (not 2))

# Comparação múltipla "e" ("and") e "ou" ("or")
print (1 = 1 and 1 != 1) # Todos são verdadeiro
print (1 = 1 and 1 != 2)
print (1 = 1 or 1 != 1) # Ao menos um é verdadeiro
print (1 = 2 or 1 != 1 )


if var_verdade == True: #se var_verdade for igual a True faça o seguinte
    print("var_verdade é verdadeiro")  #imprimir var_verdade é verdadeiro
# tudo "indentado com quatro espaços estará dentro do "if".

a = 2
b = 1
p = input("0 ou 1")

if ((a > b and ("a" == "a")) or (p == True):
    print (a, "é maior do que", b)
else:
    print (b, "é maior ou igual a", a)

print("Opções:\n1 = Escreve Falnésio\n2 = Escreve Clarinha\n3 = Escreve Lucas")
opção = input("Escolha uma opção: ")
if opção == "1":
    print("Falnésio")
elif opção == "2":
    print("Clarinha")
elif opção == "3":
    print("Lucas")
else:
    print("Opção não existe!")

```

# #fim
