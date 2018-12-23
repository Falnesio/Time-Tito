# -*- coding: utf-8 -*-
"""
Created on Tue Dec 18 23:29:46 2018

@author: Fal
"""

# Lista ou list (número modificável de ítens ordenados)
lista_nomes = ["Fernando", "Susana"]

# Tupla ou tuple (mesmo número finito de dados ordenados e não modificáveis)
tupla_nomes = ("Fernando", "Susana")

# Dicionário ou dict (ítens divididos por vírgulas)
dicionario_cadastro = {"nome" : "Falnésio", "idade" : 36}
print(dicionario_cadastro.keys())

# Conjunto ou set (não tem ítens repetidos e não é ordenado)
conjunto = {"Fal", "Marcela"}


x = "Maria"
if x in conjunto:
    print("found")
else:
    print("not found")
    
    
x = []
'''
criar múltiplos dicionários
'''
def dicks (length, lista): 
    names = []
    for i in range(length):
        names.append(str(i))
        print(type(i))
    for i in names:
        print(type(i))
    #names=["lloyd", "alice", "tyler"]
    keys= lista
    steven={ name.capitalize():{key:[] for key in range(5)} for name in names}
    print(steven)  

print(dicks(7, ["apple", "banana"]))


'''
for i in range(58):
    x.append(dicionario_cadastro)
j = 0
for i in x:
    i["indice"] = j
    print(i)
    j += 1
    
print(x)
'''