'''
Associado ao Fal_bib_twitter.py
'''

from Fal_bib_twitter import Twitter

#consumer
consumer_key = ""
consumer_secret = ""
#token
token_key = ""
token_secret = ""

twitter = Twitter(consumer_key,consumer_secret,token_key,token_secret)

twitter.pesquisa("")
