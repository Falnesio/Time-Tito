# Anotações - Fal - Aula 12 - Requisições Web - Python Básico Solyd.md


```

import sys
import time

# no cmd
pip3 install requests
# ou
python3 -m pip install requests

import requests

requisição = none

try:
    requisição = requests.get(https://google.com)
except Exception as e:
    print("Requisição de erro:",e)

print(requisição.algumacoisa) # puxa coisas do sítio


```


# #fim
