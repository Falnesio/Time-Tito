# -*- coding: utf-8 -*-
"""
Created on Fri Dec 28 23:26:41 2018

@author: Fal
"""

import requests

try:
    requisição = requests.get("https://google.com")
except Exception as e:
    print("Requisição de erro:",e)

try:
    print(requisição.text) # puxa coisas do sítio
except Exception as e:
    print(e)