# Anotações - Fal - Aula 13 - API Lista de Filmes - Python Básico Solyd

## Anotações - Fal - Aula 13 - API Lista de Filmes - Python Básico Solyd.md

### Utilizando APIs e arquivos no formato JSON

#### JSON funciona como um dicionário do Python

* Utilizando a API do OMDb

  * [http://www.omdbapi.com/](http://www.omdbapi.com/)

  Bom para puxar/criar banco de dados

  \`\`\`

import requests

req = None \# pra não reclamar no req

try: \#sempre bom colocar dentro de um try req = requests.get\('[http://www.omdbapi.com/?t=re&apikey=7bb6880e](http://www.omdbapi.com/?t=re&apikey=7bb6880e)'\) except Exception as e: print\("Erro:", e\) exit\(\)

print\(req.text\)

```text

```

import requests import json

def requi\(titulo\): req = requests.get\('[http://www.omdbapi.com/?t=](http://www.omdbapi.com/?t=)' + titulo + '&apikey=7bb6880e' \) filme = json.loads\(req.text\) return filme

def main\(\): sair = False while not sair: op = input\("Escreva o nome de um filme ou SAIR para fechar:\n"\)

```text
    if op == "SAIR":
        sair = True
    else:
        filme = requi(op)
        if filme['Response'] == "False":
            print("Sem Filme")
        else:
            printar_detalhes(filme)
```

## estruturar melhor os dados

def printar\_detalhes\(dicionario\): print\(dicionario\) print\("Título:",dicionario\['Title'\]\) print\("Ano:",dicionario\['Year'\]\) print\("Diretor:",dicionario\['Director'\]\) print\("Atores:",dicionario\['Actors'\]\) for i in dicionario: print\(i,":",dicionario\[i\]\) print\(" "\)

main\(\)

\`\`\`

## \#fim

