'''
Fal - Aula 17 - Criando uma biblioteca - Python Básico Solyd
Criando Biblioteca
'''

import oauth2
import urllib.parse
import pprint
import json

class Twitter:

    def __init__(self, consumer_key, consumer_secret, token_key, token_secret):
        self.conexao(consumer_key, consumer_secret, token_key, token_secret)


    def conexao(self, consumer_key, consumer_secret, token_key, token_secret):
        # criar objetos básicos
        self.consumidor = oauth2.Consumer(consumer_key, consumer_secret)
        self.token = oauth2.Token(token_key, token_secret)
        self.cliente = oauth2.Client(self.consumidor, self.token)
        return self.cliente

    def post_console(self):
        tweet = input("Novo Tweet:\n")
        tweet_codificado = urllib.parse.quote(tweet, safe='')
        requisicao = self.cliente.request('https://api.twitter.com/1.1/statuses/update.json?status=' + tweet_codificado,
                                     method='POST')
        # decodificar
        req_decod = requisicao[1].decode()
        # tornar objeto do python, sendo transformado em dicionário
        req_obj = json.loads(req_decod)
        ## SAÍDA5
        pprint.pprint(req_obj)

    def post(self, tweet):
        tweet_codificado = urllib.parse.quote(tweet, safe='')
        requisicao = self.cliente.request('https://api.twitter.com/1.1/statuses/update.json?status=' + tweet_codificado,
                                     method='POST')
        # decodificar
        req_decod = requisicao[1].decode()
        # tornar objeto do python, sendo transformado em dicionário
        req_obj = json.loads(req_decod)
        ## SAÍDA5
        pprint.pprint(req_obj)

    def pesquisa_console(self):
        pesquisa = input("sua pesquisa:\n")
        pesquisa_codificada = urllib.parse.quote(pesquisa, safe='')
        requisicao = self.cliente.request('https://api.twitter.com/1.1/search/tweets.json?q=' + pesquisa_codificada)
        # decodificar
        req_decod = requisicao[1].decode()
        # tornar objeto do python, sendo transformado em dicionário
        req_obj = json.loads(req_decod)
        # puxar o texto principal dos tweets
        try:
            for i in range(len(req_obj['statuses'])):
                pprint.pprint(req_obj['statuses'][i]['user']['screen_name'])
                print("--" + "-" * len(req_obj['statuses'][i]['user']['screen_name']))
                pprint.pprint(req_obj['statuses'][i]['text'])
                print("")
        except:
            print("fim dos resultados")
            print("")

    def pesquisa(self, pesquisa):
        pesquisa_codificada = urllib.parse.quote(pesquisa, safe='')
        requisicao = self.cliente.request('https://api.twitter.com/1.1/search/tweets.json?q=' + pesquisa_codificada)
        # decodificar
        req_decod = requisicao[1].decode()
        # tornar objeto do python, sendo transformado em dicionário
        req_obj = json.loads(req_decod)
        # puxar o texto principal dos tweets
        try:
            for i in range(len(req_obj['statuses'])):
                pprint.pprint(req_obj['statuses'][i]['user']['screen_name'])
                print("--" + "-" * len(req_obj['statuses'][i]['user']['screen_name']))
                pprint.pprint(req_obj['statuses'][i]['text'])
                print("")
        except:
            print("fim dos resultados")
            print("")