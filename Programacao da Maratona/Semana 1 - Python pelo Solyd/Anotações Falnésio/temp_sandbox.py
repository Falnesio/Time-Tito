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


def dicks (lista_nomes, lista_categorias): 
    names = lista_nomes
    keys= lista_categorias
    matrix={ name.capitalize():{key:[] for key in keys} for name in names}
    return matrix  

relatório = dicks (["Bob", "Luana", "João", "Tany", "Matias"], ["Empregos", "Escolaridade", "Cor", "Idade", "Sexo"])
print(relatório)
