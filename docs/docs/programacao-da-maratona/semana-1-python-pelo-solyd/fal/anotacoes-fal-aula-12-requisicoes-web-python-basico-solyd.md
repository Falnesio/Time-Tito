# Anotações - Fal - Aula 12 - Requisições Web - Python Básico Solyd.md


```

import sys
import time

# no cmd
pip3 install requests
# ou
python3 -m pip install requests

import requests

cabeçalho = {"User-agent": "Windows 12",
             "Referer": "https://google.com",
             "cf-ipcountry": "US"}

meus_biscoitos = {"ultima-visita": "10-10-2020"} #cookies

dados = {"username":"flafal",
         "senha": "adasd2243"}


#puxando de putsreq.com
try:
    requisição = requests.post("https://putsreq.com/OCShNUJtBaVxEnh2HflW",
                               headers = cabeçalho,
                               cookies = meus_biscoitos,
                               data = dados) #("https://putsreq.com/OCShNUJtBaVxEnh2HflW/inspect") #("https://google.com")
except Exception as e:
    print("Requisição de erro:",e)

print(requisição.algumacoisa) # puxa coisas do sítio


```


# #fim
