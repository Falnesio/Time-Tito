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
        try:
            for i in filme['Search']:
                lista_de_midia.append(i)
        except:
            return filme
        return filme



lista_de_midia = []


def main():
    sair = False
    while not sair:
        op = input("Escreva o nome de um filme ou SAIR para fechar:\n")

        if op == "SAIR":
            sair = True
        else:
            for i in range(1,100,1):
                i = str(i)
                filme = requi(op,i)
                try:
                    printar_detalhes(filme)
                except:
                    break
        with filmes as f:
            json.dump(lista_de_midia, f)
        with open('filmes.json') as f:
            dict = json.load(f)
            print(dict)
        print("done")
        print(" ")


 #estruturar melhor os dados
def printar_detalhes(dicionario):
    for i in dicionario:
        #print(i,":",dicionario[i])
        print(" ")


main()
