# -*- coding: utf-8 -*-
"""
Created on Tue Dec 18 12:43:17 2018

Anotações - Aula 3 - Operadores Lógicos e Estruturas de Decisão - Python Básico Solyd

Ex.1

EXERCÍCIO: Faça um programa que pergunte a idade,
o peso e a altura de uma pessoa e decide se ela 
está apta a ser do Exercito.
Para entrar no Exercito é preciso ter mais de 18 anos,
pesar mais ou igual a 60 kilos e medir mais ou igual a
1,7 metros.

@author: Fal
"""

print ("Quer entrar no exército? Veja se está apta(o)!")
idade = int(input("Qual a sua idade?:  \n"))
peso = float(input("Qual o seu peso em kilos? Utilize ponto ('.'), não vírgula (','):  \n"))
altura = float(input("Qual a sua altura em metros? Utilize ponto ('.'), não vírgula (','):  \n"))

if idade >= 18 and peso >= 60 and altura >= 1.7:
    print ("SUCESSO! Está apta(o) a entrar no Exército!")
else:
    print("Infelizmente não poderá entrar no Exército.")
    if idade < 18:
        print("Idade Insuficiente")
    if peso < 60:
        print("Peso Insuficiente")
    if altura < 1.7:
        print("Altura Insuficiente")