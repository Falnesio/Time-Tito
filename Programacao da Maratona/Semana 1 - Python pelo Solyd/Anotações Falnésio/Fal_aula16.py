'''
Mexendo no API do Twitter
Primeiro pensei em seguir com o curso mas prefiro fazer o tutorial
do próprio twitter. Então aqui vai.
https://developer.twitter.com/en/account/get-started
'''

''' 
 Create an app
  To use an API, we require you create an app as part of our OAuth
  authorization scheme. Visit the Apps page of this developer portal
  to create one. Then, return to this page to complete the next step.
'''

# criando "fal_primeiro_app" para obter chave
# "fal_primeiro_app" criado e chaves adquiridas, continuando com
# as aulas do solyd.

#---------------------------------------------------------------------

#consumer
consumer_key = "vJ7XvAROXpttRGHdOgN4pn0Ac"
consumer_secret = "JsONg6kuLI9tHpbcm8xbMUk5qXxSBRoP7k4L2puEx1evRwKh3t"
#token
token_key = "1005304557335908352-MDwFdupqCNfOtX1cvxoO30VFBppL51"
token_secret = "sOzWWx0etXbxl1tSAtQvMOydJpo5scFMGqKP5eRSE0zWN"

# baixar biblioteca pelo terminal "sudo pip install oauth2".
# abrir biblioteca oauth
import oauth2

# considerando que a requisição vem em formato json
import json

# criar objetos básicos
consumidor = oauth2.Consumer(consumer_key,consumer_secret)
token = oauth2.Token(token_key,token_secret)
cliente = oauth2.Client(consumidor, token)

# requisição da pesquisa (query)
while True:
    pesquisa = input("sua pesquisa:\n")
    pesquisa_codificada = urllib.parse.
    requisicao = cliente.request('https://api.twitter.com/1.1/search/tweets.json?q='+pesquisa)

    '''
    # requisição vem como tuple, 0 e 1
    print(type(requisicao))
    print(type(requisicao[0]))
    print(type(requisicao[1])) #sendo bytes, tem que decodificar em string
    '''

    #decodificar
    req_decod = requisicao[1].decode()

    #tornar objeto do python, sendo transformado em dicionário
    req_obj = json.loads(req_decod)

    # print(type(req_obj))

    ## SAÍDA5
    # para imprimir bonito
    import pprint

    '''
    # puxar o texto principal dos tweets
    for i in range(len(req_obj['statuses'])):
        pprint.pprint(req_obj['statuses'][i]['user']['screen_name'])
        pprint.pprint(req_obj['statuses'][i]['text'])
    '''

    # ou

    for tweet in req_obj['statuses']:
        pprint.pprint(tweet['user']['screen_name'])
        pprint.pprint(tweet['text'])
        print("")










