from PyDictionary import PyDictionary


class Dictionary:
    def __init__(self, word):
        dictionary = PyDictionary()

        print(dictionary.synonym(word))

Dictionary('this')
