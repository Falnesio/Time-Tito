# -*- coding: utf-8 -*-
"""
Created on Sat Dec 22 23:10:18 2018

Anotações - Fal - Aula 7 - Métodos e Funções - Python Básico Solyd.md

Ex. 1

EXERCÍCIO: Escreva uma função que receba um objeto de coleção
e retorna o valor do maior número dentro dessa coleção
faça outra função que retorna o menor múmero dessa coleção
    

@author: Fal
"""

def maior(lista):
    return max(lista)

def menor(lista):
    return min(lista)

print("menor:",menor([2,3,4,5,6,7,8]))
print("maior:",maior([2,3,4,5,6,7,8]))

