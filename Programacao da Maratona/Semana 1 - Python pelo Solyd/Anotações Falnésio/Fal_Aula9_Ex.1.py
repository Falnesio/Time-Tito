# -*- coding: utf-8 -*-
"""
Created on Tue Dec 25 02:58:43 2018

Ex.1

EXECÍCIO: Crie um software de gerenciamento bancário.
Esse software poderá ser capaz de criar clientes e contas
Cada cliente possui nome, cpf, idade
Cada conta possui um cliente, saldo, limite
e poderá depositar, sacar e consultar saldo


@author: Fal
"""

import sys
import re
loja = sys.argv
F  = open("clientes.py", "r+")
print ("Arquivo dos clientes",F,"\n")

clientes = []
contas = []

class contas:
    def __init__(self,cliente,saldo, limite):
        self.cliente = cliente
        self.saldo = saldo
        self.limite = limite
        
    def sacar(self, grana):
        if grana > self.limite:
            if self.saldo - grana < 0:
                self.saldo = 0
                print("Saldo insuficiente, sacou apenas", ( self.saldo))
                print("Saldo zerado!")
            else:
                self.saldo -= grana
                print("Sacou", grana)                   

class cliente:
    def __init__(self, nome, cpf, idade):
        self.nome = nome
        self.cpf = cpf
        self.idade = idade

 
def novo():    
    numero_de_entradas = int(input("Quantos clientes gostaria de cadastrar?\n"))
    print(numero_de_entradas,"pessoas")
    p = 0
    novos_clientes = []
    

    while p < numero_de_entradas:
        a = input("Digite o nome do cliente: ")
        novos_clientes.append(a)
        p += 1
        print(novos_clientes)
        print("")

    for pessoa in novos_clientes:
        print("Qual a idade de",pessoa, "?")
        idade = int(input())
        print("Qual o cpf de", pessoa,"?\n")
        cpf = int(input())
        pessoa = cliente(pessoa, cpf, idade)
        clientes.append(pessoa)
        clientela = str(clientes) 
        print(clientela)
        F.write(clientela)

      
def cli():
    a = input("Escreva 'todos' ou o número do cliente específico: ")
    if a == "todos":
        print(F.read())
    else:
        from clientes import fregues
        d = fregues
        print(d)
        
    
try:
    if loja[2] == "novo":
        novo()
    elif loja[2] == "cli":
        cli()
    elif loja[2] == "a":
        print("deu certo")
except:
    print("Programa pronto pra receber comando...")


