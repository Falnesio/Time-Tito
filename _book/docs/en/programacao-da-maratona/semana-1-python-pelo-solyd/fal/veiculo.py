# -*- coding: utf-8 -*-
"""
Created on Tue Dec 25 04:33:39 2018

Ex.2

EXECÍCIO:


@author: Fal
"""

class Veiculo:
    def __init__(self, cor, rodas, marca, tanque):
        self.cor = cor
        self.rodas = rodas
        self.marca = marca
        self.tanque = tanque
        
    def abastecer(self, litros):
        self.tanque += litros
