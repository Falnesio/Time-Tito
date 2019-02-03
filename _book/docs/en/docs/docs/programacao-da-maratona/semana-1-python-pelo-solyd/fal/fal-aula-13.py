"""
Created on Sat Dec 29 23:57:43 2018

@author: Fal
"""

import requests
import json


def requi(titulo):
    req = requests.get('http://www.omdbapi.com/?t=' + titulo + '&apikey=7bb6880e' )
    filme = json.loads(req.text)
    return filme


def main():
    sair = False
    while not sair:
        op = input("Escreva o nome de um filme ou SAIR para fechar:\n")

        if op == "SAIR":
            sair = True
        else:
            filme = requi(op)
            if filme['Response'] == "False":
                print("Sem Filme")
            else:
                printar_detalhes(filme)


 #estruturar melhor os dados
def printar_detalhes(dicionario):
    print(dicionario)
    print("Título:",dicionario['Title'])
    print("Ano:",dicionario['Year'])
    print("Diretor:",dicionario['Director'])
    print("Atores:",dicionario['Actors'])
    for i in dicionario:
        print(i,":",dicionario[i])
    print(" ")

main()
