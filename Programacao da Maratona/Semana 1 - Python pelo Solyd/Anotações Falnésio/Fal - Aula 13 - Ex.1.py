"""
Created on Sat Dec 29 23:57:43 2018

Ex.1

EXERCÍCIO:

@author: Fal
"""

import requests
import json
filmes = open("filmes.json", "w+")



def requi(titulo,pagina):
    req = requests.get('http://www.omdbapi.com/?s=' + titulo + '&apikey=7bb6880e'+'&page='+pagina )
    filme = json.loads(req.text)

    if filme['Response'] == 'True':
            for i in filme['Search']:
                lista_de_midia.append(i)
    else:
        return False
        print("Existem", filme['totalResults'], "mídias associadas.")

def filme_especifico(titulo):
    titulo = titulo.replace(" ", "+")
    req = requests.get('http://www.omdbapi.com/?t=' + titulo + '&apikey=7bb6880e')
    movie = json.loads(req.text)
    if movie['Response'] == 'True':
        for i in movie.keys():
            print(i,":",movie[i])
        arquivo_movie = open(titulo.replace(" ", "_")+"_filmesp_"+ ".json", "w")
        with arquivo_movie as f:
            json.dump(movie, f)
    else:
        return False



lista_de_midia = []


def main():

    sair = False
    while not sair:
        filmes = open("filmes.json", "w")
        op = input("Escreva o nome de um filme ou SAIR para fechar:\n")

        if op == "SAIR":
            sair = True
        else:
            op_filmes = open(op.replace(" ", "_") + ".json", "w")
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
        with op_filmes as f:
            json.dump(lista_de_midia, f)
        lista_de_midia.clear()
        print("done")
        print(" ")
        ver_mais = input("Quer ver detalhes (s) ou (n)?\n")
        if ver_mais == 's':
            with open('filmes.json') as f:
                dict = json.load(f)
            filme_exato = input("Algum filme em particular da lista (s) ou (n)?\n")
            if filme_exato == 's':
                try:
                    qual_filme = input("Escreva exatamente como na lista:\n")
                    filme_especifico(qual_filme)
                except:
                    print("Escreveu Errado")
            else:
                for i in dict:
                    for key in i.keys():
                        print(key, ":", i[key])
                    print("----------")
                    print(" ")
        else:
            print("")
        print("")


 #estruturar melhor os dados
def printar_detalhes(dicionario):
    for i in dicionario:
        print(i["Title"])



main()
