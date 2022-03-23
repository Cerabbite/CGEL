#https://api.dictionaryapi.dev/api/v2/entries/en/<word>
from bs4 import BeautifulSoup
import requests

class Dictionary:
    def __init__(self, word):
        self.access_api = requests.get(f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}")
        self.get_word = BeautifulSoup(self.access_api.content, 'html.parser')
        print(self.get_word)

    def get_synonyms(self):
        pass

    def get_meaning(self):
        pass


Dictionary('this')
