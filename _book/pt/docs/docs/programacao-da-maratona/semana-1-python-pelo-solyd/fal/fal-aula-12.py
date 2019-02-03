# -*- coding: utf-8 -*-
"""
Created on Fri Dec 28 23:26:41 2018

@author: Fal
"""
from typing import Dict, Any

import requests
import bs4

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

try:
    print(requisição.text) # puxa coisas do sítio
except Exception as e:
    print(e)