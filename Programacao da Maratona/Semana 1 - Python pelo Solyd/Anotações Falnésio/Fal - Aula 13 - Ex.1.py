"""
Created on Sat Dec 29 23:57:43 2018

Ex.1

EXERCÍCIO:

@author: Fal
"""

import requests
import json
filmes = open("filmes.json", "w+")
filmesr = open("filmes.txt", "r")



def requi(titulo,pagina):
    req = requests.get('http://www.omdbapi.com/?s=' + titulo + '&apikey=7bb6880e'+'&page='+pagina )
    filme = json.loads(req.text)

    if filme['Response'] == 'True':
            for i in filme['Search']:
                lista_de_midia.append(i)
    else:
        return False
        print("Existem", filme['totalResults'], "mídias associadas.")



lista_de_midia = []


def main():

    sair = False
    while not sair:
        filmes = open("filmes.json", "w")
        #lista_de_midia = []
        op = input("Escreva o nome de um filme ou SAIR para fechar:\n")

        if op == "SAIR":
            sair = True
        else:
            for i in range(1,100,1):
                i = str(i)
                filme = requi(op,i)
                if filme == False:
                    break
                try:
                    print("Olhando a página:",i)
                except:
                    break
        printar_detalhes(lista_de_midia)
        with filmes as f:
            json.dump(lista_de_midia, f)
        print("done")
        print(" ")
        ver_mais = input("Quer ver detalhes (s) ou (n)?\n")
        if ver_mais == 's':
            with open('filmes.json') as f:
                dict = json.load(f)
                print(dict)
        print("")


 #estruturar melhor os dados
def printar_detalhes(dicionario):
    for i in dicionario:
        print(i["Title"])



main()
