# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 00:07:41 2018

Anotações - Fal - Aula 5 - Estruturas de Laço (For e While) - Python Básico Solyd.md

Ex.1

EXERCÍCIO: Faça um programa que leia a quantidade de pessoas que
serão convidadas para a festa.
Após isso o programa irá perguntar o nome de todas pessoas e colocar 
numa lista de convidados
Após isso irá imprimir todos os nomes da lista

@author: Fal
"""

convidados_qnt = range(int(input("Escreva o número de convidados:\n")))
convidados = []
for i in convidados_qnt:
    convidados.append(input("Escreva o nome do próximo convidado:\n"))
#print("\nConvidados:", convidados)
# ou
print("\nConvidados:")
j = 1
for i in convidados:
    print(j,"-", i)
    j += 1

