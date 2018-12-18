# -*- coding: utf-8 -*-
"""
Created on Mon Dec 17 21:07:25 2018

Anotações - Aula 2 - Entrada, saída, variáveis e operações matemáticas - Python Básico Solyd.md

Ex.1

@author: Fal
"""

nome = str(input("Escreva seu nome: "))
cpf = str(input("Escreva seu cpf: "))
endereço = str(input("Escreva seu endereço: "))
idade = str(input("Escreva sua idade: "))
altura = str(input("Escreva sua altura: ")) 
telefone = str(input("Escreva seu telefone: "))

print ("Meu nome é", nome, "e tenho", idade, "anos e", altura,"de altura. Eu moro na rua", endereço, "e meu telefone é", telefone, "\n CPF:",cpf)

# ou 

respostas = (input("Escreva separado por ponto e vírgula (;) seu nome, cpf, endereço, idade, altura e telefone \n").split(';')) 
for i in respostas:
    str(i)
print ("Meu nome é", respostas[0], "e tenho", respostas[3], "anos e", respostas[4],"de altura. Eu moro na rua", respostas[2], "e meu telefone é", respostas[5], "\n CPF:",respostas[1])
