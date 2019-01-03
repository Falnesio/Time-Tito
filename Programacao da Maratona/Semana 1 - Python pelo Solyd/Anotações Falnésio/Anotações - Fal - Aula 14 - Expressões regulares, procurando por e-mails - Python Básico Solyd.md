# Anotações - Fal - Aula 14 - Expressões regulares, procurando por e-mails - Python Básico Solyd.md


```
 regular expressions, regex
# importar biblioteca

import re

string_de_test = "O gato é bonito!"

# Primeiro cria-se um padrão a ser procurado
# colocar "r" antes das aspas torna string em raw_string
padrão = re.search(r'',string_de_test)
print(padrão)
## span = (x, y) sendo x = tamanho da busca, y = tamanho de item encontrado

# Para verificar o que foi obtido:
print(padrão.group())

## sobre RAW strings
print("Hi there!\nHow are you?")
print(r"Hi there!\nHow are you?")

## procurando padrões exemplos
padrão = re.search(r'ga',string_de_test)
if padrão:
    print("Padrão encontrado (1):",padrão)
else:
    print("Padrão não encontrado!")

    ## na pesquisa colocar ponto, mesmo dentro da raw_string,
## busca por um coringa: r"gat." busca tanto "gato" quanto "gata",
## que vier primeiro
## PAra buscar o ponto como caractere é só escrever ele ("\.")

    ## r"\w" busca por qualquer caractere menos espaço.
## r"\w\w\w\w" busca pela primeira iteração de uma palavra
## com no mínimo quatro caracteres.

padrão = re.search(r'\w\w\w\w',string_de_test)
if padrão:
    print("Padrão encontrado (2):",padrão.group())
else:
    print("Padrão não encontrado!")

# Buscando todas as palavras quem contenham os caracteres de
# pesquisa e responde quais são esses:
# \w{4} = \w\w\w\w
# \w{4,6} = de 4 a 6, inclusive, \w
# a{3} = aaa
padrão = re.findall(r'\w\w\w\w',string_de_test)
if padrão:
    print("Padrão encontrado (3):",padrão)
else:
    print("Padrão não encontrado!")

# Para a resposta vier com as palavras completas com número
# maior ou igual ao que é buscado, os caracteres ('+')
# especiais são agrupados como 1:
# \w{4} = \w\w\w\w
padrão = re.findall(r'\w\w\w\w+',string_de_test)
if padrão:
    print("Padrão encontrado (4):",padrão)
else:
    print("Padrão não encontrado!")

# Para respostas com menos caracteres que a busca ('*'):
padrão = re.findall(r'gat\w\w*',string_de_test)
if padrão:
    print("Padrão encontrado (5):",padrão)
else:
    print("Padrão não encontrado!")

# Procura por as seguintes letras ["..."] e responde elas em ordem:
padrão = re.findall(r'[gat]',string_de_test)
if padrão:
    print("Padrão encontrado (6):",padrão)
else:
    print("Padrão não encontrado!")

# Procura por as seguintes letras ["..."] e responde elas em ordem
# e agrupadas:
padrão = re.findall(r'[gat]+',string_de_test)
if padrão:
    print("Padrão encontrado (7):",padrão)
else:
    print("Padrão não encontrado!")

# Procura por as seguintes letras ["..."] e responde elas em ordem
# e agrupadas junto ao resto da palavra depois:
padrão = re.findall(r'[gat]+\w+',string_de_test)
if padrão:
    print("Padrão encontrado (8):",padrão)
else:
    print("Padrão não encontrado!")

# Procura por as seguintes letras ["..."] e responde elas em ordem
# e agrupadas junto ao resto da palavra antes e depois:
padrão = re.findall(r'\w+[gat]+\w+',string_de_test)
if padrão:
    print("Padrão encontrado (9):",padrão)
else:
    print("Padrão não encontrado!")

# regex101.com <- site para testar expressões regulares

# Pegando e-mails
import requests
economia = requests.get('http://www.ufjf.br/ecogv/institucional/docentes/perfilcontato/')

padrão = re.findall(r'[\w\.-]+@[\w-]+\.[\w+\.-]+',economia.text)
for i in padrão:
    if padrão:
        print("Padrão encontrado (10):",i)
    else:
        print("Padrão não encontrado!")

```
# #fim
