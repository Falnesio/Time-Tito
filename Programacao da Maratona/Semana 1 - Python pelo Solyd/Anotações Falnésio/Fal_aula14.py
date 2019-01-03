"""
Created on Tue Dec 25 02:58:43 2018

Ex.1

EXECÍCIO: Crie um software de cotação de dolar em real
e d previsão de tempo em tmpo real

@author: Fal
"""

import requests
import re
import json
import time

## Dados gerais
# dados dolar
cotacao = requests.get('https://www.google.com/search?q=usd+brl')
dolar = re.findall(r"1 Dólar americano =..........", cotacao.text)
# dados clima
weather = requests.get('https://api.hgbrasil.com/weather/?format=json&woeid=455865')
clima_cidade = json.loads(weather.text)
results = clima_cidade['results']


def climas():
    print(results['city'],":",results['description'])
    print(results['date'],results['time'])
    print('temperatura atual',results['temp'])
    print("")
    for i in results['forecast']:
            print(i['date'],i['weekday'])
            print('max:',i['max'],'min:',i['min'])
            print(i['description'])
            print('')
    print('--------------------------')

while True:
    print ("Cotação:")
    print(dolar, time.ctime())
    print("")
    print("Clima:")
    climas()
    time.sleep(5)