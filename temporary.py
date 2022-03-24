import nltk
from nltk.corpus import wordnet
from difflib import SequenceMatcher

a = wordnet.synsets('management')
a = a[0].definition()
b = wordnet.synsets('administration')
b = b[0].definition()

a = "Hello, how are you?"
b = "How are you?"

# maybe use this instead of difflib https://stackoverflow.com/questions/65199011/is-there-a-way-to-check-similarity-between-two-full-sentences-in-python
ratio = SequenceMatcher(None, a, b).ratio()

print(a)
print(b)
print(ratio)
