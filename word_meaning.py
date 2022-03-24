#https://api.dictionaryapi.dev/api/v2/entries/en/<word>
from bs4 import BeautifulSoup
import requests
import json


"""
Check if words are synonyms or have a similar meaning if so there is a chance that they will be merged into one word
"""

class Dictionary:
    def __init__(self, word):
        self.access_api = requests.get(f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}")
        self.get_word = self.access_api.json()
        self.word = self.get_word[0] #self.get_word.decode("utf-8")
        #print(self.word)
        self.get_synonyms()
        self.get_meaning()

    def get_synonyms(self):
        self.synonyms = self.word["meanings"][0]
        #print(self.synonyms['definitions'])
        for i in range(len(self.synonyms['definitions'])):
        	print(self.synonyms["definitions"][i]['synonyms'])
        	

    def get_meaning(self):
        self.meaning = self.word["meanings"][0]
        for i in range(len(self.meaning['definitions'])):
        	print(self.meaning["definitions"][i]['definition'])
        #print(self.meaning)


Dictionary('good')
