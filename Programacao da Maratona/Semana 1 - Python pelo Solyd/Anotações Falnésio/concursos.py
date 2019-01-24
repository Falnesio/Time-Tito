'''
Programa para verificar concursos no site
https://www.concursosnobrasil.com.br/concursos/mg/
'''

import requests
import pprint
import re
import urllib.parse

site = requests.get("https://www.concursosnobrasil.com.br/concursos/mg/").text
portal = re.findall(r"\'href=\"(.*?)\".\'", site)
print(portal)

'''
municipios = open("municipios_MG.txt", "r")

for i in municipios:
    try:
        i = urllib.parse.quote(str(i).replace(" ", "-"), safe='')
        site = requests.get("https://www.concursosnobrasil.com.br/concursos/mg/concurso-camara-de-"+i+".html").text
        
        local = re.findall(r"(?<=CÃ¢mara)\w+...........", site)
        vagas = re.findall(r"(?<=<li><strong>)\w+...........", site)
        nivel = re.findall(r"(?<=necessÃ¡rio possuir nÃ­vel )\w+...............", site)
        salario = re.findall(r"R\$......... para...................", site)

        print(i)
        print(vagas)
        print(nivel)
        print(salario)
        print("-------------------------")
        
    except Exception as e:
        print(e)


for i in municipios:
    site = requests.get("https://www.concursosnobrasil.com.br/concursos/mg/concurso-"++".html")
'''

